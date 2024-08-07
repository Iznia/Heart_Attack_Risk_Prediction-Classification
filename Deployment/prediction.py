import streamlit as st
import pandas as pd
import pickle
from time import sleep
from PIL import Image


# Load the trained model
with open("best_dt_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Function to run the Streamlit app
def run():

    # Add title
    st.title('Heart Attack Prediction')
    st.write('By Iznia Azyati')

    # Tambahkan gambar
    image = Image.open('gambar2.jpg')  
    st.image(image, caption='Heart Attack Prediction Analysis')


    # Introduction
    st.subheader("📊 Heart Attack Risk Prediction")
    st.write("Selamat datang di aplikasi prediksi risiko serangan jantung!")
    st.write("Aplikasi ini memprediksi apakah seorang pasien berisiko mengalami serangan jantung berdasarkan informasi yang diberikan.")


    # Input form
    st.markdown('##  Input Data')
    with st.form('my_form'):

        with st.expander("Personal Information"):
            col1, col2, col3 = st.columns(3)

            # ID Pasien
            with col1:
                id = st.text_input("🆔Patient ID", help="Masukkan ID pasien. Contoh: ABC1234")

            # Jenis Kelamin
            with col2:
                gender = st.selectbox('🚻Sex', ['Male', 'Female'], help="Pilih jenis kelamin pasien.")

            # Usia
            with col3:
                age = st.number_input('👩🏻‍🦰Age', min_value=1, max_value=100, help="Masukkan usia pasien (antara 1 dan 100 tahun).")

        st.write("Health Information")

        # Kadar Kolesterol
        cholesterol = st.number_input('🩸Cholesterol', min_value=0, max_value=500, help="Masukkan kadar kolesterol pasien.")

        # Detak Jantung
        heart_rate = st.number_input('🫀Heart Rate', min_value=0, max_value=200, help="Masukkan heart rate pasien.")

        # Penyakit
        diabetes = st.selectbox('💉Diabetes', [0, 1], help="Pilih apakah pasien menderita diabetes (1 jika ya, 0 jika tidak).")
        smoking = st.selectbox('🚬Smoking', [0, 1], help="Pilih apakah pasien merokok (1 jika ya, 0 jika tidak).")
        obesity = st.selectbox('🙅🏻‍♀️Obesity', [0, 1], help="Pilih apakah pasien mengalami obesitas (1 jika ya, 0 jika tidak).")
        alcohol_consumption = st.selectbox('🍺Alcohol Consumption', [0, 1], help="Pilih apakah pasien mengonsumsi alkohol (1 jika ya, 0 jika tidak).")
        diet = st.selectbox('🚶🏻‍♂️‍➡️Diet', ['Average', 'Unhealthy', 'Healthy'], help="Pilih pola makan pasien.")
        stress_level = st.number_input('⛔Stress Level', min_value=0, max_value=10, help="Masukkan tingkat stres pasien (0-10).")
        bmi = st.number_input('🧍BMI', min_value=10.0, max_value=50.0, help="Masukkan BMI pasien.")
        triglycerides = st.number_input('💉Triglycerides', min_value=0, max_value=1000, help="Masukkan kadar trigliserida pasien.")
        continent = st.selectbox('🌏Continent', ['Africa', 'Europe', 'South America', 'North America', 'Australia', 'Asia'], help="Pilih benua tempat tinggal pasien.")

        submit = st.form_submit_button('🔍 let\'s Check the Predictions!')

    # Create DataFrame from user input
    data = {
            'Patient_ID': id,
            'Age': age,
            'Sex': gender,
            'Cholesterol': cholesterol,
            'Heart_Rate': heart_rate,
            'Diabetes': diabetes,
            'Smoking': smoking,
            'Obesity': obesity,
            'Alcohol_Consumption': alcohol_consumption,
            'Diet': diet,
            'Stress_Level': stress_level,
            'BMI': bmi,
            'Triglycerides': triglycerides,
            'Continent': continent
            }
    

    df = pd.DataFrame([data])
    st.dataframe(df)

    # Make prediction
    if submit:
       
        # Add progression
        bar = st.progress(0)
        for percent_complete in range(101):
            sleep(0.01)
            bar.progress(percent_complete)
        
        # Prediction result
        prediction = model.predict(df)[0]
        
        # Show prediction results
        if prediction == 0:
            st.write(f'Prediksi untuk ID {id}: 🟢 Tidak Berisiko Serangan Jantung')
        elif prediction == 1:
            st.write(f'Prediksi untuk ID {id}: 🔴 Berisiko Serangan Jantung')

if __name__ == '__main__':
    run()


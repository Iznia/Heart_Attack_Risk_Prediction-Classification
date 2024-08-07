# Import libraries
import eda
import prediction
import streamlit as st
  
# Add side bar
navigation = st.sidebar.selectbox('Navigation', ['Home', 'Exploratory Data Analysis', 'Heart Attack Risk Prediction'])

st.sidebar.markdown('# About')

# Introduction
st.sidebar.write('''Aplikasi ini dirancang untuk mengeksplorasi dan memprediksi risiko serangan jantung.''')
 
# Features
st.sidebar.write('''### Features:
- **Exploratory Data Analysis**: Explorasi data secara mendalam untuk menemukan pola dan wawasan terkait serangan jantung.
- **Heart Attack Risk Prediction**: Menggunakan model prediktif untuk meramalkan kemungkinan terjadinya serangan jantung pada pasien.''')

# Target Audience
st.sidebar.write('''### Target Audience
- **Profesional Medis**: Meningkatkan pemahaman dan mengurangi risiko terkait serangan jantung.
- **Peneliti**: Menganalisis dan memodelkan dataset serangan jantung untuk meningkatkan akurasi prediktif.
- **Data Scientist**: Mengembangkan dan mengevaluasi model machine learning untuk prediksi serangan jantung.''')



# Define the Home Page
def show_home():
    # Create title and introduction
    st.title('Welcome to the Heart Attack Risk Prediction Tool')
    st.write('''Alat ini menyediakan fungsi untuk Analisis Data Eksplorasi dan Prediksi Risiko Serangan Jantung.''')
    st.write('''Gunakan panel navigasi di sebelah kiri untuk memilih modul yang ingin digunakan.''')
    
    # Add image
    st.image('gambar3.jpg')
             
    st.markdown('---')
    

    # Dataset
    st.write('#### 📈 Dataset')
    st.markdown('''Dataset ini diperoleh dari Kaggle dan berisi informasi yang relevan tentang kejadian serangan jantung. 
                Untuk detail lebih lanjut, silahkan visit atau download dataset [Heart Attack Dataset](https://www.kaggle.com/datasets/iamsouravbanerjee/heart-attack-prediction-dataset/data).''')
    
    # Problem Statement
    st.write('#### ⚠️ Problem Statement')
    st.markdown('''Sebuah pusat kesehatan menghadapi tantangan dalam **memprediksi serangan jantung pada pasien**. Ini menyebabkan intervensi yang terlambat dan membahayakan nyawa pasien. Masalah ini berasal dari kompleksitas gejala serangan jantung dan berbagai faktor risiko, termasuk usia, kondisi kesehatan, dan pilihan gaya hidup. Tidak dapat dengan cepat mengidentifikasi siapa yang berisiko tinggi mengalami serangan jantung menyulitkan untuk bertindak cepat dengan bantuan medis. Akibatnya, pasien mungkin tidak mendapatkan perawatan segera yang mereka butuhkan, yang dapat mencegah konsekuensi serius seperti kecacatan jangka panjang atau bahkan kematian. Situasi ini menunjukkan kebutuhan mendesak akan alat yang lebih baik untuk memprediksi serangan jantung lebih awal dan menyesuaikan perawatan dengan kebutuhan setiap individu.''')
    
    # Objective
    st.write('#### 💡 Objective')
    st.markdown('''Proyek ini berfokus pada pembuatan **Clasiffication Model** untuk memprediksi serangan jantung, memilih yang terbaik dari `KNN`, `SVM`, `Logistic Regression`, `Decision Tree`, `Random Forest`, dan `XGBoost`. 
    Metode evaluasi utama untuk menilai kinerja model adalah `Recall`, yang akan digunakan untuk menentukan efektivitas masing-masing model dalam mengidentifikasi kasus serangan jantung.''')
    
# Create condition to access different pages
if navigation == 'Home':
    show_home()
elif navigation == 'Exploratory Data Analysis':
    eda.run()
elif navigation == 'Heart Attack Risk Prediction':
    prediction.run()



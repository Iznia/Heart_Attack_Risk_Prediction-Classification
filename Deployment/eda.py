# Import libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

# Define custom color palette
custom_palette = px.colors.qualitative.Set3

# Create the main program
def run():
    
    # Load the dataset
    data = pd.read_csv('P1M2_Iznia_Azyati_dataset.csv')
    
    # Add title to the app
    st.title('Exploratory Data Analysis: Heart Attack Prediction')
    
    # Tambahkan gambar
    image = Image.open('gambar1.jpg')  
    st.image(image, caption='Heart Attack Prediction Analysis')
    

    # Checkbox to display raw data
    if st.checkbox('Show Original data'):
        st.markdown('#### Original Data')
        st.write(data)


    # Section to display the pie chart
    st.subheader('Heart Attack Risk Percentage')
    # Menghitung persentase Risiko Serangan Jantung
    heart_attack_risk_counts = data['Heart Attack Risk'].value_counts()
    heart_attack_risk_percentages = heart_attack_risk_counts / heart_attack_risk_counts.sum() * 100
    # Plot the pie chart
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.pie(heart_attack_risk_percentages, labels=heart_attack_risk_percentages.index, autopct='%1.1f%%', startangle=140, colors=['lightcoral', 'lightskyblue'])
    ax.set_title('Heart Attack Risk Percentage')
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    # Show result
    st.pyplot(fig)

    # Explanation
    st.write("""
    Diagram pie di atas menunjukkan persentase individu yang memiliki risiko serangan jantung dan yang tidak memiliki risiko berdasarkan dataset yang ada. 
    Dari data yang tersedia, dapat dilihat bahwa:
    - 35.8% individu dalam dataset memiliki risiko serangan jantung.
    - 64.2% individu dalam dataset tidak memiliki risiko serangan jantung.

    Data ini menunjukkan bahwa mayoritas individu dalam dataset tidak memiliki risiko serangan jantung, namun persentase individu yang berisiko juga cukup signifikan. 
    Penting untuk menganalisis lebih lanjut faktor-faktor yang mempengaruhi risiko serangan jantung untuk dapat melakukan tindakan pencegahan yang lebih baik.
    """)

    
    # Dropdown for different analysis options
    st.markdown('#### Select Analysis')
    option = st.selectbox('Option:', ('Overview', 'Distribution Plots', 'Categorical Analysis', 'Correlation Heatmap', 'Heart Attack Risk Analysis'))
    
    # Overview analysis
    if option == 'Overview':
        st.subheader('Dataset Overview')
        st.write('Dataset ini berisi informasi tentang pasien, termasuk riwayat medis dan kebiasaan gaya hidup mereka, untuk memprediksi risiko serangan jantung.')
        st.markdown('###### Summary Statistics')
        numerical_columns = data[['Age', 'Cholesterol', 'Heart Rate', 'BMI', 'Triglycerides']]
        st.write(numerical_columns.describe())
        st.write('Dataset ini menyediakan berbagai variabel numerik dan kategorikal yang dapat digunakan untuk memprediksi risiko serangan jantung. Statistik ringkasan memberikan pemahaman awal tentang distribusi dan rentang data.')

    # Distribution plots analysis
    elif option == 'Distribution Plots':
        st.subheader('Distribution of Numerical Variables')
        numerical_columns = st.multiselect('Select columns to visualize', ['Age', 'Cholesterol', 'Heart Rate', 'BMI', 'Triglycerides'], ['Age', 'Cholesterol', 'Heart Rate', 'BMI', 'Triglycerides'])
        
        for idx, col in enumerate(numerical_columns):
            fig = px.histogram(data, x=col, title=f'Distribution of {col}', nbins=30, color_discrete_sequence=[custom_palette[idx]])
            st.plotly_chart(fig)
            st.markdown(f'Distribusi `{col}` menunjukkan penyebaran dan kecenderungan sentral data, memberikan wawasan tentang tren keseluruhan variabel ini.')

    # Categorical analysis
    elif option == 'Categorical Analysis':
        st.subheader('Categorical Data Analysis')
        categorical_columns = st.multiselect('Select columns to visualize', ['Sex', 'Diabetes', 'Smoking', 'Obesity', 'Alcohol Consumption', 'Diet', 'Continent'], ['Sex', 'Diabetes', 'Smoking', 'Obesity', 'Alcohol Consumption', 'Diet', 'Continent'])
        
        for idx, col in enumerate(categorical_columns):
            fig = px.histogram(data, x=col, title=f'{col} Distribution', color_discrete_sequence=[custom_palette[idx]])
            st.plotly_chart(fig)
            st.markdown(f'Distribusi `{col}` memberikan wawasan tentang frekuensi dan penyebaran berbagai kategori dalam variabel ini.')

    # Correlation heatmap analysis
    elif option == 'Correlation Heatmap':
        numerical_columns = data[['Age', 'Cholesterol', 'Heart Rate', 'BMI', 'Triglycerides']]
        corr = numerical_columns.corr()
        fig = px.imshow(corr, color_continuous_scale='Blues', title='Correlation Heatmap')
        st.plotly_chart(fig)
        st.markdown('The correlation heatmap highlights the relationships between different numerical variables, helping to identify potential patterns or collinearity.')
        st.markdown('Dari heatmap ini, dapat dilihat bahwa tidak ada korelasi yang sangat kuat antara variabel-variabel ini, yang menunjukkan bahwa faktor-faktor ini mungkin bekerja secara independen dalam mempengaruhi risiko serangan jantung.')

    # Heart attack risk analysis
    elif option == 'Heart Attack Risk Analysis':
        st.subheader('Analysis of Heart Attack Risk by Various Factors')
        categorical_columns = st.multiselect('Select columns to visualize', ['Sex', 'Diabetes', 'Smoking', 'Obesity', 'Alcohol Consumption', 'Diet', 'Continent'], ['Sex', 'Diabetes', 'Smoking', 'Obesity', 'Alcohol Consumption', 'Diet', 'Continent'])
        
        for idx, col in enumerate(categorical_columns):
            grouped_data = data.groupby([col, 'Heart Attack Risk']).size().reset_index(name='count')
            fig = px.bar(grouped_data, x=col, y='count', color='Heart Attack Risk', title=f'Heart Attack Occurrence by {col}', color_discrete_sequence=[custom_palette[0], custom_palette[1]], barmode='group')
            st.plotly_chart(fig)
            st.markdown(f'Diagram batang menunjukkan distribusi kejadian serangan jantung di berbagai kategori `{col}`, memberikan wawasan tentang faktor risiko potensial.')

# Run the app
if __name__ == '__main__':
    run()
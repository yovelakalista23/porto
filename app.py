import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

# Memuat dataset
url = "https://raw.githubusercontent.com/yovelakalista23/porto/refs/heads/main/data/diabetes_012_health_indicators_BRFSS2015.csv"
data_df = pd.read_csv(url)

# Pilihan visualisasi
if st.checkbox('Show Data'):
    st.write(data_df.head())

# Title
st.title("Health and Diabetes Analysis Dashboard")

# Placeholder for filtered data
st.write("### Filtered Data Summary")

# Correlation Matrix
st.subheader('Correlation Matrix')
fig, ax = plt.subplots(figsize=(6, 6))  # Resize the figure to fit better
sns.heatmap(data_df.corr(), annot=False, cmap='coolwarm', linewidths=0.5, ax=ax)
st.pyplot(fig)

# Create second row of 3 columns
col1, col2, col3 = st.columns(3) 

# Diabetes distribution by age
with col1:
    st.subheader('Diabetes Distribution by Age')
    fig, ax = plt.subplots(figsize=(6, 6))
    sns.countplot(x='Age', hue='Diabetes_012', data=data_df)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    st.pyplot(fig)

# BMI vs Diabetes
with col2:
    st.subheader('BMI Distribution by Diabetes Status')
    fig, ax = plt.subplots(figsize=(6, 6))
    sns.histplot(data_df[data_df['Diabetes_012'] == 1]['BMI'], kde=True, label='Diabetic', color='red', ax=ax)
    sns.histplot(data_df[data_df['Diabetes_012'] == 0]['BMI'], kde=True, label='Non-Diabetic', color='blue', ax=ax)
    ax.legend()
    st.pyplot(fig)

# Smoking and diabetes
with col3: 
    st.subheader('Relationshop between Smoking and Diabetes')
    fig, ax = plt.subplots(figsize=(6,4))
    sns.countplot(x='Smoker', hue='Diabetes_012', data=data_df)
    ax.set_xlabel('Smoker')
    ax.set_ylabel('Count')
    st.pyplot(fig)

    
# Create second row of 3 columns
col4, col5, col6 = st.columns(3)    

# Physical activity and diabetes    
with col4:
    st.subheader('Relationship between Physical Activity and Diabetes')
    fig, ax = plt.subplots(figsize=(6,4))
    sns.countplot(x='PhysActivity', hue='Diabetes_012', data=data_df)
    ax.set_xlabel('Physical Activity')
    ax.set_ylabel('Count')
    st.pyplot(fig)
    
# visualization with heatmap
with col5:
    # Calculating the percentage of diabetes based on smoking habits   
    smoker_vs_diabetes = pd.crosstab(data_df['Smoker'], data_df['Diabetes_012'], normalize='index') * 100 
    st.subheader('Effect of Smoking Habit on Diabetes')
    fig, ax = plt.subplots(figsize=(6,4))
    sns.heatmap(smoker_vs_diabetes, annot=True, cmap='coolwarm', cbar=True)
    ax.set_xlabel('Diabetes (0: Non, 1: Pre-diabetes, 2: Diabetes)')
    ax.set_ylabel('Smoker (0: Non Smoker, 1: Smoker)')
    st.pyplot(fig)
    
# Visualization with heatmap
with col6:
    #Calculating the percentage of diabetes based on alkohol habits
    alcohol_vs_diabetes = pd.crosstab(data_df['HvyAlcoholConsump'], data_df['Diabetes_012'], normalize='index') * 100
    st.subheader('Effect of Alkohol Habit on Diabetes')
    fig, ax = plt.subplots(figsize=(6,4))
    sns.heatmap(alcohol_vs_diabetes, annot=True, cmap='coolwarm', cbar=True)
    ax.set_xlabel('Diabetes (0: Non, 1: Pre-diabetes, 2: Diabetes)')
    ax.set_ylabel('Alcohol Consump (0: No, 1: Ya)')
    st.pyplot(fig)
    
st.caption('Yovela Kalista 2024')
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset/ElectricCarAccident.csv")

st.markdown("# Electric Car Accident In US")
st.markdown("This dataset includes accidents that occurred in the US from July 2021 to April 15, 2023, specifically involving vehicles equipped with level 2 ADAS.")
st.sidebar.markdown("# Electric Car Accident")

view = st.sidebar.radio("", ("View accidents of each brand", "View accidents in each state", "View accidents in each year", "View accidents of each model for a selected brand"))

if view == "View accidents of each brand":
    accident_counts = df.groupby('Brand').size().reset_index(name='Number of Accidents')

    temp = accident_counts.sort_values('Number of Accidents', ascending=False).reset_index(drop=True)
    other = temp[temp.index > 5]['Number of Accidents'].sum()
    temp = temp[temp.index <= 5]
    temp = temp.append({'Brand': "Other", 'Number of Accidents': other}, ignore_index=True)

    fig, ax = plt.subplots()
    ax.pie(temp['Number of Accidents'], labels=temp['Brand'], autopct='%1.1f%%')
    ax.set_title('Accidents of each Brand')
    st.pyplot(fig)

elif view == "View accidents in each state":
    accident_counts = df.groupby('State').size().reset_index(name='Number of Accidents')
    st.image("accident_by_state.png")

elif view == "View accidents in each year":
    accident_counts = df.groupby('Year').size().reset_index(name='Number of Accidents')

    fig, ax = plt.subplots()
    ax.plot(accident_counts['Year'], accident_counts['Number of Accidents'], marker='o')
    ax.set_title('Accidents by Year')
    ax.set_xlabel('Year')
    ax.set_ylabel('Number of Accidents')
    plt.xticks(accident_counts['Year'], map(int, accident_counts['Year']))
    st.pyplot(fig)

elif view == "View accidents of each model for a selected brand":
    selected_brand = st.sidebar.selectbox("Choose selected_brand:", df['Brand'].drop_duplicates().sort_values(), index=25)
    accident_counts = df.groupby(['Brand', 'Model']).size().reset_index(name='Number of Accidents')
    accident_counts = accident_counts[accident_counts['Brand'] == selected_brand]

    fig, ax = plt.subplots()
    ax.bar(accident_counts['Model'], accident_counts['Number of Accidents'])
    ax.set_xlabel('Model')
    ax.set_ylabel('Number of Accidents')
    ax.set_title("Accidents by Models")
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)

sorted_counts = accident_counts.sort_values('Number of Accidents', ascending=False).reset_index(drop=True)
st.dataframe(sorted_counts, width=800)

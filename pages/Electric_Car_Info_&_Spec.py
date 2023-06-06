import streamlit as st
import pandas as pd

df = pd.read_csv("dataset/ElectricCarData_Clean.csv")

st.markdown("# Electric Car Info & Spec")
st.sidebar.markdown("# Electric Car Info & Spec")

brands = st.multiselect("Choose selected_brand:", df["Brand"].drop_duplicates().sort_values(), ["Tesla "])
if brands:
    df = df[df["Brand"].isin(brands)]

body_style = st.sidebar.multiselect("Choose Body Style:", df["Body Style"].drop_duplicates().sort_values())
if body_style:
    df = df[df["Body Style"].isin(body_style)]

seat_range = st.sidebar.slider("Number of Seat", min_value=1, max_value=10, value=(1, 10), step=1)
st.sidebar.write(f"Selected Number of Seat: {seat_range[0]} - {seat_range[1]}")

price_range = st.sidebar.slider("Price Range", min_value=10000, max_value=100000, value=(10000, 1000000), step=10000)
st.sidebar.write(f"Selected Price Range: {price_range[0]} - {price_range[1]}")

df = df[(df['Price'] >= price_range[0]) & (df['Price'] <= price_range[1])]
df = df[(df['Seats'] >= seat_range[0]) & (df['Seats'] <= seat_range[1])]
df = df.reset_index(drop=True)
st.dataframe(df, width=800)

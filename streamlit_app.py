import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Smart Factory Dashboard")

# -----------------------------
# Load CSV files
# -----------------------------
sales_df = pd.read_csv("sales_sample.csv")
prod_df = pd.read_csv("production_sample.csv")
rec_df = pd.read_csv("recruitment_sample.csv")

# -----------------------------
# SALES DATA
# -----------------------------
st.header("Sales Overview")
store = st.selectbox("Select Store", sales_df['store'].unique())
product = st.selectbox("Select Product", sales_df['product'].unique())

filtered_sales = sales_df[(sales_df['store']==store) & (sales_df['product']==product)]
fig_sales = px.line(filtered_sales, x='date', y='units_sold', title=f"Units Sold: {product} in {store}")
st.plotly_chart(fig_sales)

# -----------------------------
# PRODUCTION DATA
# -----------------------------
st.header("Production Overview")
machine = st.selectbox("Select Machine", prod_df['machine_id'].unique())
shift = st.selectbox("Select Shift", prod_df['shift'].unique())

filtered_prod = prod_df[(prod_df['machine_id']==machine) & (prod_df['shift']==shift)]
fig_prod = px.bar(filtered_prod, x='date', y='units_produced', color='status', title=f"Units Produced by {machine} ({shift} shift)")
st.plotly_chart(fig_prod)

# -----------------------------
# RECRUITMENT DATA
# -----------------------------
st.header("Recruitment Overview")
role = st.selectbox("Select Role", rec_df['role'].unique())
location = st.selectbox("Select Location", rec_df['location_preference'].unique())

filtered_rec = rec_df[(rec_df['role']==role) & (rec_df['location_preference']==location)]
fig_rec = px.bar(filtered_rec, x='stage', y='time_in_stage_days', color='skills', title=f"Recruitment Pipeline: {role} in {location}")
st.plotly_chart(fig_rec)

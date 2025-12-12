import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# MAIN PROJECT TITLE & DESCRIPTION
# -----------------------------
st.title("Smart Factory Dashboard")
st.markdown("""
Welcome to the **Smart Factory Dashboard**.  

This dashboard demonstrates a simulated production and recruitment environment using **sample datasets** for Sales, Production, and Recruitment.  

It is designed to showcase my skills in **Python, Data Analytics, Data Visualization, and Streamlit**, and how I can turn raw data into actionable insights.  

Explore different sections to understand:
- Sales trends across stores and products
- Production efficiency and machine status
- Recruitment pipeline and candidate tracking
""")

# -----------------------------
# LOAD CSV FILES
# -----------------------------
sales_df = pd.read_csv("sales_sample.csv")
prod_df = pd.read_csv("production_sample.csv")
rec_df = pd.read_csv("recruitment_sample.csv")

# -----------------------------
# SALES SECTION
# -----------------------------
st.header("Sales Overview")
st.markdown("""
This section shows the **daily units sold** for different products across multiple stores.  

You can select a store and product to see **trends over time**, including the effect of promotions and holidays.  

**Insights you can explore:**
- Identify peak sales periods
- Compare product performance across stores
- Understand impact of promotions or holidays on sales
""")

store = st.selectbox("Select Store", sales_df['store'].unique())
product = st.selectbox("Select Product", sales_df['product'].unique())

filtered_sales = sales_df[(sales_df['store']==store) & (sales_df['product']==product)]
fig_sales = px.line(filtered_sales, x='date', y='units_sold', title=f"Units Sold: {product} in {store}")
st.plotly_chart(fig_sales)

# -----------------------------
# PRODUCTION SECTION
# -----------------------------
st.header("Production Overview")
st.markdown("""
This section tracks the **units produced by different machines and operators** across shifts.  

It also shows **machine status** (running, idle, maintenance, breakdown) and **downtime** for each machine.  

**Insights you can explore:**
- Machines with highest efficiency or most downtime
- Impact of operator and shift on production
- Patterns in machine breakdowns or maintenance needs
""")

machine = st.selectbox("Select Machine", prod_df['machine_id'].unique())
shift = st.selectbox("Select Shift", prod_df['shift'].unique())

filtered_prod = prod_df[(prod_df['machine_id']==machine) & (prod_df['shift']==shift)]
fig_prod = px.bar(filtered_prod, x='date', y='units_produced', color='status',
                  title=f"Units Produced by {machine} ({shift} shift)")
st.plotly_chart(fig_prod)

# -----------------------------
# RECRUITMENT SECTION
# -----------------------------
st.header("Recruitment Overview")
st.markdown("""
This section shows the **recruitment pipeline** for different roles and locations.  

You can select a role and location to track **candidates at different stages**, average time spent per stage, and skills distribution.  

**Insights you can explore:**
- Identify stages where candidates spend the most time
- Monitor efficiency of recruitment process
- Understand skills and sourcing effectiveness
""")

role = st.selectbox("Select Role", rec_df['role'].unique())
location = st.selectbox("Select Location", rec_df['location_preference'].unique())

filtered_rec = rec_df[(rec_df['role']==role) & (rec_df['location_preference']==location)]
fig_rec = px.bar(filtered_rec, x='stage', y='time_in_stage_days', color='skills',
                 title=f"Recruitment Pipeline: {role} in {location}")
st.plotly_chart(fig_rec)

# -----------------------------
# ADDITIONAL NOTES
# -----------------------------
st.markdown("""
**Tips for exploring the dashboard:**
- Use the dropdown menus to filter data interactively.
- Hover over charts to see exact values.
- Observe trends over time to identify insights quickly.

This dashboard is designed to simulate real-world business analytics and demonstrate my ability to **analyze data, build visualizations, and communicate insights effectively**.
""")

import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Smart Factory Analytics Platform",
    layout="wide"
)

# -------------------------------------------------
# TITLE & EXECUTIVE SUMMARY
# -------------------------------------------------
st.title("🏭 Smart Factory Analytics Platform")

st.markdown("""
### 📌 Executive Summary

This Smart Factory Analytics Platform demonstrates how **data-driven decision-making**
can be applied across **manufacturing operations, sales performance, and recruitment analytics**.

The dashboard integrates multiple business functions into a **single analytics view**,
similar to what leadership teams use to monitor performance and identify improvement opportunities.

#### 🔍 Business Problems Addressed
- Limited visibility into production efficiency and machine performance
- Difficulty understanding sales trends across stores and products
- Lack of insight into recruitment pipeline efficiency

#### 🛠️ Analytical Approach
- Structured and analysed operational datasets using **Python & Pandas**
- Built interactive dashboards using **Streamlit and Plotly**
- Enabled KPI-driven analysis through filters and visual exploration

#### 🎯 Business Value
- Faster operational insights
- Early identification of inefficiencies
- Better alignment between production, sales, and workforce planning

This project reflects **real-world analytics skills** applicable to Business Analyst,
Operations Analyst, and Data Analyst roles.
""")

st.divider()

# -------------------------------------------------
# LOAD DATA
# -------------------------------------------------
sales_df = pd.read_csv("sales_sample.csv")
prod_df = pd.read_csv("production_sample.csv")
rec_df = pd.read_csv("recruitment_sample.csv")

# -------------------------------------------------
# EXECUTIVE KPI CARDS
# -------------------------------------------------
st.subheader("📊 Executive KPIs Overview")

# Calculate KPIs
total_units_sold = sales_df['units_sold'].sum()
total_production = prod_df['units_produced'].sum()
avg_recruitment_time = rec_df['time_in_stage_days'].mean()
# Simulated efficiency: assume max possible units per machine per shift = 100
production_efficiency = round((total_production / (len(prod_df) * 100)) * 100, 2)

# Display KPI cards in 4 columns
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Units Sold", f"{total_units_sold}")
col2.metric("Total Production", f"{total_production}")
col3.metric("Avg Recruitment Time (days)", f"{round(avg_recruitment_time,2)}")
col4.metric("Production Efficiency", f"{production_efficiency}%")

st.divider()

# -------------------------------------------------
# SALES ANALYTICS
# -------------------------------------------------
st.header("📈 Sales Performance Analysis")

st.markdown("""
This section analyses **sales performance across stores and products**.

Decision-makers can evaluate demand patterns, identify high-performing products,
and understand the impact of seasonal or promotional activity.

**Key Business Questions Answered:**
- Which products perform best in each store?
- When do sales peak or decline?
- How do sales trends change over time?
""")

col1, col2 = st.columns(2)
with col1:
    store = st.selectbox("Select Store", sales_df['store'].unique())
with col2:
    product = st.selectbox("Select Product", sales_df['product'].unique())

filtered_sales = sales_df[
    (sales_df['store'] == store) &
    (sales_df['product'] == product)
]

fig_sales = px.line(
    filtered_sales,
    x='date',
    y='units_sold',
    title=f"Units Sold Over Time: {product} in {store}"
)

st.plotly_chart(fig_sales, use_container_width=True)

st.markdown("""
📌 **Insight Example:**  
Consistent peaks may indicate strong product-market fit, while sharp drops could signal
supply issues, pricing sensitivity, or reduced demand.
""")

st.divider()

# -------------------------------------------------
# PRODUCTION ANALYTICS
# -------------------------------------------------
st.header("🏭 Production & Operations Analysis")

st.markdown("""
This section focuses on **manufacturing performance and machine efficiency**.

It helps operations teams monitor production output, machine status, and downtime,
supporting continuous improvement initiatives.

**Key Business Questions Answered:**
- Which machines experience the most downtime?
- How does shift allocation impact output?
- Where are operational bottlenecks occurring?
""")

col3, col4 = st.columns(2)
with col3:
    machine = st.selectbox("Select Machine", prod_df['machine_id'].unique())
with col4:
    shift = st.selectbox("Select Shift", prod_df['shift'].unique())

filtered_prod = prod_df[
    (prod_df['machine_id'] == machine) &
    (prod_df['shift'] == shift)
]

fig_prod = px.bar(
    filtered_prod,
    x='date',
    y='units_produced',
    color='status',
    title=f"Daily Production Output: {machine} ({shift} Shift)"
)

st.plotly_chart(fig_prod, use_container_width=True)

st.markdown("""
📌 **Insight Example:**  
High downtime linked to specific shifts or machines may indicate maintenance gaps,
training needs, or scheduling inefficiencies.
""")

st.divider()

# -------------------------------------------------
# RECRUITMENT ANALYTICS
# -------------------------------------------------
st.header("👥 Recruitment Pipeline Analysis")

st.markdown("""
This section analyses the **recruitment lifecycle** across roles and locations.

HR teams can track candidate movement, identify delays, and optimise hiring strategies.

**Key Business Questions Answered:**
- Where do candidates spend the most time?
- Which roles take longer to fill?
- How effective is the recruitment funnel?
""")

col5, col6 = st.columns(2)
with col5:
    role = st.selectbox("Select Role", rec_df['role'].unique())
with col6:
    location = st.selectbox("Select Location", rec_df['location_preference'].unique())

filtered_rec = rec_df[
    (rec_df['role'] == role) &
    (rec_df['location_preference'] == location)
]

fig_rec = px.bar(
    filtered_rec,
    x='stage',
    y='time_in_stage_days',
    color='skills',
    title=f"Recruitment Pipeline Duration: {role} ({location})"
)

st.plotly_chart(fig_rec, use_container_width=True)

st.markdown("""
📌 **Insight Example:**  
Extended time in specific stages may indicate interview bottlenecks,
candidate skill mismatches, or approval delays.
""")

st.divider()

# -------------------------------------------------
# FINAL NOTES
# -------------------------------------------------
st.markdown("""
### 🧠 Key Takeaways

- Demonstrates **end-to-end analytics capability**
- Combines **engineering, business, and data analytics**
- Built using **free, open-source tools**
- Designed to mirror real organisational dashboards

This project highlights my ability to **translate data into insights and business value**,
a key requirement for analytics roles in modern organisations.
""")

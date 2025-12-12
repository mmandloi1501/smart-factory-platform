import pandas as pd
import numpy as np

# -----------------------------
# 1) Sales Data
# -----------------------------
dates = pd.date_range(start="2023-01-01", periods=365)
stores = ["Dublin", "Cork", "Galway"]
products = ["Product A", "Product B", "Product C"]

sales_data = []

for store in stores:
    for product in products:
        units = np.random.randint(5, 50, size=len(dates))
        price = np.random.uniform(10, 50)
        promo = np.random.choice([0,1], size=len(dates))
        holiday = np.random.choice([0,1], size=len(dates))
        for i, date in enumerate(dates):
            sales_data.append([date, store, product, round(price,2), units[i], promo[i], holiday[i]])

sales_df = pd.DataFrame(sales_data, columns=["date","store","product","price","units_sold","promotion","holiday"])
sales_df.to_csv("sales_sample.csv", index=False)

# -----------------------------
# 2) Production Log Data
# -----------------------------
machine_ids = ["M1","M2","M3"]
operator_ids = ["O1","O2","O3"]
status_options = ["running","idle","breakdown","maintenance"]

prod_data = []

for day in pd.date_range(start="2023-01-01", periods=30):
    for machine in machine_ids:
        for operator in operator_ids:
            units_produced = np.random.randint(10,100)
            status = np.random.choice(status_options)
            shift = np.random.choice(["A","B","C"])
            downtime = np.random.randint(0,60)
            prod_data.append([day, machine, operator, status, units_produced, shift, downtime])

prod_df = pd.DataFrame(prod_data, columns=["date","machine_id","operator_id","status","units_produced","shift","downtime_minutes"])
prod_df.to_csv("production_sample.csv", index=False)

# -----------------------------
# 3) Recruitment Pipeline Data
# -----------------------------
roles = ["Data Analyst","Production Manager","Recruiter"]
sources = ["LinkedIn","Referral","JobBoard","Agency"]
stages = ["Applied","PhoneScreen","TechInterview","Offer","Hired","Rejected"]

rec_data = []

for i in range(500):
    candidate_id = f"C{i+1}"
    applied_date = pd.Timestamp("2023-01-01") + pd.to_timedelta(np.random.randint(0,365), unit='d')
    role = np.random.choice(roles)
    source = np.random.choice(sources)
    stage = np.random.choice(stages)
    time_in_stage = np.random.randint(1,15)
    location = np.random.choice(["Dublin","Cork","Galway"])
    skills = ",".join(np.random.choice(["Python","Excel","SQL","PowerBI","Machine Learning","Tableau"], size=2, replace=False))
    rec_data.append([candidate_id, applied_date, role, source, stage, time_in_stage, location, skills])

rec_df = pd.DataFrame(rec_data, columns=["candidate_id","applied_date","role","source","stage","time_in_stage_days","location_preference","skills"])
rec_df.to_csv("recruitment_sample.csv", index=False)

print("Sample CSV files created: sales_sample.csv, production_sample.csv, recruitment_sample.csv")

import streamlit as st
import pandas as pd
import json
import matplotlib.pyplot as plt
from utils.scoring import calculate_score

st.set_page_config(page_title="100B Jobs Selector", layout="wide")
st.title("🚀 100B Jobs – Smart Candidate Selection App")

# Load data
try:
    with open("data/form-submissions.json", "r", encoding="utf-8") as f:
        raw_data = json.load(f)
except json.JSONDecodeError:
    st.error("❌ Invalid JSON file. Please check the format.")
    st.stop()

df = pd.DataFrame(raw_data)

if df.empty:
    st.warning("⚠️ No data found.")
    st.stop()

# Score calculation
df["score"] = df.apply(calculate_score, axis=1)
df = df.sort_values("score", ascending=False)

# Sidebar filters
st.sidebar.header("🔍 Filters")

# 1. Location filter
locations = df["location"].dropna().unique().tolist()
selected_location = st.sidebar.selectbox("📍 Filter by Location", ["All"] + locations)
if selected_location != "All":
    df = df[df["location"] == selected_location]

# 2. Availability filter
all_availabilities = sorted({a for sublist in df['work_availability'] for a in sublist})
selected_avail = st.sidebar.multiselect("🕒 Availability", all_availabilities, default=all_availabilities)
df = df[df["work_availability"].apply(lambda avail: any(a in avail for a in selected_avail))]

# 3. Skill filter (basic keyword search in work_experiences roles)
skills = ["Python", "JavaScript", "React", "Node", "C++", "Java", "AWS", "SQL"]
selected_skill = st.sidebar.selectbox("🧠 Filter by Skill", ["All"] + skills)

if selected_skill != "All":
    def has_skill(experiences):
        for exp in experiences:
            if selected_skill.lower() in exp.get("roleName", "").lower():
                return True
        return False
    df = df[df["work_experiences"].apply(has_skill)]

# Graph: Top 10 Locations
st.subheader("📊 Top 10 Locations of Candidates")

location_counts = df['location'].value_counts().head(10)
fig, ax = plt.subplots()
ax.bar(location_counts.index, location_counts.values, color='skyblue')
ax.set_ylabel("Number of Candidates")
plt.xticks(rotation=45)
st.pyplot(fig)

# All candidates table
st.subheader("📋 All Candidates (Filtered & Scored)")
st.dataframe(df[["name", "location", "score", "work_availability"]].reset_index(drop=True))

# Top 5 selection
top_5 = df.head(5)
st.subheader("🏆 Top 5 Selected Candidates")

for _, row in top_5.iterrows():
    with st.expander(f"✅ {row['name']} | Score: {row['score']}"):
        st.markdown(f"**📧 Email:** `{row['email']}`")
        st.markdown(f"**📍 Location:** {row['location']}")
        st.markdown(f"**💼 Experience:** {len(row.get('work_experiences', []))} roles")
        st.markdown(f"**🕒 Availability:** {', '.join(row.get('work_availability', []))}")
        st.markdown("---")

# Save top 5
top_5.to_json("selected/chosen.json", orient="records", indent=2)
st.success("✅ Top 5 saved to selected/chosen.json")

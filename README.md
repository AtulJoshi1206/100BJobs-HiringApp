# 🚀 100B Jobs – Candidate Selection App

This is a full-stack Streamlit web application built to help hiring teams shortlist the best 5 candidates from over 1000 form submissions. The raw data comes in unstructured JSON format, and this app processes, filters, scores, and selects the top candidates based on defined criteria.

---

## 🔍 Features

- ✅ Uploads and parses raw JSON form submissions
- ✅ Calculates candidate score based on experience, salary expectation, and availability
- ✅ Filters by:
  - Location
  - Availability (full-time / part-time)
  - Key technical skills (like Python, React, AWS, etc.)
- ✅ Visualizes top candidate locations using bar charts
- ✅ Saves selected top 5 candidates to a clean `chosen.json` file
- ✅ Fully interactive UI built with Streamlit – no setup needed to use

---

## 🧠 Scoring Logic

Each candidate is scored on:
- Number of work experiences
- Availability for full-time work
- Lower annual salary expectation

The score is used to sort and select the top 5 best-fit candidates.

---

## 🧰 Tech Stack

- **Frontend:** Streamlit
- **Backend Logic:** Python, Pandas
- **Visualization:** Matplotlib
- **Storage:** JSON
- **Directory Structure:**

100BJobs-HiringApp/
├── app.py # Main Streamlit app
├── utils/
│ └── scoring.py # Custom scoring logic
├── data/
│ └── form-submissions.json # Raw candidate data
├── selected/
│ └── chosen.json # Final top 5 candidates
└── README.md


---

## ▶️ How to Run

1. Clone this repo:

git clone https://github.com/AtulJoshi1206/100BJobs-HiringApp.git
cd 100BJobs-HiringApp 



![WhatsApp Image 2025-07-16 at 19 30 14_708a9a7c](https://github.com/user-attachments/assets/ed3c4982-21ab-4e8d-8d6f-b7617937d6ee)

![WhatsApp Image 2025-07-16 at 19 30 27_9ca8c129](https://github.com/user-attachments/assets/56b316d3-9da4-4bb6-bfb2-a42380aea67e)

![WhatsApp Image 2025-07-16 at 19 30 45_9718c134](https://github.com/user-attachments/assets/bc73b9f4-0294-4599-932f-3324de39491a)







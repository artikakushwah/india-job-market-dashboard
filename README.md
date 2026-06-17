# India Job Market Intelligence Dashboard

An end-to-end data analytics project that collects real job listing data from across India, analyzes hiring trends and in-demand skills, and presents findings through an interactive 4-page dashboard.

🔗 **Live Dashboard:** _(add GitHub Pages link here once set up)_
📁 **Data Source:** [Adzuna API](https://developer.adzuna.com/)

---

## 📌 What This Project Does

- Fetches **1,000 live job listings** across India using the Adzuna REST API
- Cleans and processes the data using Python and Pandas
- Extracts skills, experience levels, and city/sector breakdowns from raw text fields
- Visualizes everything in an interactive dashboard (built with HTML, CSS, and Chart.js)
- Includes a rule-based **Salary Estimator** based on experience, city, sector, and skills

---

## 🗂️ Project Structure

| File | Description |
|---|---|
| `fetch_jobs.py` | Python script that calls the Adzuna API and saves job data to CSV |
| `india_jobs.csv` | Raw dataset — 1,000 job listings (title, company, location, category, description, date posted) |
| `india_jobs_dashboard_corrected.html` | Interactive dashboard — open this file in any browser |

---

## 📊 Dashboard Pages

1. **Overview** — Key stats, jobs by sector, jobs by city, hiring volume by month, top hiring companies
2. **Deep Analysis** — Experience level distribution, skill frequency in job descriptions
3. **Salary Estimator** — Enter your profile (level, city, sector, skills) to get an estimated salary range
4. **Skill Gap** — Which skills are mentioned most/least across job descriptions

---

## 🛠️ Tech Stack

- **Python** (requests, pandas) — data collection & processing
- **Adzuna REST API** — real job listing data
- **HTML / CSS / JavaScript** — dashboard frontend
- **Chart.js** — interactive charts

---

## ⚠️ Important Notes on Data Honesty

- All charts on the **Overview**, **Deep Analysis**, and **Skill Gap** pages are built from real values in `india_jobs.csv`.
- The Adzuna India API does not return salary data, so all **salary figures** (in the Deep Analysis and Salary Estimator pages) are **market-research-based estimates**, not predictions trained on this dataset. This is clearly disclaimed within the dashboard itself.
- The "Hiring Volume by Month" chart reflects posting dates present in this one-time data pull (16 June 2026), not a continuously tracked live feed.

---

## 🚀 How to Run

1. Clone or download this repository
2. To re-fetch fresh data: install dependencies (`pip install requests pandas`) and run `python fetch_jobs.py` (you'll need your own free Adzuna API key)
3. To view the dashboard: simply open `india_jobs_dashboard_corrected.html` in any browser

---

## 📈 Key Insights Found

- **Bangalore** leads hiring with 24.1% of all listings
- **IT roles** dominate at 39.3% of the job market
- **Cloud** is the most-mentioned technical skill in job descriptions (50 mentions)
- Experienced roles (Mid/Senior/Manager) significantly outnumber Junior/Fresher roles
- **Tata Consultancy Services** is the single largest hirer in this dataset (58 open roles)

---

## 👤 Author

**Artika Singh Kushwah**
[GitHub](https://github.com/artikakushwah)

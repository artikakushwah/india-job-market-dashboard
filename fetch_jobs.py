import requests
import pandas as pd
import time

APP_ID = "439bd393"
APP_KEY = "eacab230c4357abae4c884757e2a2490"

all_jobs = []
total_pages = 20  # 50 jobs x 20 pages = 1000 jobs

print("Data fetch ho raha hai, wait karo...")

for page in range(1, total_pages + 1):
    url = f"https://api.adzuna.com/v1/api/jobs/in/search/{page}"
    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "results_per_page": 50,
    }
    try:
        response = requests.get(url, params=params)
        data = response.json()
        jobs = data.get("results", [])
        
        for job in jobs:
            all_jobs.append({
                "title": job.get("title", ""),
                "company": job.get("company", {}).get("display_name", ""),
                "location": job.get("location", {}).get("display_name", ""),
                "salary_min": job.get("salary_min", None),
                "salary_max": job.get("salary_max", None),
                "category": job.get("category", {}).get("label", ""),
                "description": job.get("description", "")[:300],
                "created": job.get("created", ""),
                "redirect_url": job.get("redirect_url", "")
            })
        
        print(f"Page {page}/{total_pages} done — {len(jobs)} jobs fetched")
        time.sleep(0.5)  # API rate limit se bachne ke liye

    except Exception as e:
        print(f"Page {page} mein error: {e}")

df = pd.DataFrame(all_jobs)
df.to_csv("india_jobs.csv", index=False)

print(f"\n✅ Done! Total {len(df)} jobs saved in india_jobs.csv")
print(df.head())

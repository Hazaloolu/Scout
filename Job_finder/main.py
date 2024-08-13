import requests
from dotenv import load_dotenv
from notion_client import Client
import os
import time


load_dotenv()

ADZUNA_APP_ID = os.getenv('ADZUNA_APP_ID')
ADZUNA_API_KEY = os.getenv('ADZUNA_API_KEY')


# NOTION_API_KEY = os.getenv('NOTION_API_KEY ')
# DATABASE_ID = os.getenv('DATABASE_ID')
NOTION_API_KEY = 'secret_KpVLVzlsA8dY4o7R3Dl8MuyOWVf876uKjvIhDhAb3pS'
DATABASE_ID = '624e08127af84ff0adb763089eb696a5'

notion = Client(auth=NOTION_API_KEY)



def fetch_jobs(what, where='', page=1):
    base_url = f"https://api.adzuna.com/v1/api/jobs/{where}/search/{page}"
    params = {
        'app_id': ADZUNA_APP_ID,
        'app_key': ADZUNA_API_KEY,
        'results_per_page': 20,
        'what': what,
        'what_and': 'backend developer'
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching jobs: {e}")
        return None

def add_job_to_notion(title, company, location, url, description):
    try:
        notion.pages.create(
            parent={'database_id': DATABASE_ID},
            properties={
                "Title": {"title": [{"text": {"content": str(title)}}]},
                "Company": {"rich_text": [{"text": {"content": str(company)}}]},
                "Location": {"rich_text": [{"text": {"content": str(location)}}]},
                "URL": {"url": str(url)},
                "Description": {"rich_text": [{"text": {"content": str(description)[:50]}}]},
            }
        )
        print(f"Added job: {title} at {company} in {location}")
    except Exception as e:
        print(f"Error adding job to Notion: {e}")
        print(f"Job details: Title={title}, Company={company}, Location={location}")

def main():
    stacks = ["Backend intern"]
    countries = ["ng","gb", "us"]

    for stack in stacks:
        for country in countries:
            page = 1
            while True:
                jobs = fetch_jobs(stack, country, page)
                if not jobs or not jobs.get('results'):
                    print(f"No more results for {stack} in {country}")
                    break

                print(f"Fetched {len(jobs['results'])} jobs for {stack} in {country}, page {page}")

                for job in jobs['results']:
                    title = job.get('title', 'No Title')
                    company = job.get('company', {}).get('display_name', 'No Company')
                    location = job.get('location', {}).get('display_name', 'No Location')
                    url = job.get('redirect_url', 'No URL')
                    description = job.get('description', 'No Description')

                    add_job_to_notion(title, company, location, url, description)

                page += 1
                time.sleep(1)  # Be cautious with rate limiting

if __name__ == "__main__":
    main()
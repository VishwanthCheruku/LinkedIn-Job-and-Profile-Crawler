import requests
from bs4 import BeautifulSoup
import time
import random

class JobCrawler:
    def __init__(self):
        self.base_url = "https://www.linkedin.com/jobs/search/"
        self.headers = {
            "User -Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }

    def crawl_jobs(self, location, designation):
        jobs = []
        params = {
            'keywords': designation,
            'location': location
        }
        response = requests.get(self.base_url, headers=self.headers, params=params)
        soup = BeautifulSoup(response.text, 'html.parser')

        for job in soup.find_all('div', class_='job-search-card'):
            title = job.find('h3').text.strip()
            company = job.find('h4').text.strip()
            location = job.find('span', class_='job-search-card__location').text.strip()
            description = job.find('p', class_='job-search-card__description').text.strip()
            skills = self.extract_skills(description)
            jobs.append({
                'title': title,
                'company': company,
                'location': location,
                'description': description,
                'skills': skills
            })
            time.sleep(random.uniform(1, 3)) 
            return jobs

    def extract_skills(self, description):
        return ["skill1", "skill2"]

crawler = JobCrawler()
jobs = crawler.crawl_jobs("New York", "Software Engineer")
print(jobs)
import requests
from bs4 import BeautifulSoup
import time
import random

class ProfileCrawler:
    def __init__(self):
        self.base_url = "https://www.linkedin.com/in/"
        self.headers = {
            "User -Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }

    def crawl_profiles(self, skills):
        profiles = []
        # Simulated search for profiles based on skills
        for skill in skills:
            response = requests.get(f"{self.base_url}search/results/people/?keywords={skill}", headers=self.headers)
            soup = BeautifulSoup(response.text, 'html.parser')

            for profile in soup.find_all('div', class_='search-result'):
                name = profile.find('span', class_='name').text.strip()
                title = profile.find('span', class_='headline').text.strip()
                location = profile.find('span', class_='location').text.strip()
                profiles.append({
                    'name': name,
                    'title': title,
                    'location': location,
                    'skills': skills
                })
                time.sleep(random.uniform(1, 3))  
        return profiles


profile_crawler = ProfileCrawler()
profiles = profile_crawler.crawl_profiles(["Python", "Django"])
print(profiles)
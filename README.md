# Job Profile Crawler

#Author - Cheruku Vishwanth Kumar Goud

## Introduction
This project aims to create a system that crawls job postings and LinkedIn profiles, stores the data in a database, and provides an API for querying relevant profiles and jobs.

## Setup Instructions
1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Set up the database using the provided schema.
4. Run the API with `python api/app.py`.

## Algorithms
- **Job Matching**: Utilizes keyword matching and skill overlap to calculate match scores.
- **Profile Matching**: Based on designation, location, and skills.

## System Design
- **Architecture Diagram**: ![image](https://github.com/user-attachments/assets/a0c3ad2b-2035-47fb-970a-dbf10c7aee27)

- **Database Schema**: Jobs and Profiles tables with appropriate indexing.
- **API Structure**: Two main endpoints for fetching profiles and jobs.

## Scalability Pros and Cons
- **Pros**: Supports multiple concurrent crawlers and API requests, designed for high throughput.
- **Cons**: Complexity in managing concurrent processes and potential rate-limiting issues.

## Assumptions and Limitations
- Compliance with LinkedIn's scraping policies.
- Limited to public data available on LinkedIn.

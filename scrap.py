import requests
from bs4 import BeautifulSoup

URL = 'https://realpython.github.io/fake-jobs/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')

job_elems = results.find_all('div', class_='card-content')

for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('h3', class_='company')
    location_elem = job_elem.find('p', class_='location')
    print(title_elem.text)
    print(company_elem.text)
    print(location_elem.text)
    print()

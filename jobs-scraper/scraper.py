import requests
from bs4 import BeautifulSoup

# Ref. https://realpython.com/beautiful-soup-web-scraper-python/#scrape-the-fake-python-job-site

class BFSoupScrapper: 

    def execute(self):
        URL = "https://realpython.github.io/fake-jobs/"
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")
        self.results = soup.find(id="ResultsContainer")
        # print(results.prettify())
        # print(page.text)
    
    def print_content(self, job_elements):
        # job_elements = self.results.find_all("div", class_="card-content")
        for job_element in job_elements:
            title_element = job_element.find("h2", class_="title")
            company_element = job_element.find("h3", class_="company")
            location_element = job_element.find("p", class_="location")
            links = job_element.find_all("a")
            for link in links:
                link_url = link["href"]
            print(f"Apply here: {link_url}\n")
            print(title_element.text.strip())
            print(company_element.text.strip())
            print(location_element.text.strip())

            print()


    def get_special(self, keyword):
        keyword_jobs = self.results.find_all("h2", string=lambda text: keyword in text.lower())
        keyword_job_elements = [
            h2_element.parent.parent.parent for h2_element in keyword_jobs
        ]
        # print(keyword_jobs)
        # return keyword_jobs
        return keyword_job_elements


subj = BFSoupScrapper()
subj.execute()
jobs = subj.get_special("python")
subj.print_content(jobs)

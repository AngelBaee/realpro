import requests

def get_page_content(url):
    response = requests.get(url)
    return response.text

from bs4 import BeautifulSoup

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    headings = soup.find_all('h1')
    for heading in headings:
        print(heading.text)



def search_keyword(keyword,html):
    soup = BeautifulSoup(html, 'html.parser')
    results = []
    paragraphs = soup.find_all('p')
    for paragraph in paragraphs:
        if keyword in paragraph.text:
            results.append(paragraph.text)

    return results    

url = 'https://proffclean24.ru/'   
keyword = "python"

html = get_page_content(url)
results = search_keyword(keyword, html)

for result in results:
    print(result)

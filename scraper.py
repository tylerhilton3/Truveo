import requests
from bs4 import BeautifulSoup

def get_text(url):
    result = requests.get(url)

    soup = BeautifulSoup(result.text, 'html.parser')

    title = soup.find('h1')
    if not title:
        title = soup.find('h2')

    article = soup.find('article')
    if article is None:
        article = soup.find('div', class_='article-body')

    content = []
    if title:
        content.append(f"Title: {title.get_text()}")

    if article:
        paragraphs = article.find_all('p')
    else:
        paragraphs = soup.find_all('p')

    content.append("\n".join([p.get_text() for p in paragraphs]))

    bullet_points = article.find_all(['ul', 'ol']) if article else soup.find_all(['ul', 'ol'])
    for bullet_list in bullet_points:
        content.append("\nBullet Points:")
        for li in bullet_list.find_all('li'):
            content.append(f"- {li.get_text()}")
        
    full_content = "\n".join(content)
    return full_content

def get_html(url):
    result = requests.get(url)
    html = result.text
    return html


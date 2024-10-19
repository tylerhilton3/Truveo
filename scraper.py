import requests
from bs4 import BeautifulSoup

# Get URL input from user

def get_text(url):
    # Fetch the content from the URL
    result = requests.get(url)

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(result.text, 'html.parser')

    # Extract the title of the article (commonly in h1 or h2 tags) saokdjsao idjiaso
    title = soup.find('h1')
    if not title:
        title = soup.find('h2')  # Fallback if h1 is not found

    # Extract the main article content (modify based on site structure)
    article = soup.find('article')  # Looks for an article tag
    if article is None:
        # If no article tag, look for a main div or section tag
        article = soup.find('div', class_='article-body')

    # Extract text from paragraphs, bullet points (ul, ol, li), and other elements
    content = []

    # Add the title to content
    if title:
        content.append(f"Title: {title.get_text()}")

    # Add paragraphs to content
    if article:
        paragraphs = article.find_all('p')
    else:
        paragraphs = soup.find_all('p')  # If no article or div, get all paragraphs

    content.append("\n".join([p.get_text() for p in paragraphs]))

    # Extract bullet points (ul > li or ol > li)
    bullet_points = article.find_all(['ul', 'ol']) if article else soup.find_all(['ul', 'ol'])
    for bullet_list in bullet_points:
        content.append("\nBullet Points:")
        for li in bullet_list.find_all('li'):
            content.append(f"- {li.get_text()}")
        

    # Join and print the content
    full_content = "\n".join(content)
    return full_content

def get_html(url):
    result = requests.get(url)
    html = result.text
    return html


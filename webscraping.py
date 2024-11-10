import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.w3schools.com/'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    titles = []
    descriptions = []
    links = []

    for title in soup.find_all('h2'):
        title_text = title.get_text().strip()
        titles.append(title_text)

        description_tag = title.find_next('p')
        if description_tag:
            description_text = description_tag.get_text().strip()
        else:
            description_text = "No description available"
        descriptions.append(description_text)

        link_tag = title.find_next('a')
        if link_tag and link_tag.has_attr('href'):
            link_url = link_tag['href']
        else:
            link_url = "No link available"
        links.append(link_url)

    df = pd.DataFrame({
        'Title': titles,
        'Description': descriptions,
        'Link': links
    })

    df.to_excel('scraped_details2.xlsx', index=False)

    print("Data successfully saved to 'scraped_details.xlsx'")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

import requests
from bs4 import BeautifulSoup

def scrape_webpage(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404)

        # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract titles and links
        data = []
        for item in soup.find_all('div', class_='mw-parser-output'):
            for link in item.find_all('a', href=True):
                title = link.text.strip()
                href = link['href']
                # Exclude non-article links (e.g., external links, edit links)
                if href.startswith('/wiki/') and ':' not in href:
                    data.append({'title': title, 'link': 'https://en.wikipedia.org' + href})

        return data
    except requests.exceptions.RequestException as e:
        print("Error fetching webpage:", e)
        return None
    except Exception as e:
        print("An error occurred:", e)
        return None

def main():
    url = "https://en.wikipedia.org/wiki/Main_Page"
    scraped_data = scrape_webpage(url)

    if scraped_data:
        print("Scraped Data:")
        for item in scraped_data:
            print(f"Title: {item['title']}")
            print(f"Link: {item['link']}")
            print()  # Add a blank line for better readability
    else:
        print("No data scraped.")

if __name__ == "__main__":
    main()

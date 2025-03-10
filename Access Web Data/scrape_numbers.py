from urllib.request import urlopen
from urllib.error import URLError
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def validate_url(url):
    pattern = r'^https?://[^\s/$.?#].[^\s]*$'
    return bool(re.match(pattern, url))

def sum_comments(url):
    if not validate_url(url):
        print("Error: Invalid URL format")
        return
        
    try:
        # Open URL and read HTML
        html = urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, "html.parser")

        # Find all span tags with class="comments"
        spans = soup('span', {'class': 'comments'})
        
        # Sum the numbers
        total = sum(int(span.contents[0]) for span in spans)
        
        # Print results
        print(f"Count {len(spans)}")
        print(f"Sum {total}")
        
    except URLError as e:
        print(f"Error accessing URL: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Get URL from user
    url = input('Enter URL: ')
    sum_comments(url)
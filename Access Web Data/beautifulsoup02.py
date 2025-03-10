import urllib.request
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors for https
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def process_url(url, position):
    """Process a single URL and return the name and next URL at given position"""
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    # Get all anchor tags
    tags = soup('a')
    
    if position > len(tags):
        raise ValueError(f"Position {position} exceeds available links ({len(tags)})")
        
    # Get name and URL at specified position (adjusting for 0-based index)
    target_tag = tags[position-1]
    return target_tag.contents[0], target_tag.get('href', None)

def follow_links(start_url, count, position):
    """Follow links count times at specified position"""
    current_url = start_url
    
    # Follow links specified number of times
    for i in range(count + 1):  # +1 to include initial URL
        print(f"Retrieving: {current_url}")
        name, next_url = process_url(current_url, position)
        current_url = next_url
        
        if i == count:  # On last iteration
            return name

def main():
    # Get user input
    url = input('Enter URL: ')
    count = int(input('Enter count: '))
    position = int(input('Enter position: '))
    
    try:
        final_name = follow_links(url, count, position)
        print(f"\nLast name found: {final_name}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
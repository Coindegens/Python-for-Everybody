import urllib.request
import json

def get_sum_from_json_url(url):
    # Retrieve the JSON data
    print(f'Retrieving {url}')
    data = urllib.request.urlopen(url).read().decode()
    print(f'Retrieved {len(data)} characters')
    
    # Parse JSON
    js = json.loads(data)
    
    # Extract comments and calculate sum
    comments = js['comments']
    count = len(comments)
    total = sum(comment['count'] for comment in comments)
    
    return count, total

def main():
    while True:
        try:
            url = input('Enter location: ')
            if len(url) < 1:
                break
                
            count, total = get_sum_from_json_url(url)
            print(f'Count: {count}')
            print(f'Sum: {total}')
            break
            
        except Exception as e:
            print(f'Error: {e}')
            continue

if __name__ == '__main__':
    main()
import urllib.request
import xml.etree.ElementTree as ET

def get_sum_from_xml_url(url):
    # Retrieve the XML data
    print(f'Retrieving {url}')
    data = urllib.request.urlopen(url).read()
    print(f'Retrieved {len(data)} characters')
    
    # Parse XML
    tree = ET.fromstring(data)
    
    # Find all count elements using XPath
    counts = tree.findall('.//count')
    
    # Sum up the counts
    total = sum(int(count.text) for count in counts)
    
    return len(counts), total

def main():
    while True:
        try:
            url = input('Enter location: ')
            if len(url) < 1:
                break
                
            count, total = get_sum_from_xml_url(url)
            print(f'Count: {count}')
            print(f'Sum: {total}')
            break
            
        except Exception as e:
            print(f'Error: {e}')
            continue

if __name__ == '__main__':
    main()
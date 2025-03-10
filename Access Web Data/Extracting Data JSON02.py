import urllib.request
import urllib.parse
import json

def get_geolocation_data(address):
    """Retrieve geolocation data for given address from OpenGeo API"""
    base_url = 'http://py4e-data.dr-chuck.net/opengeo?'
    
    # Build query parameters
    params = {'q': address}
    url = base_url + urllib.parse.urlencode(params)
    
    print(f'Retrieving {url}')
    
    # Get and parse JSON response
    try:
        uh = urllib.request.urlopen(url)
        data = uh.read().decode()
        print(f'Retrieved {len(data)} characters')
        
        js = json.loads(data)
        if 'features' in js and len(js['features']) > 0:
            return js['features'][0]
        else:
            print('No features found in response')
            return None
            
    except Exception as e:
        print('Error:', e)
        return None

def main():
    address = input('Enter location: ')
    if len(address) < 1: 
        print('==== Empty Address ====')
        return
    
    feature = get_geolocation_data(address)
    if feature and 'properties' in feature:
        plus_code = feature['properties'].get('plus_code')
        if plus_code:
            print(f'Plus code {plus_code}')
        else:
            print('==== Plus Code Not Found ====')
    else:
        print('==== Failure To Retrieve ====')

if __name__ == '__main__':
    main()
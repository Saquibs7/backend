import requests
import os

url = "http://127.0.0.1:5002/api/search"

try:
    # Check if the file exists
    if not os.path.exists('sample2.jpg'):
        print("Error: sample2.jpg doesn't exist in the current directory")
        exit(1)
    
    with open('sample2.jpg', 'rb') as img_file:
        files = {'image': img_file}
        
        try:
            response = requests.post(url, files=files)
            print(f"Status code: {response.status_code}")
            print(response.json())
        except requests.exceptions.ConnectionError:
            print(f"Error: Could not connect to server at {url}")
        except Exception as e:
            print(f"Error during request: {e}")
            
except Exception as e:
    print(f"Error: {e}")

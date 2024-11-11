import requests
import time

# URL of your page
url = 'https://comiconuserregistration.onrender.com/'  # Replace with your URL

# Interval time (in seconds) between each request
interval = 40  # Adjust as needed (e.g., every 60 seconds)

while True:
    try:
        # Send a GET request to the server
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Successfully pinged the server at {url}")
        else:
            print(f"Failed to ping the server. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error pinging the server: {e}")
    
    # Wait for the specified interval before pinging again
    time.sleep(interval)

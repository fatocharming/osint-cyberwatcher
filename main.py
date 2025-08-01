import requests
from urllib.parse import urlparse

def get_http_headers(url):
    """
    Fetch and display HTTP headers for a given URL.
    
    Args:
        url (str): The target URL to analyze.

    Returns:
        dict: A dictionary containing HTTP headers.
    """
    try:
        response = requests.get(url)
        # If the request was successful, return the headers
        if response.status_code == 200:
            return response.headers
        else:
            print(f"Failed to retrieve headers. Status code: {response.status_code}")
            return {}
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return {}

def display_headers(headers):
    """
    Display the HTTP headers in a readable format.
    
    Args:
        headers (dict): Dictionary of HTTP headers.
    """
    print("\nHTTP Headers:")
    for key, value in headers.items():
        print(f"{key}: {value}")

def analyze_url(url):
    """
    Analyze the provided URL and fetch its HTTP headers.
    
    Args:
        url (str): The target URL to analyze.
    """
    print(f"Analyzing URL: {url}")
    headers = get_http_headers(url)
    if headers:
        display_headers(headers)

if __name__ == "__main__":
    # Sample URLs for analysis
    urls_to_analyze = [
        "https://www.example.com",
        "https://httpbin.org/get",
    ]
    
    # Loop through each URL and analyze
    for url in urls_to_analyze:
        analyze_url(url)
```
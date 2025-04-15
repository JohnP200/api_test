import requests

def test_endpoint(url):
    try:
        # Send a GET request to the API endpoint
        respone = requests.get(url)

        # Check the status code amd print appropriate message
        if respone.status_code == 200:
            print(f"[+] {url} is accessible (Status Code: 200)")
        elif respone.status_code == 401: 
            print(f"[-] {url} is protected (Unauthorized - Status Code: 401)")
        elif respone.status_code == 403:
            print(f"[-] {url} is forbidden (Forbidden - Status Code: 403)")
        elif respone.status_code == 404:
            print(f"[-] {url} not found (Status Code: 404)")
        
    except requests.exceptions.RequestException as e:
        print(f"[!] An error occurred: {e}")
def main():
    # List of API endpoints to test
    endpoints = [
        "http://example.com/api/v1/resource1",
        "http://example.com/api/v1/secure-endpoint"
        "http://example.com/api/v1/nonexistent-endpoint"

    ]

    for url in endpoints:
        test_endpoint(url)

if __name__ == "__main__":
    main()
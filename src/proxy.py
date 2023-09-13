import requests


# Check connectivity to Google
def check_connectivity():
    url = 'http://www.google.com'
    timeout = 5
    try:
        request = requests.get(url, timeout=timeout)
        return False
    except (requests.ConnectionError, requests.Timeout):
        return True


import os


# Configure proxy
def configure_proxy(proxy_url):
    os.environ['http_proxy'] = proxy_url
    os.environ['https_proxy'] = proxy_url

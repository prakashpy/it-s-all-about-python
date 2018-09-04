import requests


response_endpoint = 'http://some_rest_api_endpoint.com/some_val'
try:
    resp = requests.post(response_endpoint)
except requests.exceptions.RequestException as e:
    print "Attempt to call API end point failed {} Error - ".format(response_endpoint)

""" we expect return of status code 200 for success """
if resp.status_code != 200:
    #logging.error("Expected api request to return value of zero for success but got %s", resp.status_code)
    print "status code wasn't 200"

api_return = resp.json()
if api_return != 0:
    #logging.error("Expected return value of 0 from API but got %s", str(api_return))    
    print "status response body was non 0"

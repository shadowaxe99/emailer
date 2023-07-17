# This is the integration points module

# Import necessary libraries
import requests

# Define a function to integrate with an API

def integrate_with_api(
        api_url,
        method='GET',
        headers=None,
        params=None,
        data=None):
    # Choose the request function based on the method
    if method == 'GET':
        request_func = requests.get
    elif method == 'POST':
        request_func = requests.post
    elif method == 'PUT':
        request_func = requests.put
    elif method == 'DELETE':
        request_func = requests.delete
    else:
        raise ValueError('Invalid method: {}'.format(method))

    # Send a request to the API
    response = request_func(api_url, headers=headers, params=params, data=data)

    # Check the status code of the response
    if response.status_code != 200:
        raise Exception(
            'GET request to {} returned status code {}'.format(
                api_url, response.status_code))

    # Return the response data
    return response.json()
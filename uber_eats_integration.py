import requests


def get_order_details(order_id, token):
    url = f'https://api.uber.com/v2/eats/order/{order_id}'
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept-Encoding': 'gzip'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def pretty_print_order_details(order_details):
    if order_details is None:
        print('No order details available.')
        return
    print(f'Order ID: {order_details['id']}')
    print(f'Store: {order_details['store']['name']}')
    print('Items:')
    for item in order_details['cart']['items']:
        print(f'  - {item['title']} x {item['quantity']}')
    print(f'Total: {order_details['payment']['charges']['total']['formatted_amount']}')


def get_ride_estimates(start_latitude, start_longitude, end_latitude, end_longitude, token):
    url = 'https://api.uber.com/v1.2/estimates/price'
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept-Language': 'en_US',
        'Content-Type': 'application/json'
    }
    params = {
        'start_latitude': start_latitude,
        'start_longitude': start_longitude,
        'end_latitude': end_latitude,
        'end_longitude': end_longitude
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def main():
    order_id = input('Enter the order ID: ')
    token = input('Enter the OAuth 2.0 Bearer token: ')
    order_details = get_order_details(order_id, token)
    pretty_print_order_details(order_details)
    start_latitude = input('Enter the start latitude for the ride: ')
    start_longitude = input('Enter the start longitude for the ride: ')
    end_latitude = input('Enter the end latitude for the ride: ')
    end_longitude = input('Enter the end longitude for the ride: ')
    ride_estimates = get_ride_estimates(start_latitude, start_longitude, end_latitude, end_longitude, token)
    print('Ride Estimates:')
    for estimate in ride_estimates['prices']:
        print(f'{estimate['display_name']}: {estimate['estimate']}')


if __name__ == '__main__':
    main()

# Placeholder functions for the additional APIs

def get_google_maps_data():
    pass

def get_weather_data():
    pass

def send_sms_with_twilio():
    pass

def process_payment_with_stripe():
    pass

def get_nasa_data():
    pass

def get_facebook_data():
    pass

def get_linkedin_data():
    pass

def get_google_drive_data():
    pass

def get_youtube_data():
    pass

def get_paypal_data():
    pass

def get_trello_data():
    pass

def get_slack_data():
    pass

def get_zoom_data():
    pass

def get_zapier_data():
    pass

def get_netflix_data():
    pass

def get_exercise_data():
    pass
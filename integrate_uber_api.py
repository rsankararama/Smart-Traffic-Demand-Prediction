import requests

UBER_API_KEY = "YOUR_UBER_API_KEY"

def get_uber_demand(latitude, longitude):
    """
    Fetches real-time ride demand from Uber API.
    - Inputs: latitude, longitude
    - Outputs: estimated ride demand at that location
    """
    url = "https://api.uber.com/v1.2/estimates/price"
    headers = {"Authorization": f"Token {UBER_API_KEY}"}
    params = {
        "start_latitude": latitude,
        "start_longitude": longitude,
        "end_latitude": latitude + 0.01,  
        "end_longitude": longitude + 0.01,  
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        return data["prices"]
    else:
        print(f"Error fetching Uber data: {response.status_code}")
        return None

if __name__ == "__main__":
    latitude, longitude = 40.7128, -74.0060  # Example: NYC
    demand_data = get_uber_demand(latitude, longitude)
    print("Uber Demand Data:", demand_data)

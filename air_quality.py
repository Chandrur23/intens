import requests

# Replace 'YOUR_API_KEY' with your actual Weatherbit API key
api_key = '64efca388d274fad847198f295f68b0c'
base_url = 'https://api.weatherbit.io/v2.0/current/airquality'

# Define the location for which you want to get the air quality details
latitude = '35.7796'  # Example: Latitude for Raleigh, NC
longitude = '-78.6382' # Example: Longitude for Raleigh, NC

# Construct the complete API URL
url = f"{base_url}?lat={latitude}&lon={longitude}&key={api_key}"

# Make a request to the Weatherbit API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Check if data is available
    if data.get('data'):
        # Extract relevant air quality details
        air_quality = data['data'][0]
        aqi = air_quality.get('aqi', 'N/A')
        pm10 = air_quality.get('pm10', 'N/A')
        pm25 = air_quality.get('pm25', 'N/A')
        o3 = air_quality.get('o3', 'N/A')
        no2 = air_quality.get('no2', 'N/A')
        so2 = air_quality.get('so2', 'N/A')
        co = air_quality.get('co', 'N/A')
        
        # Print the air quality details
        print(f"Air Quality Index (AQI): {aqi}")
        print(f"PM10: {pm10} µg/m³")
        print(f"PM2.5: {pm25} µg/m³")
        print(f"O3: {o3} ppb")
        print(f"NO2: {no2} ppb")
        print(f"SO2: {so2} ppb")
        print(f"CO: {co} ppb")
    else:
        print("Error: No air quality data available for the specified location.")
else:
    print(f"Error: Unable to fetch air quality data (Status code: {response.status_code})")


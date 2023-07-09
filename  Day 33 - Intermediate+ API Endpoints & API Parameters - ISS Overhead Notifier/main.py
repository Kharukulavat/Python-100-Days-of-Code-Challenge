import requests
response = requests.get(url = "http://api.open-notify.org/iss-now.json")

print(response) #>> <Response [200]>
print(response.status_code) #>> 200
print(response.raise_for_status) #>> <bound method Response.raise_for_status of <Response [200]>>

if response.status_code != 200:
    raise Exception("Bad response from ISS API")
elif response.status_code == 401:
    raise Exception("You are not authorized to access this data")

data = response.json() #The actual data
longitude = response.json()['iss_position']['longitude'] 
latitude = response.json()['iss_position']['latitude']
iss_position = (longitude, latitude)

print(data) #>> >> {'iss_position': {'longitude': '115.7088', 'latitude': '-11.2346'}, 'message': 'success', 'timestamp': 1687710736}
print(iss_position) #>> ('115.7088', '-11.2346')


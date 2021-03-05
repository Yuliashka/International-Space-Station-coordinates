# http://open-notify.org/Open-Notify-API/ISS-Location-Now/
# https://httpstatuses.com/
# https://www.latlong.net/Show-Latitude-Longitude.html

# to make a request to ISS location API:

# we import a library that helps us to do this:
# the request module is the most useful module for developers to work with APIs.
import requests


# TO GET THE DATA FROM END POINT:
# to get the data that we want from the endpoint we call a method get():
# the endpoint goes to our url and we have to check the docs to know what is the end point url is:
response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # if response.status_code != 200:
# #     raise Exception("Bad response from ISS API")
# if response.status_code == 404:
#     raise Exception("That resource does not exist.")
# To avoid lot of code with exceptions for every response status we can use a request module.
# Now if we don't have the response == 200 (pass) we will get an exception that has been raised
# that explains the problem
response.raise_for_status()

# TO GET THE INFO IN JSON FORMAT:
json_data = response.json()
longitude = json_data["iss_position"]["longitude"]
latitude = json_data["iss_position"]["latitude"]

# creating a tuple:
iss_position = (latitude, longitude)
print(json_data)
print(iss_position)

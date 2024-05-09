import requests
from datetime import datetime
pixela_endpoint = "https://pixe.la/v1/users"

TOKEN = "MadhavDahalSecretCode"
USERNAME = "madhav-dahal"
GRAPH_ID = "graph1"

# creating user
user_params = {
    "token": "MadhavDahalSecretCode",
    "username": "madhav-dahal",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

user_response = requests.post(url=pixela_endpoint, json=user_params)

# creating graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
yesterday = datetime(year=2024, month=5, day=8)
YESTERDAY = yesterday.strftime("%Y%m%d")
graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

#creating a pixel in the graph
new_pixel = {
    "date": YESTERDAY,
    "quantity": "15.5",
}
draw_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_response = requests.post(url=draw_endpoint, json=new_pixel, headers=headers)


# Updating the data in the pixel
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{YESTERDAY}"
update_data = {

    "quantity": "34.45",

}
update_response = requests.put(url=update_endpoint, json=update_data, headers=headers)


#Deleting the data in the pixel
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{YESTERDAY}"
delete_response = requests.delete(url=delete_endpoint, headers=headers)

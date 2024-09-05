import requests

url = "http://127.0.0.1:5000/add_user"
user1 = {"age_group": "<20", "gender": "male", "occupation": "student"}
user2 = {"age_group": "21-30", "gender": "female", "occupation": "accountant"}

users = [user1, user2]

for user in users:
    response = requests.post(url, json=user)
    print(response.text)

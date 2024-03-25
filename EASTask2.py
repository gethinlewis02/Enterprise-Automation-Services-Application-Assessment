import requests
import json

def StoreUserData():
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    UserData = response.json()
    
    JSONObject = json.dumps(UserData, indent = 2)
    
    with open('UserData.txt', 'w') as OutFile:
        OutFile.write(JSONObject)
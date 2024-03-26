import requests
import json

def StoreUserData():
    #This function retrieves user data from the JSONPlaceholder API, and stores
    #the data in JSON format in a text file called UserData.txt
    
    #Import user data from the JSONPlaceholder API
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    UserData = response.json()
    
    #Convert the List of dictionaries retrieved from JSONPlaceholder into a
    #a single string in JSON format
    JSONObject = json.dumps(UserData, indent = 2)
    
    #Save JSONObject string as a text file called UserData.txt
    with open('UserData.txt', 'w') as OutFile:
        OutFile.write(JSONObject)
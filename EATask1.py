# -*- coding: utf-8 -*-
import requests
import tabulate

def DisplayUserData():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    UserData = response.json()
    
    for User in UserData:
        User['city'] = User['address']['city']
        User.pop('address')
        
        User['company name'] = User['company']['name']
        User.pop('company')
    print(UserData[0].keys())    
    print(tabulate.tabulate(UserData,headers = 'keys', tablefmt = 'fancy_grid'))
    
DisplayUserData()
        
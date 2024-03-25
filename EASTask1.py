import requests
import tabulate as tb

def DisplayUserData():
    #This function imports user data from the JSONplaceholder API, reduces the
    #nested dictionaries for user address and company name to just the user's
    #city of residence and company name respectively and then displays the user
    #data in a table in the console.
    
    #Import user data from the JSONPlaceholder API
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    UserData = response.json()
    
    #Iterate over Users to remove nested dictionary elements, creating new
    #entries for city of residence and company name and deleting the rest of
    #the address and company data from the dictionary
    for User in UserData:
        User['city'] = User['address']['city']
        User.pop('address')
        
        User['company name'] = User['company']['name']
        User.pop('company')
    
    #Use the tabulate module to display user data in a table in the console        
    print(tb.tabulate(UserData, headers = 'keys', tablefmt = 'fancy_grid'))
    
        
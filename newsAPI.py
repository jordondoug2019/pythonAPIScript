#Choose an API from RapidAPI that interests you—make sure it has a free tier and simple authentication.
#Write a Python script that makes a request to your selected API, 
#using the appropriate endpoint and parameters to retrieve data. Save the response data to a variable, 
#and handle it as JSON to work with nested structures. Extract a specific item from the nested dictionary in the response,
#and print a statement that meaningfully displays this information. Have fun exploring the data you retrieve!

#make a request for selected API- Import requests 
#use endpoint and params to retireve data- API URL/ Code snippet from Rapid APi  
#save response to variable- raw=repsonse.json()
#get specific item form the nested dictionary in the responces- raw.items(), raw[items]
#print statement that clearly displays information- print("In todays news {raw[items]} ")

import requests
import random
from datetime import date #The module is datetime, date is the class

url = "https://financial-news6.p.rapidapi.com/news/headline"

querystring = {"lang":"en"}

headers = {
	"x-rapidapi-key": "744a48c97cmsh959f96c56a935ecp1209f4jsn124057d036b7",
	"x-rapidapi-host": "financial-news6.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

#print(response.json())

#assigned Response to a variable 
finNews= response.json()

#print(finNews.text)
#JSON response returns a list. access indexes of list and dictionary like Dating Script 
#print(type(finNews))
#print(finNews)

#Checked to make sure the HTTP Request would return a 200 Response Code 
print(response)
#for each in finNews:
 #   print(each["title"])

#Ok, Figured out how to access the index of the list and its Key pair.(I think thats what it is called)
#I always get confused on the dictionary/list and key,value pair thing
#Is it possible to automatically update with the API? 
#Use random number function for index maybe? 
#print(finNews[0]["title"])
#Imported Random Module to randomly access a different Financial News title every time the API is called. 
#I did a google search on how to randomly access an index. I also wanted to print the title of that index. 
#I know that has something to do with a key value pair but Im still confused on how to properly explain that 
#print(random.choice(finNews)["title"])

#Now I'm just optimizing. I want to add the current date every time the script is ran
print(f"Financial News for {date.today()}: {random.choice(finNews)["title"]} ")
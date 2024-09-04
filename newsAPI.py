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

url = "https://financial-news6.p.rapidapi.com/news/headline"

querystring = {"lang":"en"}

headers = {
	"x-rapidapi-key": "744a48c97cmsh959f96c56a935ecp1209f4jsn124057d036b7",
	"x-rapidapi-host": "financial-news6.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

#print(response.json())

finNews= response.json()
#print(finNews.text)
#JSON response returns a list. access indexes of list and dictionary like Dating Script 
print(type(finNews))
print(finNews)
print(response)
for each in finNews:
    print(each["title"])
from urllib.request import urlopen #import urlopen from request module
import json #import json module

print('-'*50)
print('Please Enter your city:\n')
city = str(input())    #asks for city name

#url to request for weather imformation from yahoo weather api. City name is concatenated in the url
url  = 'https://query.yahooapis.com/v1/public/yql?q=select%20units,astronomy,atmosphere,wind,location,item%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text=%22'+city+'%22)%20and%20u=%22c%22&format=json'
try:
	u = urlopen(url) #makes the GET request with the provided url
	page = u.read()  #reads and stores the response to the page variable
	u.close() #connection is closed

	json_data = json.loads(page) #the response is only json data and no html so json.loads() method will load the json data into json_data variable.
	print('-'*50)

	#uncomment below line to see raw json data
	#print(json_data)

	#uncomment below line to see well structured or beautified json data in the command line
	#print(json.dumps(json_data, sort_keys=True, indent=2))

	r_date  = json_data['query']['results']['channel']['item']['condition']['date'] #extract date from json data
	temp    = json_data['query']['results']['channel']['item']['condition']['temp'] #extract temperature from json data
	r_city  = json_data['query']['results']['channel']['location']['city']
	sunrise = json_data['query']['results']['channel']['astronomy']['sunrise']
	sunset  = json_data['query']['results']['channel']['astronomy']['sunset']
	humidity = json_data['query']['results']['channel']['atmosphere']['humidity']
	oveview = json_data['query']['results']['channel']['item']['condition']['text']
	temp    = json_data['query']['results']['channel']['item']['condition']['temp']

	#print all the fetched information
	print('Report Date :::::: '+str(r_date))
	print('City ::::::::::::: '+str(r_city))
	print('Temperature :::::: '+str(temp)+' *C')
	print('Condition :::::::: '+str(oveview))
	print('Sunrise :::::::::: '+str(sunrise))
	print('Sunset ::::::::::: '+str(sunset))
	print('Humidity ::::::::: '+str(humidity)+' %')

	print('-'*50)

except Exception as e:
	print('Error:'+str(e))


from django.shortcuts import render

# Create your views here.
def home(request):
	import json
	import requests


	if request.method == "POST":
		print(">>>>>>>>>>>>>> print here")
		zipcode = request.POST['zipcode']
		print(">>>>>>>>>>>>>> 12 <<<<<<<<<<<<<<<<<<<<<<<")	
		api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode +"&distance=25&API_KEY=A17FB90B-F0AA-42FB-AA0D-F4C567A8240B")	
		# return render(request, 'home.html', {'zipcode':zipcode})
		print(api_request)
	else:
		print(">>>>>>>>>>>>>> print in else")
		zipcode="60610"
		api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode +"&distance=25&API_KEY=A17FB90B-F0AA-42FB-AA0D-F4C567A8240B")
		print(">>>>>>>>>>>>>",api_request)
	print(">>>>>>>>>>>>>>> 21 <<<<<<<<<<<<<<<<<<<<<<<") 	
	# if api_request == "<Response [200]>":
	

	try:
		api = (json.loads(api_request.content) or len(api)==0)
		# print(api)
	except Exception as e:
		api = "Error..."

	if api[0]['Category']['Name'] == "Good":
		category_description="(0-50) Air quality is considered satisfactory, and air pollution poses little or no risk."
		category_color = "good"

	elif api[0]['Category']['Name'] == "Moderate":
		category_description="(51-100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
		category_color = "moderate"
	elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
		category_description="(101- 150) Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air."
		category_color = "Unhealthy_for_Sensitive_Groups"

	elif api[0]['Category']['Name'] == "Unhealthy":
		category_description="(151 - 200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
		category_color = "unhealthy"

	elif api[0]['Category']['Name'] == "Very Unhealthy":
		category_description="(201-300) Health alert: everyone may experience more serious health effects."
		category_color = "veryunhealthy"

	elif api[0]['Category']['Name'] == "Hazardous":
		category_description="(301-500) Health warnings of emergency conditions. The entire population is more likely to be affected."
		category_color = "hazardous"
					
	return render(request, 'home.html', {"api":api, "category_description":category_description, 'category_color':category_color})

	# else :
		# api = "Error..."

def about(request):
	return render(request, 'about.html', {})

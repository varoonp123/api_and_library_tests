import requests
import json
#Review json and http requests. Prints some universities with more than 1000 students. Uses the College Scorecard provided by the DOEd.
url = "https://api.data.gov/ed/collegescorecard/v1/schools"



parameters = {'api_key': 'eIBBYtzvK5wlx40khCOGmsOG73rylRma0LE7HMbh', "_fields": "school.name,2013.student.size,2013.admissions.admission_rate.overall", '2013.student.size__range':'1000..', '2013.admissions.admission_rate.overall__range': '...1'}

#gets the response equiv to sending HTTP request: url?key=val as denoted in parameters dict
r = requests.get(url,params = parameters)

#Now need to load the object as a json object
json_obj = json.loads(r.text)
print(json_obj)
print(json_obj['metadata'])
for res in json_obj['results']:
	print("{} had {} students in 2013. Its admission rate was {}".format (res['school.name'], res['2013.student.size'], res['2013.admissions.admission_rate.overall']))

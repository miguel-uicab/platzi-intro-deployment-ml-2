import requests

url = 'https://deployment-intro-ml-service-uaplhne67a-uc.a.run.app/v1/prediction'

json = {"opening_gross": 17435092.0,
 "screens": 3008.0,
 "production_budget": 65000000, 
 "title_year": 2012.0,
 "aspect_ratio": 2.35,
 "duration": 99.0,
 "cast_total_facebook_likes": 1375,
 "budget": 65000000.0,
 "imdb_score": 6.4}


response = requests.post(url, json=json)
print(response)
print(response.json())

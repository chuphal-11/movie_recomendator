import requests

def url_img(name):
    

    url = "https://imdb8.p.rapidapi.com/auto-complete"

    querystring = {"q":name}

    headers = {
	   "x-rapidapi-key": "b0cdd92d84msh81e0bf7be7ca224p147776jsnd98c2a60e81a",
	   "x-rapidapi-host": "imdb8.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    a=response.json()
    imgurl = a['d'][0]['i']['imageUrl']
    print(imgurl)
    return imgurl
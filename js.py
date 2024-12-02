import requests
import os
import dotenv
from dotenv import load_dotenv

load_dotenv()
api=os.getenv('API_KEY')

def img(title,year):
    
    url_omdb = 'http://www.omdbapi.com/?t='+title+'&y='+year+'&apikey=974b4b9c'
    url_imdb='https://api.themoviedb.org/3/search/movie?api_key='+api+'&query=Inception'
    response = requests.get(url_omdb)
    a=response.json()
    try:
        
        return a['Poster']
    except :
        
        return a['Error']
        
print(img('avatar','2009'))
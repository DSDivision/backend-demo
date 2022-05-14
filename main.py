from fastapi import FastAPI, Path, Query, HTTPException, status
import pandas as pd
from typing import Optional
import requests

app = FastAPI()

api_key = '15d2ea6d0dc1d476efbca3eba2b9bbfb'
recommendation_payload = {'api_key' : api_key,'language' : 'en-US'}

@app.get("/recommendation/{title}")
async def recommendation(title: str = Path(None, description="Title of the basis movie (mandatory)"),
                         #limit: Optional[int] = Query(None, description="Max nr of movies to list."),
                         #genre: Optional[str] = Query(None, description="Search by genre"),
                         #director: Optional[str] = Query(None, description="Search by director"),
                         #actor: Optional[str] = Query(None, description="Search by actor"),
                         #keyword: Optional[str] = Query(None, description="Search by a keyword from description"),
                         #release_year: Optional[int] = Query(None, description="Search by release year")
                         ):

    movie_payload = {
        
    'api_key' : api_key,
    'language' : 'en-US',
    'include_adult' : 'false',
    'query' : title

    }
    r = requests.get('https://api.themoviedb.org/3/search/movie', params=movie_payload, timeout=10)
    
    if(not r.ok):
        raise HTTPException(status_code = r.status_code, detail="Some error")

    if(r.json()['total_results']==0):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No movie found")

    movie_id = r.json()['results'][0]['id']

    r = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations', params=recommendation_payload, timeout=10)

    if(not r.ok):
        raise HTTPException(status_code = r.status_code, detail="Some error")
    
    results = r.json()['results']
    for movie in results:
        new_poster_path = 'https://image.tmdb.org/t/p/original'+movie['poster_path']
        movie['poster_path']=new_poster_path
        r = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}', params=recommendation_payload, timeout=10)
        imdb_id = r.json()['imdb_id']
        movie['imdb_path']='https://www.imdb.com/title/'+imdb_id
        r = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}/watch/providers?api_key={api_key}', timeout=10)
        providers = r.json()['results']['FI']['flatrate']
        movie['providers']=providers
        for provider in providers:
            new_logo_path = 'https://image.tmdb.org/t/p/original'+provider['logo_path']
            provider['logo_path'] = new_logo_path
    return results


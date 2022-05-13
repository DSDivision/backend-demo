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
    movie_id = r.json()['results'][0]['id']

    r = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations', params=recommendation_payload, timeout=10)

    if(not r.ok):
        raise HTTPException(status_code = r.status_code, detail="Some error")

    return r.json()['results']


from fastapi import FastAPI, Path, Query, HTTPException, status
import pandas as pd
from typing import Optional

app = FastAPI()

data = pd.read_csv("data/netflix_titles.csv",index_col=0).fillna("null")

@app.get("/recommendation")
async def recommendation(limit: Optional[int] = Query(10, description="Max nr of movies to list."),
                         title: Optional[str] = Query("", description="Search by title"),
                         genre: Optional[str] = Query("", description="Search by genre"),
                         director: Optional[str] = Query("", description="Search by director"),
                         actor: Optional[str] = Query("", description="Search by actor"),
                         keyword: Optional[str] = Query("", description="Search by a keyword from description"),
                         release_year: Optional[int] = Query(None, description="Search by release year")):

    
    sample = data.loc[data['title'].str.contains(title) &
                      data['listed_in'].str.contains(genre) &
                      data['director'].str.contains(director) &
                      data['cast'].str.contains(actor) &
                      data['description'].str.contains(keyword)]
    if release_year!=None:
        sample = sample.loc[sample['release_year']==release_year]
    if(len(sample)==0):
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="No media found")
        
    return sample.head(limit).to_dict(orient="index")

@app.get("/recommendation/{show_id}")
async def getMovie(show_id: str = Path(None, description="An id of the show")):
    if(show_id not in data.index):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie with that id does not exist")
    return data.loc[show_id].to_dict()
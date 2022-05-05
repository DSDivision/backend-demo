from fastapi import FastAPI
import pandas as pd

app = FastAPI()

data = pd.read_csv("data/netflix_titles.csv")

@app.get("/recommendation")
async def recommendation():
    sample = data.sample().iloc[0]
    return {"movie": {
            "title": sample.title,
            "genre": sample.listed_in,
            "description": sample.description
        }
    }
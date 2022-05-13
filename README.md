# backend-demo
Temporary playground for backend testing


# Setup

```bash
git clone git@github.com:DSDivision/backend-demo.git
cd backend-demo
pip install pandas "FastAPI[all]"
uvicorn main:app --reload
```

Access the api in your browser, at: http://127.0.0.1:8000/docs.
There you can see the generated docs for the api, and can try out the functionality.
Currently there is 1 GET function: enter a movie title to get a list of recommendations.
Add the 'poster_path' to this url to get the poster image: https://image.tmdb.org/t/p/original
If nothing is found there's an internal server error. More coming soon!

Have fun :)

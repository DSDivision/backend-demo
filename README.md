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
Currently there's only one simple GET function that'll return a single random recommendation in the form:

```json
{
    "movie": {
        "title": <title-of-the-movie>,
        "genre": <list-of-genres>,
        "description": <shortish-description>
    }
}
```

Have fun :)

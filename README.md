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
Currently there are 2 GET functions, one with basic search functionality and other for getting a specific movie by id.
No errors are caught atm.


Have fun :)

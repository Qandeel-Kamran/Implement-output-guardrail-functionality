# def main():
#     print("Hello from assisment-001!")


# if __name__ == "__main__":
#     main()
# main.py



from fastapi import FastAPI, Query
from search_tool import web_search

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Custom Web Search API. Go to /docs to test it."}

@app.get("/search")
def search(query: str = Query(..., description="Enter your search query")):
    result = web_search(query)
    return result

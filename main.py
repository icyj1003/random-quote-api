from fastapi import FastAPI
import random

app = FastAPI()


@app.get("/")
def read_root():
    return "Random quote"

@app.get("/quote")
def get_quote():
    quotes = []

    with open('./Quotes.csv', 'r', encoding='utf8') as f:
        for l in f.readlines(): 
            quote, author, genre = l.strip('\n').split(';')  
            quotes.append({'quote':quote, 'author' : author, "genre": genre})

    quotes = quotes[1:]
    return random.choice(quotes)
    
# uvicorn main:app --reload


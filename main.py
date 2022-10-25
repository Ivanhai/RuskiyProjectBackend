from fastapi import FastAPI
import spacy


nlp = spacy.load("ru_core_news_md")
app = FastAPI()


@app.get("/{sentence}")
async def root(sentence):
    doc = nlp(sentence)
    return doc.to_json()

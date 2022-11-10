from fastapi import FastAPI
import spacy
import uvicorn


nlp = spacy.load("ru_core_news_md")
app = FastAPI()


@app.get("/{sentence}")
async def root(sentence):
    doc = nlp(sentence)
    return doc.to_json()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True, log_level="debug")

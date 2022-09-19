from fastapi import FastAPI
from annotate_stock_news_titles import annotate_text

app = FastAPI()

@app.get("/")
def root(text):
    return {"message": "Hello World"}


@app.get("/gettext/{text}")
def get_text(text):
    return {"message": text}

@app.get("/getannotation/{text}")
def get_text(text):
    tokens = list()
    annotations = annotate_text(text)
    print(annotations)
    poses = annotations['pos']
    for p in range(len(poses)):
        if 'NN' in poses[p]:
            token = annotations["token"][p]
            tokens.append(token)
    return tokens
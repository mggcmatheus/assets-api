from fastapi import FastAPI


app = FastAPI()


@app.router.get('/')
def index():
    return 'Deu certo'

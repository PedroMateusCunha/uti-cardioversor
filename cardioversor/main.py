from fastapi import FastAPI, Request
from cardioversor import Cardioversor

app = FastAPI()
cardioversor = Cardioversor()

cardioversor.get_freq_cardiaca()

@app.get("/")
def read_root():
    return {"message": "Cardioversor"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/status")
def check_status():
    return cardioversor.get_status()

@app.put("/identificador_marca_passo/{identificador_marca_passo}")
def set_identificador_marca_passo(identificador_marca_passo: bool):
    cardioversor.set_identificador_marca_passo(identificador_marca_passo)
    return {"message": "Identificador de marca passo atualizado com sucesso"}

@app.put("/potencia/{potencia}")
def set_potencia(potencia: int):
    cardioversor.set_potencia(potencia)
    return {"message": "Potência atualizada com sucesso"}

@app.put("/frequencia/{frequencia}")
def set_frequencia(frequencia: int):
    cardioversor.set_frequencia(frequencia)
    return {"message": "Frequência atualizada com sucesso"}

@app.put("/ligar")
def ligar():
    return cardioversor.ligar()

@app.put("/desligar")
def desligar():
    cardioversor.desligar()
    return {"message": "Cardioversor desligado"}
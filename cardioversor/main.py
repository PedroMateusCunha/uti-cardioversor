"""
Modulo para inicialização e disponilibilização do serviço
relacionado ao componente cardioversor.
"""
from fastapi import FastAPI
from cardioversor import Cardioversor

app = FastAPI()
cardioversor = Cardioversor()

@app.get("/")
def read_root():
    """Metodo para roteamento inicial do componente"""
    return {"message": "Cardioversor"}

@app.get("/status")
def check_status():
    """Metodo para roteamento para checagem de status do cardioversor"""
    return cardioversor.get_status()

@app.put("/freq_cardiaca/{freq_cardiaca}")
def set_freq_cardiaca(freq_cardiaca: int):
    """Metodo para roteamento para setar a frequencia cardiaca"""
    cardioversor.set_freq_cardiaca(freq_cardiaca)
    return {"message": "Frequência cardíaca atualizada com sucesso"}

@app.put("/identificador_marca_passo/{identificador_marca_passo}")
def set_identificador_marca_passo(identificador_marca_passo: bool):
    """Metodo para roteamento para registrar existencia de marca passo no paciente"""
    cardioversor.set_identificador_marca_passo(identificador_marca_passo)
    return {"message": "Identificador de marca passo atualizado com sucesso"}

@app.put("/potencia/{potencia}")
def set_potencia(potencia: int):
    """Metodo para roteamento para setar a potencia de atuação do cardioversor"""
    cardioversor.set_potencia(potencia)
    return {"message": "Potência atualizada com sucesso"}

@app.put("/frequencia/{frequencia}")
def set_frequencia(frequencia: int):
    """Metodo para roteamento para setar a frequecia de atuação do do cardioversor"""
    cardioversor.set_frequencia(frequencia)
    return {"message": "Frequência atualizada com sucesso"}

@app.put("/ligar")
def ligar():
    """Metodo para roteamento para ligar o cardioversor"""
    return cardioversor.ligar()

@app.put("/desligar")
def desligar():
    """Metodo para roteamento para desligar o cardioversor"""
    cardioversor.desligar()
    return {"message": "Cardioversor desligado"}

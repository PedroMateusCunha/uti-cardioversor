import utils.loadinfo
import requests

environment_vars = utils.loadinfo.environment_vars()


class Cardioversor:
    def __init__(self):
        self.freq_cardiaca = 0
        self.identificador_marca_passo = False
        self.potencia = 10
        self.frequencia = 0
        self.ligado = False

    def get_freq_cardiaca(self):
        response = requests.get(f'{environment_vars["sinais_vitais_container_protocol"]}'
                                f'://{environment_vars["sinais_vitais_container_name"]}'
                                f':{environment_vars["sinais_vitais_container_port"]}'
                                f'/status',
                                timeout=5)
        self.freq_cardiaca = response.json()["sinais_vitais"]["freq_cardiaca"]

    def set_identificador_marca_passo(self, identificador_marca_passo: bool):
        self.identificador_marca_passo = identificador_marca_passo

    def set_potencia(self, potencia: int):
        self.potencia = potencia

    def set_frequencia(self, frequencia: int):
        self.frequencia = frequencia

    def ligar(self):
        if self.identificador_marca_passo == False:
            self.ligado = True
            return {"message": "Cardioversor ligado com sucesso"}
        else:
            return {"aviso": "Marca passo identificado"}

    def desligar(self):
        self.ligado = False

    def get_status(self):
        self.get_freq_cardiaca()
        return {"cardioversor": {
                "freq_cardiaca": self.freq_cardiaca,
                "identificador_marca_passo": self.identificador_marca_passo,
                "potencia": self.potencia,
                "frequencia": self.frequencia,
                "ligado": self.ligado}
                }

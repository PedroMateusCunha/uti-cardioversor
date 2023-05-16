"""Modulo para gerenciamento do cardioversor do leito hospitalar."""
import utils.loadinfo
import requests

environment_vars = utils.loadinfo.environment_vars()


class Cardioversor:
    """
    Classe para gerenciamento do cardioversor do leito hospitalar
    """

    def __init__(self):
        """
        Metodo para inicializar os atributos do cardioversor
        """
        self.freq_cardiaca = 0
        self.identificador_marca_passo = False
        self.potencia = 10
        self.frequencia = 0
        self.ligado = False

    def get_freq_cardiaca(self):
        """
        Metodo para setar o valor da frequencia cardiaca do paciente
        """
        response = requests.get(f'{environment_vars["sinais_vitais_container_protocol"]}'
                                f'://{environment_vars["sinais_vitais_container_name"]}'
                                f':{environment_vars["sinais_vitais_container_port"]}'
                                f'/status',
                                timeout=5)
        self.freq_cardiaca = response.json()["sinais_vitais"]["freq_cardiaca"]

    def set_identificador_marca_passo(self, identificador_marca_passo: bool):
        """
        Metodo para setar a existencia de marcapasso no paciente
        """
        self.identificador_marca_passo = identificador_marca_passo

    def set_potencia(self, potencia: int):
        """
        Metodo para setar a potencia de atuação do cardioversor
        """
        self.potencia = potencia

    def set_frequencia(self, frequencia: int):
        """
        Metodo para setar a frequencia de atuação do cardioversor
        """
        self.frequencia = frequencia

    def ligar(self):
        """
        Metodo para ligar o cardioversor
        """
        if self.identificador_marca_passo is False:
            self.ligado = True
            return {"message": "Cardioversor ligado com sucesso"}

        return {"aviso": "Marca passo identificado"}

    def desligar(self):
        """
        Metodo para desligar o cardioversor
        """
        self.ligado = False


    def get_status(self):
        
        """
        Metodo para recuperar o status do cardioversor
        """
        return {"cardioversor": {
            "freq_cardiaca": self.freq_cardiaca,
                "identificador_marca_passo": self.identificador_marca_passo,
                "potencia": self.potencia,
                "frequencia": self.frequencia,
                "ligado": self.ligado}
                }

from Nomina import Nomina
import Senda

class Cliente(Nomina):
    tag = 0 # Variable de Clase, identificador único!!!

    def __init__(self, client_id: int, edad: int, genero: str, inicial_fpo: int, ingreso: int) -> None:
        salario_minimo = 1000000
        self.nombre = 'N.N'
        self.cedula = client_id
        self.edad = edad
        self.genero = genero
        self.inicial_fpv = inicial_fpo
        self.ingreso = ingreso
        self.mensual = self.ingreso*0.11*salario_minimo
        self.exp_vida = Senda.expectativa_vida(self.genero)
        self.perfil = self.perfilar(edad, genero, perfil=None)
        self.client_id = Cliente.tag
        Cliente.tag += 1

    def __str__(self):
        print(f'< Cliente {self.nombre} de {self.edad}, años y perfil {self.perfil}')

    # Devuelve el perfil de tolerancia al riesgo entre Conservador, moderado y arriesgado
    def perfilar(self, edad, genero, perfil):
        edad_retiro = self.exp_vida - edad

        if((self.mensual > self.mensual * 10 or self.mensual < self.mensual * 3) and edad_retiro > 20):
            perfil = 'Arriesgado'
        
        if((self.mensual > self.mensual * 3 and self.mensual < self.mensual * 10) or (edad_retiro > 10 and edad_retiro < 20)):
            perfil = 'Moderado'
        
        if(edad_retiro < 10):
            perfil = 'Conservador'

        return perfil

    # Devuelve las tasas de retorno reales estimadas para cada perfil
    def get_retorno_obligatorias(self):
        rentabilidades_obligatorias = {'Conservador': 0.03, 'Moderado': 0.04, 'Arriesgado': 0.05}

        return rentabilidades_obligatorias

    # Devuelve el estimativo de mesada para un cliente según su expectativa de vida
    def get_mesada(self):
        pass

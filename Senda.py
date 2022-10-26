def sendaMesadaFee(inicio=100,tasas=[0.03,0.06,0.08],nAcum=100,aporte=1,nDesacum=180,fee=0.02,graficar=True):
    """
    Grafica la senda de acumulación y desacumulación dadas 3 tasas probables y
    un valor inicial y periódico  de aporte
    INPUTS
    inicio: saldo inicial
    tasas: floats, lista con 3 tasas probables de retorno (ret medio +- desviación)
    fee: Comisión efectiva anual 
    nAcum: Meses de acumulación 
    aporte: aporte periódico 
    nDesacum: periodo de desacumulación
    OUTPUTs
    tipo : Figura de matplotlib.pyplot , float
         de rangoMesadaFee acumula los caminos de las 3 tasas 
    """ 
    # Su Codigo Aquí
    #return rangoMesadaFees


#Devuelve la expectativa de vida según género: Hombres->78, Mujeres->82
def expectativa_vida(genero:str) -> int:
    exp_vida = 82

    if genero == 'm':
        exp_vida = 72

    return exp_vida

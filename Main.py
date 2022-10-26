from Cliente import Cliente

def main():
    cliente = Cliente(client_id=1054915321, edad=21, genero='f', inicial_fpo=2, ingreso=3)

    cliente.__str__()

main()
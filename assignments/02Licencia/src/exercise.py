def main():

    edad = int(input("Ingresa tu edad: "))
    
    
    if edad >= 18:
        identi = input("¿Tienes identificación oficial? (s/n): ")
        if  identi == 's'or identi == 'S':
            print("Trámite de licencia concedido")
        elif identi == 'n' or identi == 'N':
            print("No cumples requisitos")
        else:
            print("Respuesta incorrecta")
            
               
    else:
        if edad <= 0:
            print("Respuesta incorrecta")
        else:
            print("No cumples requisitos")

if __name__ == '__main__':
    main()
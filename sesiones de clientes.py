def clasificar_compromiso(duracion, clics):
    if duracion > 180 and clics > 8:
        clasificacion = "Alto"
    elif duracion < 60 or clics < 3:
        clasificacion = "Bajo"
    else:
        clasificacion = "Medio"
    return clasificacion

def generar_informe(matriz_sesiones):
    print("\n===============================================")
    print("         INFORME DE COMPROMISO DE CLIENTES     ")
    print("===============================================")
    print("ID Cliente    Clasificación")
    print("-----------------------------------------------")
    
    for sesion in matriz_sesiones:
        id_cliente = sesion[0]
        duracion = sesion[1]
        clics = sesion[2]
        
        resultado = clasificar_compromiso(duracion, clics)
        
        print(f"{id_cliente:<15}{resultado:<15}")
    
    print("==============================================\n")

def main():
    sesiones = [
        ["C101", 200, 10],
        ["C102", 45, 5],
        ["C103", 120, 2],
        ["C104", 150, 6],
        ["C105", 300, 9],
    ]
    generar_informe(sesiones)
    
if __name__=="__main__":
    main()
      
    

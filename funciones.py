
#x e y son listas.

def obtener_puntos():
    x=[]
    y=[]
    while True:
        punto=input()
        
        if punto.lower() == "e":

            break

        try:
            x_i, y_i = map(float, punto.split(','))
            x.append(x_i)
            y.append(y_i)

        except ValueError:
            print("Entrada inválida. Por favor, ingrese el punto en el formato 'x, y'.")

    
    return x,y 
    



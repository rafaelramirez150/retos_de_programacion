'''
/*
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */
'''
def calcula_area(poligono, dimensiones):
    if poligono == "triangulo":
        base, altura = dimensiones
        area = (base * altura) / 2
        print(f"El área del triángulo es: {area}")
    elif poligono == "cuadrado":
        lado = dimensiones[0]
        area = lado * lado
        print(f"El área del cuadrado es: {area}")
    elif poligono == "rectangulo":
        base, altura = dimensiones
        area = base * altura
        print(f"El área del rectángulo es: {area}")
    else:
        print("Polígono no soportado")
    
calcula_area("triangulo", [3, 4])
calcula_area("cuadrado", [3])
calcula_area("rectangulo", [3, 4])
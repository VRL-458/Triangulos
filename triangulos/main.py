valorA = input("Ingrese el lado A del triangulo")
valorB = input("Ingrese al lado B del triangulo")
valorC = input("Ingrese el lado C del triangulo")

if valorA == valorB:
    if valorB == valorC:
        print("El triangulo es equilatero")
    else:
        print("El tringulo es isosceles")
elif valorB==valorC:
    print("El tringulo es isosceles")
elif valorA == valorC:
    print("el triangulo es isosceles")
else:
    print("El triangulo es escaleno")
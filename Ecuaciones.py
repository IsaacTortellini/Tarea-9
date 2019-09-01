
print("Ecuaciones de segundo grado")
a = int(input("introduce el valor de a: "))
b = int(input("introduce el valor de b: "))
c = int(input("introduce el valor de c: "))
print("La ecuacion es: " + str(a) + "x + " + str(b) +  "x^2 + "  + str(c) +  " = 0 ")
if b**2 > (4*a*c):
    e = 2*a
    d = (b**2 - 4*a*c)**(1/2)
    x1 = (-b + d)/e
    x2 = (-b - d)/e
    print("X1 = " + str(x1))
    print("X2 = " + str(x2))
if b**2 < (4*a*c):
    ei = 2*a
    d = (b**2 - 4*a*c)**(1/2)
    x1 = (-b + d)/e
    x2 = (-b - d)/e
    print("El resultado contiene numeros complejos")
    print("X1 = " + str(x1))
    print("X2 = " + str(x2))





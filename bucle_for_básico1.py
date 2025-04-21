#Juan Diego Medina
#11/04/2025

#1. Básico: imprime todos los números enteros del 0 al 100.
print("1.Básico: números enteros del 0 al 100.")
for i in range(101):
    print(i)

#2. Múltiplos de 2: imprime todos los números múltiplos de 2 entre 2 y 500.
print("\nEjercicio 2: Múltiplos de 2 entre 2 y 500")
for i in range(2, 501, 2):
    print(i)

# 3. Contando Vanilla Ice
print("\nEjercicio 3: Contando Vanilla Ice")
for i in range(1, 101):
    if i % 10 == 0:
        print("baby")
    elif i % 5 == 0:
        print("ice ice")
    else:
        print(i)
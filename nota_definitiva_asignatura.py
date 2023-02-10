# Programa para calcular la nota definitiva de una asignatura en la Espesialidad de sistemas


# input
nc = int(input("Digite el valor de nota cognitiva: "))
np = int(input("Digite el valor de npta procedimental: "))
na = int(input("Digite el valor de nota actitudinal: "))
au = int(input("Digite el valor de autoevaluacion: "))
bi = int(input("Digite el valr de bimestral: "))


# processing
nd = (0.3*nc) + (0.3*np) + (0.1*na) + (0.1*au) + (0.2*bi)


# output
print("La nota definitiva de " + str(nd))
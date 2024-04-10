#programa para conocer si eres de derecha o izquierda

#¿Estás a favor de políticas que promuevan la igualdad social y económica?

#Sí: Suma 1 punto a la izquierda.
#No: Suma 1 punto a la derecha.

#¿Crees en la importancia de la intervención del gobierno para regular la economía y proteger los derechos laborales?

#Sí: Suma 1 punto a la izquierda.
#No: Suma 1 punto a la derecha.
#¿Apoyas la idea de una menor intervención del gobierno en la economía y una mayor libertad individual en los asuntos sociales?

#Sí: Suma 1 punto a la derecha.
#No: Suma 1 punto a la izquierda.
#¿Consideras que las tradiciones culturales y los valores conservadores deben tener un papel importante en la sociedad?

#Sí: Suma 1 punto a la derecha.
#No: Suma 1 punto a la izquierda.

izquierda = 0
derecha = 0

print("¿Estás a favor de políticas que promuevan la igualdad social y económica?")

respuesta1 = input("si / no: ")

print("¿Crees en la importancia de la intervención del gobierno para regular la economía y proteger los derechos laborales?")

respuesta2 = input("si / no: ")

print("¿Apoyas la idea de una menor intervención del gobierno en la economía y una mayor libertad individual en los asuntos sociales?")

respuesta3 = input("si / no: ")

print("¿Consideras que las tradiciones culturales y los valores conservadores deben tener un papel importante en la sociedad?")

respuesta4 = input("si / no: ")

if respuesta1 == "si":
    izquierda += 1
else:
    derecha += 1

if respuesta2 == "si":
    izquierda += 1
else:
    derecha += 1

if respuesta3 == "si":
    derecha += 1
else:
    izquierda += 1   

if respuesta4 == "si":
    derecha += 1
else:
    izquierda += 1   

if izquierda > derecha:
    print("eres de izquierda compañero!")
elif izquierda < derecha:
    print("eres de derecha, eres gente de bien")
else:
    print("no tienes inclinación política, eres tibio")
    













    

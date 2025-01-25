print("*******************")
print("***    BIENVENIDO     ***")
print("** A LA TIENDA DE MASCOTAS **")
print("*******************")

num_perros = 10
num_gatos = 8
num_pajaros = 25

animales_totales = num_perros + num_gatos + num_pajaros

print("Actualmente contamos con:")
print ("perros", num_perros, "gatos", num_gatos, "pajaros", num_pajaros)
print("En total tenemos", animales_totales, 'animales')

#input: para que el usuario ingrese informacion
print ("por favor ingresa tu nombre:")
nombre = (input ())
print ("por favor ingresa tu apellido:")
apellido = (input ())

#concatenacion

nombre_completo = nombre + " " + apellido

print("gracias por visitarnos:", nombre_completo)


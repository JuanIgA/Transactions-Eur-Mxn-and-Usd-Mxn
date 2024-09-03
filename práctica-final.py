#Problemática: La empresa mexicana SuperTech está perdiendo dinero porque en las transacciones desde moneda internacional hay muchos errores del personal al realizar cálculos a mano para pasar de Euro a Peso Mexicano y Dólar a Peso Mexicano en los pagos de importaciones.

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Algoritmo:
#Definir el valor actual del Euro y Dólar respecto al Peso Mex.
#2-Solicitar al usuario tipo de conversión: Euro a Mex o Dólar a Mex)
#3-Solicitar al usuario el monto a convertir.
#4-Realizar la conversión utilizando el tipo de cambio correspondiente.
#5-Mostrar el resultado de la conversión.
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

eur_a_mxn = 23.70
usd_a_mxn = 20.75

tipo_de_conversion = input("Ingrese qué tipo de conversión va a realizar: 1-Euro a Mex o 2-Dólar a Mex. \nSeleccione '1' o '2'. \n-")

if tipo_de_conversion == "1":
    monto = float(input("Ingrese la cantidad de Euros a convertir: \n"))
    conversion = monto * eur_a_mxn
    print(f"La cantidad ingresada fue: {monto} Euros, lo que corresponde a {conversion} Pesos Mexicanos.")
elif tipo_de_conversion == "2":
    monto = float(input("Ingrese la cantidad de Dólares a convertir: \n"))
    conversion = monto * usd_a_mxn
    print(f"La cantidad ingresada fue: {monto} Dólares, lo que corresponde a {conversion} Pesos Mexicanos.")
else: 
    print("La opción ingresada no es válida. Vuelva a intentar.")
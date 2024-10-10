#Librerias
import vendor
#Variables y constantes globales
n1 = 0
n2 = 0
#Funciones
def run():
    #TODO
    #Variables locales
    n1 = int(input("Dame el primer num: "))
    n2 = int(input("Dame el segundo num: "))
    #Siempre que declares una variable hay que INICIALIZARLA
    suma = resta = multiplicacion = division = 0
    suma = n1 + n2
    resta = n1 - n2
    multiplicacion = n1 * n2
    division = n1 / n2 
    print("El resultado de la operacion de: ",n1 ,"+", n2, "es: " ,suma)
    print("El resultado de la operacion de: ",n1 ,"-", n2, "es: " ,resta)
    print("El resultado de la operacion de: ",n1 ,"*", n2, "es: " ,multiplicacion)
    print("El resultado de la operacion de: ",n1 ,"/", n2, "es: " ,division)
    return 


#Codigo principal
# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    

    vendor.launch(run)
    


#Segunda forma de hacerlo, pero con condicional

# num1 = int(input("Introduce el primer numero: "))
# num2 = int(input("Introduce el segundo numero: "))

# operacion = input("Que operacion quieres hacer, suma, resta, division, multiplicacion: ")

# if operacion == "suma":
#     resultado = num1 + num2
#     print("El resultado es: \n" ,num1,"+", num2 ,resultado)
# elif operacion == "resta":
#     resultado = num1 - num2
#     print("El resultado es: \n" ,num1,"-", num2 ,resultado)
# elif operacion == "division":
#     resultado = num1/num2
#     print("El resultado es: \n" ,num1,"/", num2 ,resultado)
# elif operacion == "multiplicacion":
#     resultado = num1*num2
#     print("El resultado de estos dos numeros \n" ,num1,"*", num2 ,"es este: ", resultado)
# else:
#     print("Rarete")

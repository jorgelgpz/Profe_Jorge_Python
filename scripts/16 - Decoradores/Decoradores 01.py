# TEMA: Decoradores

# Funciones que a su vez añaden funcionalidades a otras funciones

######################################################################
def funcionDecoradora(funcionParametro):
    def funcionInterior():
        # Aciones adicionales que decoran
        print("Vamos a realizar un calculo")

        # Funcion Original
        funcionParametro()

        # Aciones adicionales que decoran
        print("Hemos Realizado el calculo\n\n")

    return funcionInterior


######################################################################


######################################################################
@funcionDecoradora
def suma():
    print(15 + 20)


######################################################################


######################################################################
@funcionDecoradora
def resta():
    print(30 - 10)


######################################################################


######################################################################
suma()
resta()

######################################################################

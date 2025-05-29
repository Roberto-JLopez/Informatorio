
# # metodo independiente de la clase
# class Calculadora:
#     @staticmethod                #no me quedo claro, consultar en mentoria 
#     def restar (a,b):
#         return a-b
#     #decorador
#     @staticmethod
#     def sumar (a, b):
#         return a+b


# print(Calculadora.sumar(2, 5))
# print(Calculadora.restar(2, 5))


class Pastel:

    def __init__(self, sabor):
        self.sabor = sabor

    @classmethod
    def chocolate(cls):
        return cls("Chocolate")
    

torta1 = Pastel("Vainilla")
print(torta1.sabor)

torta2 = Pastel("Frutilla")
print(torta2.sabor)

torta3= Pastel.chocolate()
print(torta3.sabor)

print("Clases Version 2 el constructor")

class Perro:
    # funcion constructor
    def __init__(self,color,edad):
        self.color=color
        self.edad=edad
    # funciones creadas por el usuario
    def muerde(self):
        print("chale el perro me mordio")
    def chatperro(self,mensaje):
        print(f"chat perro: {mensaje}")
    def chatperra(self,mensajep):
        print(f"chat perra: {mensajep}")
    def datos(self):
        print(f"color: {self.color} edad: {self.edad}")    
# crear el objeto
chihuas=Perro("Negro",2)
#llamadas a funciones 
chihuas.datos()
chihuas.muerde()
chihuas.chatperro("hola canina")
chihuas.chatperra("hola boby")
chihuas.chatperro("Quieres ser mi tilina? ")
chihuas.chatperra("gruuu.....")
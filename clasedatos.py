class Informacion:
    
    def milista(self):
        lista_Nomperros=["boby","dollar","fany"]
        for x in lista_Nomperros:
            print(x)
    def mitupla(self):
        tuplaraza=("golden","corgi","doberman")
        for tup in tuplaraza:
            print(tup)   
    def miconjunto(self):
        conj_edad={"2","3","6"}
        for con in conj_edad:
            print(con)    
    def midiccionario(self):
        dicci_color={"boby": "beige",
            "dollar": "café",
            "fany": "negro"}
        for di in dicci_color:
            print(dicci_color[di]) 
# creando el objeto

datos=Informacion()
print("listado de nombres de perros")
datos.milista()
print("tupla raza de perros")
datos.mitupla()
print("conjunto edad de perros")
datos.miconjunto()
print("diccionario color de perro")
datos.midiccionario()
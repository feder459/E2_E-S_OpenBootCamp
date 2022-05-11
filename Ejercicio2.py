import pickle
class Vehículo:
    Marca=""
    Modelo=""   
    
    def __init__ (self, Marca, Modelo):
        self.Marca=Marca
        self.Modelo=Modelo
        
    def getMarca(self):
        return self.Marca
    def getModelo(self):
        return self.Modelo
    
instancia=Vehículo("Chevrolet", "Spin")
print("Marca: ",instancia.getMarca()," Modelo: ",instancia.getModelo())
fichero=open('C:/Users/Fede Franco/Documents/CAPACITACIONES 2022/OpenBootcamp/Python/Entrada y Salida/ficheroNuevo.bin','w+b')
pickle.dump(instancia,fichero)



fichero.seek(0)
e=pickle.load(fichero)

print(e)
fichero.close()

import pickle

class Persona:

    def __init__(self, nombre, genero,edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Se ha creado una persona nueva  con el nombre de ", self.nombre)
    
    #Para convertir en cadena de texto la informacion del obj
    def __str_(self):
        return "{} {} {}".format(self.nombre,self.genero,self.edad)

class ListaPersonas:
    personas=[]

    def __init__(self):
        #Creamos info para agregar info bin
        listaDePersonas=open("ficheroExterno","ab+")
        listaDePersonas.seek(0)
        try:
            self.personas=pickle.load(listaDePersonas)
            print("Se cargaron {} personas de momento del  fichero externo".format(len(self.personas)))
        except:
            print("El fichero est[a vac[io")
        finally:
            listaDePersonas.close()
            del(listaDePersonas)
    def agregarPersonas(self,people):
        self.personas.append(people)
        self.GuardarPersonasFicheroExterno()

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)
    def GuardarPersonasFicheroExterno(self):
        #Para poder escribir informacion:
        listaDePersonas=open("ficheroExterno","wb")
        pickle.dump(self.personas,listaDePersonas)
        #Como ya tenemos todo en el archivo no necesitamos lista personas anymore
        listaDePersonas.close()
        del(listaDePersonas)
    def mostrarInfoFicheroExt(self):
        print("Info del fichero externo es: ")
        for p in self.personas:
            print(p)

milista=ListaPersonas()
persona = Persona("Sebastian","Masculono", 22)
milista.agregarPersonas(persona)
milista.mostrarInfoFicheroExt()
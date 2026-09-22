from abc import ABC, abstractmethod


class Habitant(ABC):
    def __init__(self, nom, prenom,age,adresse) :
       self.nom = nom
       self.prenom = prenom
       self.age = age
       self.adresse = adresse
      

    @abstractmethod
    def calcul_nombre_annee_avant_retraite(self): 
        pass
    def __str__(self):
        return self.prenom + " " + self.nom + ", " + str(self.age) + " ans habite a " + self.adresse

# h1 = Habitant("tata",15,"tobn",None) test de linstanciation d'une classe abstraite

class Adulte(Habitant) :
    def __init__(self,nom,prenom,age,adresse) :
        super().__init__(nom,prenom,age,adresse)
        
    def calcul_nombre_annee_avant_retraite(self):
        if(self.age>=62) : 
            raise ValueError("Deja a la retraite")
        return 62-self.age

class Enfant(Habitant) :
    def __init__(self,nom,prenom,age,adresse) :
        super().__init__(nom,prenom,age,adresse)
        
        
        if(self.age>18) :
            raise ValueError("Un enfant doit avoir moins de 18 ans")
            
    def calcul_nombre_annee_avant_retraite(self):
        return "Erreur: un enfant ne peut pas calculer sa retraite"

def affichage(h: Habitant) :
    print (str(h))

adulte = Adulte("Dupont", "Marie", 35, "Rue A")
enfant = Enfant("Martin", "Lucas", 12, "Rue B")
print(adulte)
print(enfant)
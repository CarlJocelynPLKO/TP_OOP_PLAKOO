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


# Adulte : leve une ValueError si age < 18
# calcul_nombre_annee_avant_retraite() renvoie :
# - "Deja a la retraite" si age >= 62
# - 62 - age sinon
# Enfant : leve une ValueError si age >= 18
# calcul_nombre_annee_avant_retraite() renvoie toujours :
# - "Erreur: un enfant ne peut pas calculer sa retraite"
adulte = Adulte("Dupont", "Marie", 35, "Rue A")
enfant = Enfant("Martin", "Lucas", 12, "Rue B")
assert isinstance(adulte, Habitant)
assert adulte.calcul_nombre_annee_avant_retraite() == 27
assert "enfant" in enfant.calcul_nombre_annee_avant_retraite()

try:
    Enfant("Oups", "Martie", 25,"Rue C")
    assert False, "une ValueError aurait du etre levee"
except ValueError:
    pass
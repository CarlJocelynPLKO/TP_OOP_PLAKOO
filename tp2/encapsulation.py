
class Habitant() : 
    def __init__(self, nom, age, adresse, animaux=None) :
        self.__nom = nom
        self.__age = age
        self.__adresse = adresse
        self.__animaux = animaux

    def get_nom(self):
        return self.__nom
    def get_adresse(self) :
        return self.__adresse
    def get_animaux(self) :
        return self.__animaux
    
    def set__nom(self,nom):
        self.__nom = nom
    def set_age(self,age):
        self.__age = age
    def set_adresse(self,adresse):
        self.__adresse = adresse
    def set_animaux(self,animaux):
        self.__animaux = animaux

    @property
    def age(self) :
        return self.__age
    @age.setter
    def age(self,age) :
        if ((age>130)|(age<0)):
            raise ValueError
        self.__age = age

    def affichage_adresse(self,nom,adresse) :    
        print(self.__nom + " habite a"+ self.__adresse)
    
    def compte_animal(self, animal) : 
        for anim in self.__animaux :
            if anim == animal :
                return self.__animaux[animal]
        return 0   
h1 = Habitant("Aldric", 25, "Rue A", {"vaches": 3})

h1.age = 26
assert h1.age == 26
try:
    h1.age = -5
    assert False, "une ValueError aurait du etre levee"
except ValueError:
    pass

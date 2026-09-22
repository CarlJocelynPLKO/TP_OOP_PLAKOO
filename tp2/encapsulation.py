
class Habitant() : 
    def __init__(self, nom, age, adresse, animaux=None) :
        self.__nom = nom
        self.__age = age
        self.__adresse = adresse
        self.__animaux = animaux

    def get_nom(self):
        return self.__nom
    def get_age(self) :
        return self.__age
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

    def affichage_adresse(self,nom,adresse) :    
        print(self.__nom + " habite a"+ self.__adresse)
    
    def compte_animal(self, animal) : 
        for anim in self.__animaux :
            if anim == animal :
                return self.__animaux[animal]
        return 0   
    
                
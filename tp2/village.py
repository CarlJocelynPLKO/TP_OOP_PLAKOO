from encapsulation import*
class Village(): 
    def __init__(self,nom) : 
        self.__nom = nom
        self.__habitant = []
    def get_nom(self) :
        return self.__nom
    def set_nom(self,nom):
        self.__nom = nom 
    def get_habitant(self) :
        return self.__habitant
    def set_habitant(self,habitant):
        self.__habitant = habitant

    def ajouter_habitant_composition(self, nom, age, adresse, animaux=None) :
        hab = Habitant(nom,age,adresse,animaux)
        self.__habitant.append(hab)

    def ajouter_habitant_agregation(self, habitant) : 
        self.__habitant.append(habitant)
    def afficher_habitants(self) :
        for i in range(0,len(self.__habitant)-1) :
            print(self.__habitant[i].nom)


pytown = Village("PyTown")
pytown.ajouter_habitant_composition("Aldric", 25, "Rue A", {"vaches": 3})
elise = Habitant("Elise", 28, "Rue B", {"poules": 10})
pytown.ajouter_habitant_agregation(elise)
autre_village = Village("VillageVoisin")
autre_village.ajouter_habitant_agregation(elise) # meme habitant dans 2 villages

assert len(pytown.get_habitant()) == 2
assert elise in autre_village.get_habitant()

#dans la composition l'objest est creer dans la methode, elle n'existe que dans cet environement alors que dans l'agregation l'objet existe en dehors de la methode
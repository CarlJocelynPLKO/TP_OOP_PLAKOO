"""exo 3"""
releve1 = ("laser_avant", 2.35, "m")
releve2 = ("laser_arriere", 1.10, "m")
releve3 = ("gyroscope", 87.5, "deg")
releves = [releve1, releve2, releve3]

def afficher_releve(a) :
    """
    affiche les infos du capteur
    """
    return "Capteur " + a[0] + " : "+ str(a[1])+ " " + a[2]

assert len(releves) == 3
assert releves[0][0] == "laser_avant"
assert afficher_releve(releve1) == "Capteur laser_avant : 2.35 m"

def recalibrer(releve, capteur, mes ) :
    """
    mofifie la mesure du capteur
    """
    for i in range(0, len(releve)-1) :
        if releve[i][0] == capteur :
            unit = releve[i][2]
            nouv = ( capteur, mes, unit)
            releve[i] = nouv
    return releve

nouveaux_releves = recalibrer(releves, "laser_avant", 2.40)

assert nouveaux_releves[0] == ("laser_avant", 2.40, "m")
assert nouveaux_releves[1] == releve2
assert nouveaux_releves[2] == releve3

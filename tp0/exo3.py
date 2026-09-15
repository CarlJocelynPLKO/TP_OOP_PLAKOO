releve1 = ("laser_avant", 2.35, "m")
releve2 = ("laser_arriere", 1.10, "m")
releve3 = ("gyroscope", 87.5, "deg")
releves = [releve1, releve2, releve3]

def afficher_releve(a) :
  
 

  return "Capteur " + a[0] + " : "+ str(a[1])+ " " + a[2]

assert afficher_releve(releve1) == "Capteur laser_avant : 2.35 m"



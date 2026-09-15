import unittest
from exo3 import*

class TestJournalDeBord(unittest.TestCase):
"""Tests pour les fonctions sur les relevés (tuples)."""

   
    def test_recalibrer_capteur_existant(self) :
        nouv = recalibrer(releves, "laser_avant", 2.40)
        self.assertEqual(nouv[0],("laser_avant", 2.40, "m"))

    def test_recalibrer_capteur_absent(self) :
        nouv = recalibrer(releves, "laser_avant", 2.40)
        self.assertEqual(nouv[0],("laser_avant", 2.40, "m"))
    

if __name__ == "__main__":
    unittest.main(verbosity=2)





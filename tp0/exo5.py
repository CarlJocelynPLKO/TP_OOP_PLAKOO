"""
exo5
"""

pieces_stock = {
"ModeleA": {"moteurs": 10, "capteurs": 25, "roues": 40},
"ModeleB": {"moteurs": 6, "capteurs": 15, "roues": 24},
}

def quantite_piece(stock, modele, piece) :
    """
    retourne nb piece
    """
    return stock[modele][piece]

assert quantite_piece(pieces_stock, "ModeleA", "moteurs") == 10

def consommer_piece(stock, modele, piece, nb) :
    """
    pieces en moins
    """
    stock[modele][piece]-= nb

def ajouter_modele(stock, modele,moteurs, capteurs, roues) :
    """
    nouveau modele
    """
    stock[modele] = {"moteurs": moteurs , "capteurs": capteurs, "roues":   roues}

def total_pieces(stock) :
    """
    total piece
    """
    tot_roues = 0
    tot_capt = 0
    tot_mot = 0
    for modele in stock :
        for piece in stock[modele] :
            if piece == "moteurs" :
                tot_mot += stock[modele][piece]
            if piece == "capteurs" :
                tot_capt += stock[modele][piece]
            if piece == "roues" :
                tot_roues += stock[modele][piece]   
    tot= {"moteurs": tot_mot, "capteurs": tot_capt, "roues": tot_roues}
    return tot

consommer_piece(pieces_stock, "ModeleA", "moteurs", 3)
assert pieces_stock["ModeleA"]["moteurs"] == 7
ajouter_modele(pieces_stock, "ModeleC",moteurs=4, capteurs=10, roues=16)
assert pieces_stock["ModeleC"] == {"moteurs": 4, "capteurs": 10, "roues": 16}
totaux = total_pieces(pieces_stock)
assert totaux == {"moteurs": 17, "capteurs": 50, "roues": 80}

tableau = [0, 5, 8, 9, 15,34, 37,56,62,69]
rech =int(input("entrer la valeur rechercher:"))
debut = 0
fin = len(tableau) - 1
trouve = False
while debut <= fin:
    milieu = (debut + fin) // 2
    if tableau[milieu] == rech:
        print("L'élément ",rech, " est trouvé à l'index ",milieu)
        trouve = True
        break
    elif tableau[milieu] < rech:
        debut = milieu + 1
    else:
        fin = milieu - 1
if not trouve:
    print("L'element ", rech , "n'est pas present dans la liste.")


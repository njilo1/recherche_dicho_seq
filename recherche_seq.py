tableau = [69, 1, 47, 99, 25, 9, 2, 23]
rech =int(input("entrer la valeur rechercher:"))
trouve = False
for index, element in enumerate(tableau):
    if element == rech:
        print("L'élément ",rech," est trouver à l'index ",index)
        trouve = True
        break
if not trouve:
    print("L'element " ,rech , " n'est pas present dans la liste.")

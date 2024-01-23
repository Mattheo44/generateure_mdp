#liam
def dictionnaire():
    langue_choisi = (input("quelles langues voulez vous ?"))

    tous_mots=[]                                         #  Liste défini comme vide
    langue=False                                         #variable booléenne
    while langue==False:                                   # boucle while cette partie du code change la langue en "fr"
        choix=langue_choisi                 #ou "en" si autre langue  on recommence
        if choix=="fr":
            Pages_Francais  =  open("langues/liste_francais.txt","r")        #  ouvrir en lecture seul le fichier et stockée dans Pages "francais
            tous_mots =  Pages_Francais.readlines()                     # Tous les mots sont mis dans Tous Mots
            Pages_Francais.close                                    # on referme le fichier
            langue=True
        elif choix=="en":
            Pages_Anglais = open("langues/words.txt","r")
            tous_mots= Pages_Anglais.readlines()
            Pages_Anglais.close
            langue=True
        elif choix=="deu":
            Pages_allemande = open("langues/deutch.txt","r")
            tous_mots= Pages_allemande.readlines()
            Pages_allemande.close
            langue=True
    dico_lettres  =  {}
    dico_lettres  =  {}                                 # dictionnaire vide


    for Mots in tous_mots:                          # Mots prend chaque mots indépendament
        for letter in range(len(Mots)-1):
                Mots[letter].lower()
                if( ord(Mots[letter]) >=  97         #prend les lettres entre a et z
                and ord(Mots[letter]) <=  122
                and  ord(Mots[letter+1]) >=  97
                and ord(Mots[letter+1]) <=  122):
                    lettre = Mots[letter]               #lettre prend le Mots à l'indice letter
                    lettre_suivante  =  Mots[letter+1]  # lettre prend le Mots à l'indice letter +1
                    if not lettre in dico_lettres:      # si lettre n'est pas une clé de dico
                        dico_lettres[lettre]  = []      #ajouter la clé en tant que liste vide
                    if  lettre_suivante !=  lettre:     #si la lettre suivante est différente à la lettre ...
                        if not  lettre_suivante in dico_lettres[lettre] :   #... et qu'elle n'est pas déja une valeur de la clé ...
                            dico_lettres[lettre].append(lettre_suivante)    #   ...on ajoute la valeur
    return dico_lettres
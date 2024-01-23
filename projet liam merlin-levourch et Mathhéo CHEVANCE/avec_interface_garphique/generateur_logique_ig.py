from random import randint
from prog_dico_interface_graphique import dictionnaire


#matthéo
def generateur_mdp(dico, nb_mots, nb_lettre):         #on prend en entrer le nb de lettre par mot du mdp
  """in : le dictionnaire et le nombre de mot(s) et de lettre(s) du mot géneré
  out : le mot de passe prononcable (voyelle / consonne) aléatoire """

  mot_entier = ""

  for n in range(nb_mots):
      word = ""                     # on crée une chaine de caractère qui sera le mot

      premiere_lettre = chr(randint(97,122))   #première lettre du mots generé aléatoirement avec 8 lettres dans le dico
      while premiere_lettre == chr(104):  #pour ne pas commencer par un h
         premiere_lettre = chr(randint(97,122))

      if premiere_lettre in dico :           #on verifie si la lettre generé entre a et z est une clé du dictionnaire
          word = word + premiere_lettre        #on rajoute la lettre au mot
      else :
          premiere_lettre = chr(randint(97,122)) #sinon on la regénère

      voyelle = ["a", "e", "i", "o", "u", "y"] #liste contenant les voyelles pour plus tard (prononciation)

      for i in range(0,nb_lettre-1):            #boucle avec le nb de lettre demander moins 1 car out of range sinon
            autres_lettres = randint(0,len(dico[premiere_lettre])-1) #choisi un indice au hasard dans la liste de la clé du dico de la lettre précedente

            if word[-1] not in voyelle:                #regarde si la dernière lettre du mot n'est pas une voyelle sois la variable premiere_lettre

                while dico[premiere_lettre][autres_lettres] not in voyelle:
                    autres_lettres = randint(0, len(dico[premiere_lettre]) - 1)
                word += dico[premiere_lettre][autres_lettres] #tant que c'est une consonne on tire une lettre au hasard dans la liste de clé de la dernière lettre du mot puis on l'ajoute au mot
            else:

                while dico[premiere_lettre][autres_lettres] in voyelle: #si la lettre générer est une voyelle
                    autres_lettres = randint(0, len(dico[premiere_lettre]) - 1)
                word += dico[premiere_lettre][autres_lettres] #pareil mais on cherche une consonne pour ne pas avoir deux voyelles d'affilées et donc un mot prononcable
            premiere_lettre = word[-1] #on stock la derniere lettre

      mot_entier +=  word
      if nb_mots - n != 1 :                   #boucle pour enlever le dernier tiret
        mot_entier += "-"         #on rajoute un tiret entre les mots si on est pas au dernier tour

      #explication pour la prononciabilité : -on regarde la dernière lettre du mot si c'est une consonne on rajoute une voyelle generé aléatoirement à partir de la liste du dico
      #                                      -                                     si c'est une voyelle on rajoute une consonne ...
      #                                      -                                     on a donc un enchainement consonne voyelle

  return mot_entier   # enfin la fonction renvoie le mdp




#programme principal


#print(generateur_mdp(dictionnaire("fr"),5 , 8))
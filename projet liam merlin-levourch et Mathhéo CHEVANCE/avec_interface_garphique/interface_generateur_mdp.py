# Créé par MATTHEO.CHEVANCE, le 20/01/2024 en Python 3.7
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from generateur_logique_ig import generateur_mdp
from prog_dico_interface_graphique import dictionnaire

#création de page :

window = Tk()
window.title("Interface generateur de mdp")
window.geometry("1080x550")

label = Label(window, text="Générateur de mot de passe", font = ( "Arial Bold" , 40 ), fg = ("blue") , bg = ("white")) # le titre de l'interface
label.pack()

#saisie utilisateur :
s = Label(window, text="Saisir la langue pour votre mot de passe :", font = ( "Arial Bold" , 20 ), fg = ("black") , bg = ("white")) # le mot de passe générer
s.pack()

saisie = Entry(window, width=30, bg='yellow')
saisie.pack()
saisie.focus()                    #pour  que l'utilisateur soit directement dans la zone de saisie

#crée une liste pour choisir le nb de mots et de lettre du mot de passe
m = Label(window, text="Choisir le nombre de mot de votre mot de passe :", font = ( "Arial Bold" , 20 ), fg = ("black") , bg = ("white")) # le mot de passe générer
m.pack()

liste_mots = Combobox(window)
liste_mots['values']= (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
liste_mots.current(2) #index de l'élément sélectionné (à l'origine
liste_mots.pack()


l = Label(window, text="Choisir le nombre de lettre de votre mot de passe :", font = ( "Arial Bold" , 20 ), fg = ("black") , bg = ("white")) # le mot de passe générer
l.pack()

liste_lettre = Combobox(window)
liste_lettre['values']= (5, 6, 7, 8, 9, 10)
liste_lettre.current(3) #index de l'élément sélectionné
liste_lettre.pack()


mdp = Label(window, text="mot de passe", font = ( "Arial Bold" , 30 ), fg = ("red") , bg = ("white")) # le mot de passe générer
mdp.pack()

langues_possible = ["fr", "en", "deu"]
# récupérer les données saisies et les afficher après le click
def click():
    saisie.focus()
    if saisie.get() not in langues_possible:   #on vérifie que l'utilisateur est bien entrée une langue valide
       messagebox.showinfo('erreur , langue non disponible', 'choisir parmi les langues suivante : fr, en ou deu')
       window .geometry( '300x100' )
    else :
        langue = saisie.get()
        nb_mots = int(liste_mots.get())  #on transforme les elements de la liste en entier
        nb_lettre = int(liste_lettre.get())
        mdp.configure(text = generateur_mdp( dictionnaire(langue) , nb_mots , nb_lettre)) #on change la zone de texte 'mdp' par le mot de passe généré à partir des informations fourni par l'utilisateur





bouton = Button( window , text = "Clickez ici", width = 10 , fg = "blue" , bg = "white" , command = click) # un bouton qui utilise la fonction "click"
bouton.pack()



window.mainloop()
from tkinter import *
import tkinter as tk

root = tk.Tk()
root.withdraw()

windowNames = ["test", "test2"]

def windowManager(screen, args):
    windowNumber = args
    if(windowNames[0] == windowNames[windowNumber]):
        tk.Label(screen, text=f"Fenêtre numéro {windowNumber}").pack(pady=10)
        # implementer le window pour l'addition de sprites

    if(windowNames[1] == windowNames[windowNumber]):
        tk.Label(screen, text=f"Fenêtre numéro {windowNumber}").pack(pady=10)
        # implementer le window pour les parametres et le lancement de la scene
    
    # implementer les windows pour changer de scenes, editer les propriété dun sprite ect...


for i in range(len(windowNames)):
    fenetre = tk.Toplevel(root)
    fenetre.title(windowNames[i])
    windowManager(fenetre, i)

root.mainloop()
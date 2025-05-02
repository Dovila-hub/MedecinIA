import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import datetime

from IA import *

from chatbotv2 import *


def resize_image(image, width, height):
        image = image.resize((width, height))
        return ImageTk.PhotoImage(image)

def show_page_med():  # permet d'aller de la page d'accueil à la page principale médecin
    page_accueil.pack_forget()  # Masquer la première page
    page_principale_medecin.pack()  # Afficher la deuxième page
    
def show_page_patient():  # permet d'aller de la page d'accueil à la page principale patient
    page_accueil.pack_forget()  # Masquer la première page
    page_principale_patient.pack()  # Afficher la deuxième page

def exit_app():
    racine.quit()
    racine.destroy()

def create_account_med():
    page_principale_medecin.pack_forget()  # Masquer la première page
    page_creation_compte.pack()  # Afficher la deuxième page
    
def create_account_patient():
    page_principale_patient.pack_forget()  # Masquer la première page
    page_creation_compte2.pack()  # Afficher la deuxième page

def login_med():
    email = email_entry.get()
    password = password_entry.get()
    fichier = open("fichier_medecin.txt","r")
    print(email, password)
    for ligne in fichier:
        L=ligne.split("=")
        print(L)
        if email==L[0] and password==L[1]:
            page_principale_medecin.pack_forget()  # Masquer la première page
            page_accueil_medecin.pack()  # Afficher la deuxième page
            
    fichier.close()
    #email_entry.delete(0, 'end')
    password_entry.delete(0, 'end')
    
def login_patient():
    email = email_entry9.get()
    password = password_entry9.get()
    fichier = open("fichier_patient.txt","r")
    for ligne in fichier:
        L=ligne.split("=")
        print(L)
        if email==L[0] and password==L[1]:
            page_principale_patient.pack_forget()  # Masquer la première page
            page_accueil_patient.pack()  # Afficher la deuxième page
    fichier.close()

    #email_entry9.delete(0, 'end')
    password_entry9.delete(0, 'end')

    
def verif_creation_med():
    email_entry=email_entry2.get()
    Mdp=password_entry2.get()
    Mdp2=password_entry3.get()
    nom = nom_med_entry.get()
    prenom= prenom_med_entry.get()
    
    a=len(Mdp)
    if str(Mdp)!=str(Mdp2):
        messagebox.showerror("Erreur", 'Vos mots de passe ne se correspondent pas')
        return
         
    if a<=2:
        messagebox.showerror("Erreur", 'Votre mot de passe est trop court')
        return
 
    ch=str(email_entry)+"="+str(Mdp)+"="+str(nom)+"="+str(prenom)+"="

    text1 = open("fichier_medecin.txt","a")
    text1.write(ch)
    text1.write("\n")
    text1.close()
    page_creation_compte.pack_forget()  # Masquer la première page
    page_principale_medecin.pack()  # Afficher la deuxième page
    email_entry2.delete(0, 'end')
    password_entry2.delete(0, 'end')
    password_entry3.delete(0, 'end')
    
def verif_creation_patient():
    email_entry=email_entry8.get()
    Mdp=password_entry8.get()
    Mdp2=password_entry7.get()
    nom = nom_patient_entry.get()
    prenom = prenom_patient_entry.get() 
    a=len(Mdp)
    if str(Mdp)!=str(Mdp2):
        messagebox.showerror("Erreur", 'Vos mots de passe ne se correspondent pas')
        return
         
    if a<=2:
        messagebox.showerror("Erreur", 'Votre mot de passe est trop court')
        return
 
    ch=str(email_entry)+"="+str(Mdp)+"="+str(nom)+"="+str(prenom)+"=0=0=0= ="
    #messagebox.showinfo("Bienvenue(", 'Votre compte est enregistré')
    text1 = open("fichier_patient.txt","a")
    text1.write(ch)
    text1.write("\n")
    text1.close()
    page_creation_compte2.pack_forget()  # Masquer la première page
    page_principale_patient.pack()  # Afficher la deuxième page
    email_entry8.delete(0, 'end')
    password_entry8.delete(0, 'end')
    password_entry7.delete(0, 'end')
    
def retour_accueil_med():
    page_principale_medecin.pack_forget()  # Masquer la première page
    page_accueil.pack()  # Afficher la deuxième page

def retour_principal_med():
    page_accueil_medecin.pack_forget()  # Masquer la première page
    page_principale_medecin.pack()  # Afficher la deuxième page

def retour_accueil_patient():
    page_principale_patient.pack_forget()  # Masquer la première page
    page_accueil.pack()  # Afficher la deuxième page

def retour_principal_patient():
    page_accueil_patient.pack_forget()  # Masquer la première page
    page_principale_patient.pack()  # Afficher la deuxième page
    
def page_mon_medecin():
    page_accueil_patient.forget()
    page_mon_med.pack()
    
def quitter_mes_patients():
    canvas.forget()
    page_accueil_medecin.pack()
    
page_mes_patients_charge = False
    
def page_mes_patients():
    
    global page_mes_patients_charge
    print(page_mes_patients_charge)
    
    #b = page_mes_patients_charge
    
    page_accueil_medecin.forget()
    canvas.pack(anchor="center", fill="both", expand=True)

    for widget in page_mes_patients.winfo_children():
        widget.destroy()
    

    

    page_mes_patients.bind("<Configure>", configure_canvas_scrollregion)
    
   
    if page_mes_patients_charge == False:
        mes_patients_titre = tk.Label(canvas, text="Mes Patients", font=('Courrier', 30), bg="#AFE3DD")
        mes_patients_titre.pack(pady=5, anchor='center', expand=True)

        scrollbar = tk.Scrollbar(canvas, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        canvas.config(yscrollcommand=scrollbar.set)
        page_mes_patients_charge = True



        mail_med = email_entry.get()
    
        nom = ""
        prenom = ""
    
    
        with open("fichier_medecin.txt", 'r') as file:
            lines = file.readlines()
        for line in lines:
            parts = line.strip().split('=')
            if parts[0] == mail_med:
                nom = parts[2]
                prenom = parts[3]
                break
    
        nom_prenom = nom + " " + prenom
    
        with open("fichier_patient.txt", 'r') as file2:
            lines = file2.readlines()
    
        for line in lines:
            parts2 = line.split('=')
            text = str(parts2[2] + " " + parts2[3])
            if parts2[7] == nom_prenom:
                button = tk.Button(canvas, text=text, command=lambda parts=parts2: page_info_patients_pour_med(parts))
                button.pack(pady=5, fill="x", expand=True)
    
        retour = tk.Button(canvas, text="Retour", command=quitter_mes_patients, font=('Courrier', 10), fg="#FFFEFE", bg="#AFE3DD")
        retour.pack(pady=5, expand=False, side="left")
    
    page_mes_patients.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))

    
            


def page_info_patients_pour_med(info):
    
    mail = info[0]
    nom = info[2]
    prenom = info[3]
    age = info[4]
    poids = info[5]
    taille = info[6]
    
    page_info_patient = tk.Toplevel(racine, bg="#AFE3DD")
    page_info_patient.title(str(nom + " " + prenom))
    
    
    
    titre = Label(page_info_patient, text=str(nom + " " + prenom), font=('Courrier', 25), bg="#AFE3DD")
    titre.pack(pady=30)
    
    separator = ttk.Separator(page_info_patient, orient='horizontal')
    separator.pack(fill='x', padx=5, pady=10)

    l1 = Label(page_info_patient, text=mail, font=('Courrier', 20), bg="#AFE3DD")
    l1.pack(pady=5)
    l2 = Label(page_info_patient, text=age + " ans", font=('Courrier', 20), bg="#AFE3DD")
    l2.pack(pady=5)
    l3 = Label(page_info_patient, text=poids + " kg", font=('Courrier', 20), bg="#AFE3DD")
    l3.pack(pady=5) 
    l4 = Label(page_info_patient, text=taille + " cm", font=('Courrier', 20), bg="#AFE3DD")
    l4.pack(pady=5)
    
    separator = ttk.Separator(page_info_patient, orient='horizontal')
    separator.pack(fill='x', padx=5, pady=10)
    
    liste = []
    with open("fichier_synthese.txt", 'r') as file:
        lines = file.readlines()
        
    #on sélectionne les lignes qui correspondent à notre patient
    for line in lines:
        
        parts = line.strip().split('=')
        
        if parts[0] == mail:
            liste.append(line)
            
      
    if len(liste) > 5:
        liste = liste[-3:] #recup que les 3 derniers 
            
    
    for l in liste:
        
        if l != " ":
            
            
            element = l.strip().split('=')
            
            m1 = element[2]
            p1 = element[3]
            m2 = element[4]
            p2 = element[5]
            m3 = element[6]
            p3 = element[7]
            date = element[1]
            symptomes = element[8:]
            symptomes = [e for e in symptomes if e.strip()]
            
            
            txt = f"{','.join(symptomes)}"
       
            labDate = Label(page_info_patient, text=date, font=('Courrier', 20), bg="#AFE3DD")
            labDate.pack(pady=2)
            labm1 = Label(page_info_patient, text=m1 + " :" + p1 + "%", font=('Courrier', 20), bg="#AFE3DD")
            labm1.pack(pady=2)
            labm2 = Label(page_info_patient, text=m2 + " :" + p2 + "%", font=('Courrier', 12), bg="#AFE3DD")
            labm2.pack(pady=2)
            labm3 = Label(page_info_patient, text=m3 + " :" + p3 + "%", font=('Courrier', 9), bg="#AFE3DD")
            labm3.pack(pady=2)
            labSympt = Label(page_info_patient, text=txt, font=('Courrier', 11), bg="#AFE3DF")
            labSympt.pack(pady=15)
            
            separator = ttk.Separator(page_info_patient, orient='horizontal')
            separator.pack(fill='x', padx=5, pady=10)
    
   
   
    

def quitter_page_mon_med():
    page_mon_med.forget()
    
    med = mon_med_label.cget("text")
    
    if med == "Cette adresse mail n'est associée à aucun médecin!":
        med = " "
    
    email_patient = email_entry9.get()

    
    with open("fichier_patient.txt", 'r') as file:
        lines = file.readlines()
        
    updated_lines = []
    
    for line in lines:
        parts = line.strip().split('=')
        mail = parts[0]
        char_sup = ""
        if mail == email_patient:
            parts = [mail, parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], str(med)]
            char_sup ="="
        
        updated_line = '='.join(parts) + char_sup + "\n"
        updated_lines.append(updated_line)
                
    with open("fichier_patient.txt", 'w') as file:
        file.writelines(updated_lines)
    
    
    page_accueil_patient.pack()
    
def page_get_info_patient():
    page_accueil_patient.forget()
    page_informations_patient.pack()
    
    age_entry.delete(0, tk.END)
    age_entry.insert(0, get_info_patient()[0])
    
    poids_entry.delete(0, tk.END)
    poids_entry.insert(0, get_info_patient()[1])
    
    taille_entry.delete(0, tk.END)
    taille_entry.insert(0, get_info_patient()[2])
    
    
def page_mes_dossiers():
    page_accueil_patient.forget()
    
    for widget in page_mes_dossiers.winfo_children():
        widget.destroy()
        
    
    titre_mes_dossiers = Label(page_mes_dossiers, text="Mes dossiers", font=('Courrier', 30), fg="#FFFFFF", bg="#AFE3DD")
    titre_mes_dossiers.pack(pady=0)
    
    separator = ttk.Separator(page_mes_dossiers, orient='horizontal')
    separator.pack(fill='x', padx=5, pady=10)
    
    mail = email_entry9.get()
    
    liste = []
    
    with open("fichier_synthese.txt", 'r') as file:
        lines = file.readlines()
        
    #on sélectionne les lignes qui correspondent à notre patient
    for line in lines:
        
        parts = line.strip().split('=')
        
        if parts[0] == mail:
            liste.append(line)
            
      
    if len(liste) > 5:
        liste = liste[-3:] #recup que les 3 derniers 
            
    
    for l in liste:
        
        if l != " ":
            
            
            element = l.strip().split('=')
            
  
            date = element[1]
            symptomes = element[8:]
            symptomes = [e for e in symptomes if e.strip()]
            
            
            txt = f"{','.join(symptomes)}"
            
   
            labDate = Label(page_mes_dossiers, text=date, font=('Courrier', 20), bg="#AFE3DD")
            labDate.pack(pady=2)
            labSympt = Label(page_mes_dossiers, text=txt, font=('Courrier', 11), bg="#AFE3DF")
            labSympt.pack(pady=15)
            
            separator = ttk.Separator(page_mes_dossiers, orient='horizontal')
            separator.pack(fill='x', padx=5, pady=10)
    
    retour = Button(page_mes_dossiers, text="Retour", command=quitter_mes_dossier, font=('Courrier', 10), fg="#FFFEFE", bg="#AFE3DD")
    retour.pack(pady=30, side="left")  

    page_mes_dossiers.pack()    


def quitter_mes_dossier():
    page_mes_dossiers.forget()
    page_accueil_patient.pack()

def validate_patient_info():
    age = age_entry.get()
    poids = poids_entry.get()
    taille = taille_entry.get()
    
    email_patient = email_entry9.get()

    
    with open("fichier_patient.txt", 'r') as file:
        lines = file.readlines()
        
    updated_lines = []
    
    for line in lines:
        parts = line.strip().split('=')
        mail = parts[0]
        char_sup = ""
        if mail == email_patient:
            parts = [mail, parts[1], parts[2], parts[3], age, poids, taille, parts[7]]
            char_sup ="="
        
        updated_line = '='.join(parts) + char_sup + "\n"
        updated_lines.append(updated_line)
                
    with open("fichier_patient.txt", 'w') as file:
        file.writelines(updated_lines)
        
    page_informations_patient.forget()
    page_accueil_patient.pack()
   
        
    
    
    
    
    
def get_info_patient():
    
    email_patient = email_entry9.get()
    
   
    fichier = open("fichier_patient.txt","r")
    
    age = "0"
    poids = "0"
    taille = "0"
    
    for ligne in fichier:
        L=ligne.split("=")

        if(len(L) >=6):
            if L[0] == email_patient:               
                age = L[4]
                poids = L[5]
                taille = L[6]
        else:
            print("trop petit")
        
    fichier.close()
    return age, poids, taille

def get_list_med():
    
    liste = []

    with open("fichier_medecin.txt", 'r') as file:
        lines = file.readlines()
        
    for line in lines:
        parts = line.strip().split("=")
        
        med = str(parts[2]) + " " + str(parts[3])
        
        liste.append(med)

    return liste

def check_med(event=None):
    with open("fichier_medecin.txt", 'r') as file:
        lines = file.readlines()
        
    for line in lines:
        parts = line.split("=")

        if str(parts[0])== str(email_mon_med_entry.get()):
            mon_med_label.configure(text=str(parts[2]) + " " + str(parts[3]))
            return
        else:
            mon_med_label.configure(text="Cette adresse mail n'est associée à aucun médecin!")


def enregistrer_synthese(mail, m1,p1,m2,p2,m3,p3, symptomes):
    
    p1 = round(p1*100, 2)
    p2 = round(p2*100, 2)
    p3 = round(p3*100, 2)
    
    p1 = str(p1)
    m1 = str(m1)
    
    p2 = str(p2)
    m2 = str(m2)
    
    p3 = str(p3)
    m3 = str(m3)

    # Limiter les symptômes à 5 au maximum
    symptomes = symptomes[:5]
    
    symptomes = [str(symptome) for symptome in symptomes]
    
    # Compléter la liste des symptômes avec des espaces si elle contient moins de 5 éléments
    while len(symptomes) < 5:
        symptomes.append(" ")

    date_actuelle = datetime.datetime.now().strftime("%Y-%m-%d")
    
    ligne = f"{mail}={date_actuelle}={m1}={p1}={m2}={p2}={m3}={p3}={'='.join(symptomes)}=\n"

    # Ouvrir le fichier en mode ajout pour ne pas écraser les données existantes
    with open("fichier_synthese.txt", 'a') as file:
        file.write(ligne)
        
      
        
      
liste_symptomes_synthese = []  
      
      
        
def on_button_click(text):
    
    global liste_symptomes_synthese

    print(liste_symptomes_synthese)
    
    if text == "Généraux":

        update_scrollable_page("Vous avez choisis 'Generaux'. Veuillez maintenant préciser :", ["Fatigue ou faiblesse", "Symptomes liés au poids", "Symptomes liés à la température", "Psychologiques", "Autres"]) 
    
    elif text == "Dermatologiques":
        update_scrollable_page(f"Vous avez choisis '{text}'. Veuillez maintenant préciser :", ["Eruption lesions cutanées", "Symptomes liés à la couleur", "Gonflements / inflammations", "Démangeaisons"])
    
    elif text == "Gastro intestinaux":
        update_scrollable_page(f"Vous avez choisis '{text}'. Veuillez maintenant préciser :", ["Douleurs abdominales", "Symptomes urinaires", "Autres"])
        
    elif text == "Respiratoire":
        update_scrollable_page(f"Vous avez choisis '{text}'. Veuillez maintenant préciser :", ["Nez", "Gorge", "Temperature", "Autre"])
        
    elif text == "Neurologiques ou musculaire":
        update_scrollable_page(f"Vous avez choisis '{text}'. Veuillez maintenant préciser :", ["Douleur musculaire / articulaire", "Perte equilibre", "Problemes sensoriels", "Problemes neurologiques", "Gonflements"])
        
        
    
    elif text == "Fatigue ou faiblesse":
        update_scrollable_page(f"Vous avez choisis '{text}'. Veuillez maintenant préciser :",fatigue_et_faiblesse + ["Retour au debut"])
    elif text == "Symptomes liés au poids":
        update_scrollable_page(f"Vous avez choisis '{text}'. Veuillez maintenant préciser :",symptomes_de_poids + ["Retour au debut"])
    elif text == "Symptomes liés à la température":
        update_scrollable_page(f"Vous avez choisis '{text}'. Veuillez maintenant préciser :",symptomes_de_temperature + ["Retour au debut"])
    elif text == "Psychologiques":
        update_scrollable_page(f"Vous avez choisis '{text}'. Veuillez maintenant préciser :",symptomes_psychologiques + ["Retour au debut"])  
    elif text == "Autres":
        update_scrollable_page(f"Vous avez choisis '{text}'. Veuillez maintenant préciser :",autres_symptomes_generaux + ["Retour au debut"])
        
    elif text == "Eruption lesions cutanées":
        update_scrollable_page(f"Vous avez choisis '{text}'. Veuillez maintenant préciser :",eruptions_lesions_cutanees + ["Retour au debut"])
    elif text == "Symptomes liés à la couleur":
        update_scrollable_page(f"Vous avez choisis '{text}'. Veuillez maintenant préciser :",decoloration_anomalies_cutanees + ["Retour au debut"])
    elif text == "Gonflements / inflammations":
        update_scrollable_page(f"Vous avez choisis '{text}'. Veuillez maintenant préciser :",gonflements_inflammations + ["Retour au debut"])
    elif text == "Démangeaisons":
        update_scrollable_page(f"Vous avez choisis '{text}'. Veuillez maintenant préciser :",irritations_demangeaisons + ["Retour au debut"])
        
    elif text == "Douleurs abdominales":
        update_scrollable_page(f"Vous avez choisis '{text}'. Veuillez maintenant préciser :",douleurs_abdominales_digestives + ["Retour au debut"])
    elif text == "Symptomes urinaires":
        update_scrollable_page(f"Vous avez choisis '{text}'. Veuillez maintenant préciser :",symptomes_urinaires + ["Retour au debut"])
    elif text == "Autres":
        update_scrollable_page(f"Vous avez choisis '{text}'. Veuillez maintenant préciser :",autres_symptomes_gastrointestinaux + ["Retour au debut"])
        
    elif text == "Nez":
        update_scrollable_page(f"Vous avez choisis '{text}'. Veuillez maintenant préciser :",symptomes_nasaux_sinaux + ["Retour au debut"])
    elif text == "Gorge":
        update_scrollable_page(f"Vous avez choisis '{text}'. Veuillez maintenant préciser :",symptomes_gorge + ["Retour au debut"])
    elif text == "Temperature":
        update_scrollable_page(f"Vous avez choisis '{text}'. Veuillez maintenant préciser :",symptomes_respiratoires + ["Retour au debut"])
    elif text == "Autre":
        update_scrollable_page(f"Vous avez choisis '{text}'. Veuillez maintenant préciser :",symptomes_temperature + ["Retour au debut"])
        
    elif text == "Douleur musculaire / articulaire":
        update_scrollable_page(f"Vous avez choisis '{text}'. Veuillez maintenant préciser :",douleurs_musculaires_articulaires + ["Retour au debut"])
    elif text == "Perte equilibre":
        update_scrollable_page(f"Vous avez choisis '{text}'. Veuillez maintenant préciser :",problemes_coordination_equilibre + ["Retour au debut"])
    elif text == "Problemes sensoriels":
        update_scrollable_page(f"Vous avez choisis '{text}'. Veuillez maintenant préciser :",symptomes_sensoriels + ["Retour au debut"])
    elif text == "Problemes neurologiques":
        update_scrollable_page(f"Vous avez choisis '{text}'. Veuillez maintenant préciser :",symptomes_neurologiques + ["Retour au debut"])
    elif text == "Gonflements":
        update_scrollable_page(f"Vous avez choisis '{text}'. Veuillez maintenant préciser :",inflammations_gonflements + ["Retour au debut"])
        
    elif text == "Retour au debut":
        it = ["Généraux", "Dermatologiques", "Gastro intestinaux", "Respiratoire", "Neurologiques ou musculaire", "Terminer ma synthèse", "Quitter"]
        titre = "Nous sommes de retour à la première page. Nous allons essayer de trouver ensemble vos autres symptomes :"
        update_scrollable_page(titre, it)
    elif text == "Quitter":
        scrollable_frame.pack_forget()
        page_accueil_patient.pack()
    elif text == "Terminer ma synthèse":
        make_synthese()
    else:
        liste_symptomes_synthese.append(text)

    
def make_synthese():
    global liste_symptomes_synthese
    
    mail = email_entry9.get()
    
    if len(liste_symptomes_synthese) <3:
        messagebox.showerror("Erreur", f"Vous devez avoir au moins 3 symptomes pour terminer la synthèse (actuellement : {len(liste_symptomes_synthese)})")
        
    else:
        
        
        sympt = [e for e in liste_symptomes_synthese]
        pred_class= SVM(sympt)
        
        m1 = pred_class[0][0]
        p1 = pred_class[0][1]
        
        m2 = pred_class[1][0]
        p2 = pred_class[1][1]
        
        m3 = pred_class[2][0]
        p3 = pred_class[2][1]
        
        
       
        enregistrer_synthese(mail, m1, p1, m2, p2, m3, p3, liste_symptomes_synthese)
        
    
        
def create_scrollable_button_list(root,titre, items):
    # Créer une frame principale
    main_frame = tk.Frame(root, bg="#AFE3DD")
    #main_frame.pack(fill=tk.BOTH, expand=1)
    
    # Ajouter une scrollbar
    canvas = tk.Canvas(main_frame, bg="#AFE3DD")
    scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    
    
    lab = Label(scrollable_frame, text=titre, font=('Courrier', 14), bg="#AFE3DD", wraplength=350)
    lab.pack(pady=5, fill=tk.X)
    
    
    # Ajouter les boutons à la frame scrollable
    for item in items:
        print(item)
        button = tk.Button(scrollable_frame, text=item, command=lambda item=item: on_button_click(item))
        button.pack(pady=5, fill=tk.X)
    
    return main_frame

def show_scrollable_page():
    
    global liste_symptomes_synthese
    liste_symptomes_synthese = []
    page_accueil_patient.pack_forget()
    
    #for widget in root.winfo_children():
    #    widget.pack_forget()
    scrollable_frame.pack(fill=tk.BOTH, expand=1)
    


def update_scrollable_page(titre, new_items):
    
    # Créer une nouvelle frame scrollable avec les nouveaux items
    global scrollable_frame
    # Détruire l'ancienne frame scrollable
    scrollable_frame.pack_forget()
    scrollable_frame.destroy()
    
    scrollable_frame = create_scrollable_button_list(racine, titre, new_items)
    scrollable_frame.pack(fill=tk.BOTH, expand=1)



# Ecran
racine = tk.Tk()
racine.geometry("350x650")
racine.title("MedecinIA")
racine.iconbitmap("logo.ico")
racine.config(background="#AFE3DD")


#------------------------------------------------------------------------------
# Page d'accueil
page_accueil = tk.Frame(racine, bg="#AFE3DD")

titre = Label(page_accueil, text="Connexion", font=('NORMAL', 45), fg="#FFFFFF", bg="#AFE3DD")
titre.grid(row=0, column=0, columnspan=2, pady=80)

# Charger et redimensionner l'image
image = Image.open("logo_medecin.png")
image = resize_image(image, 80, 80)
image_label = tk.Label(page_accueil, image=image, bg="#AFE3DD")
image_label.grid(row=1, column=0, padx=10, pady=10)  # Placer l'image dans la première colonne

# Bouton "Espace médecin"
bouton_medecin = Button(page_accueil, text="Espace médecin", font=('Courrier', 20), bg="#F1A3A3", command=show_page_med)
bouton_medecin.grid(row=1, column=1, padx=10, pady=10)  # Placer le bouton dans la deuxième colonne

image2 = Image.open("icone_groupe.png")
image2 = resize_image(image2, 80, 80)
image_label2 = tk.Label(page_accueil, image=image2, bg="#AFE3DD")
image_label2.grid(row=2, column=0, padx=10, pady=10)  # Placer l'image dans la première colonne

bouton_patient = Button(page_accueil, text="Espace patient", font=('Courrier', 20), bg="#F1A3A3", command=show_page_patient)
bouton_patient.grid(row=2, column=1, columnspan=2, pady=10)

bouton_quitter = Button(page_accueil, text="Quitter", command=exit_app, font='Courrier', bg="#D9D9D9")
bouton_quitter.grid(row=3, column=0, columnspan=2, pady=50)

text1 = Label(page_accueil, text="MedecinIA", font='ITALIC', bg="#AFE3DD")
text1.grid(row=4, column=0, columnspan=2, pady=10)
#------------------------------------------------------------------------------





#------------------------------------------------------------------------------
# Page principale médecin -- Page de login
    
page_principale_medecin = tk.Frame(racine, bg="#AFE3DD")

image3 = Image.open("logo_medecin.png")
image3 = resize_image(image3, 150, 150)
image_label3 = tk.Label(page_principale_medecin, image=image3, bg="#AFE3DD")
image_label3.pack()

titre = Label(page_principale_medecin, text="Espace médecin", font=('Courrier', 30), bg="#AFE3DD")
titre.pack(pady=5)

# Ajouter des champs d'entrée pour l'email et le mot de passe
email_label = Label(page_principale_medecin, text="Email", font=('Courrier', 20), bg="#AFE3DD")
email_label.pack(pady=5)
email_entry = Entry(page_principale_medecin, font=('Courrier', 20))
email_entry.pack(pady=5)

password_label = Label(page_principale_medecin, text="Mot de passe", font=('Courrier', 20), bg="#AFE3DD")
password_label.pack(pady=5)
password_entry = Entry(page_principale_medecin, font=('Courrier', 20), show="*")
password_entry.pack(pady=5)

# Ajouter un bouton pour se connecter
login_button = Button(page_principale_medecin, text="Se connecter", command=login_med, font=('Courrier', 20), bg="#F1A3A3")
login_button.pack(pady=15)
#------------------------------------------------------------------------------





#------------------------------------------------------------------------------
# page creation compte --med
page_creation_compte = tk.Frame(racine, bg="#AFE3DD")

titre = Label(page_creation_compte, text="Entrez vos informations", font=('Courrier', 25), bg="#AFE3DD")
titre.pack(pady=30)

nom_med_label = Label(page_creation_compte, text="Nom", font=('Courrier', 20), bg="#AFE3DD")
nom_med_label.pack(pady=5)
nom_med_entry = Entry(page_creation_compte, font=('Courrier', 20))
nom_med_entry.pack(pady=5)

prenom_med_label = Label(page_creation_compte, text="Prenom", font=('Courrier', 20), bg="#AFE3DD")
prenom_med_label.pack(pady=5)
prenom_med_entry = Entry(page_creation_compte, font=('Courrier', 20))
prenom_med_entry.pack(pady=5)

email_label2 = Label(page_creation_compte, text="Email", font=('Courrier', 20), bg="#AFE3DD")
email_label2.pack(pady=5)
email_entry2 = Entry(page_creation_compte, font=('Courrier', 20))
email_entry2.pack(pady=5)

password_label2 = Label(page_creation_compte, text="Mot de passe", font=('Courrier', 20), bg="#AFE3DD")
password_label2.pack(pady=5)
password_entry2 = Entry(page_creation_compte, font=('Courrier', 20), show="*")
password_entry2.pack(pady=5)

password_label3 = Label(page_creation_compte, text="Confirmer le mot de passe", font=('Courrier', 20), bg="#AFE3DD")
password_label3.pack(pady=5)
password_entry3 = Entry(page_creation_compte, font=('Courrier', 20), show="*")
password_entry3.pack(pady=5)

valider_bouton = Button(page_creation_compte, text="Valider", command=verif_creation_med, font=('Courrier', 20), bg="#F1A3A3")
valider_bouton.pack(pady=10)

# Ajouter un bouton pour créer un compte
create_account_button = Button(page_principale_medecin, text="Créer un compte", command=create_account_med, font=('Courrier', 20), bg="#F1A3A3")
create_account_button.pack(pady=10)

# Bouton retour à la page accueil
bouton_accueil = Button(page_principale_medecin, text="Retour", command=retour_accueil_med, font=('Courrier', 10), fg="#FFFEFE", bg="#AFE3DD")
bouton_accueil.pack(pady=30, side="left")
# Afficher la page d'accueil par défaut
page_accueil.pack(expand=YES)
#------------------------------------------------------------------------------





#------------------------------------------------------------------------------
# page accueil medecin
page_accueil_medecin = tk.Frame(racine, bg="#AFE3DD")

image4 = Image.open("logo_medecin.png")
image4 = resize_image(image4, 250, 250)
image_label4 = tk.Label(page_accueil_medecin, image=image4, bg="#AFE3DD")
image_label4.pack()

titre = Label(page_accueil_medecin, text="Mon espace", font=('Courrier', 30), fg="#FFFFFF", bg="#AFE3DD")
titre.pack(pady=10)

bouton_patients = Button(page_accueil_medecin, command= page_mes_patients, text="Mes patients", font=('Courrier', 20), bg="#F1A3A3")
bouton_patients.pack(pady=90)

bouton_page_principale = Button(page_accueil_medecin, text="Retour", command=retour_principal_med, font=('Courrier', 10), fg="#FFFEFE", bg="#AFE3DD")
bouton_page_principale.pack(pady=30, side="left")
#------------------------------------------------------------------------------






#------------------------------------------------------------------------------
# Page principale patient -- login
page_principale_patient = tk.Frame(racine, bg="#AFE3DD")

image5 = Image.open("icone_groupe.png")
image5 = resize_image(image5, 150, 150)
image_label5 = tk.Label(page_principale_patient, image=image5, bg="#AFE3DD")
image_label5.pack()

titre2 = Label(page_principale_patient, text="Espace patient", font=('Courrier', 30), bg="#AFE3DD")
titre2.pack(pady=5)

# Ajouter des champs d'entrée pour l'email et le mot de passe
email_label9 = Label(page_principale_patient, text="Email", font=('Courrier', 20), bg="#AFE3DD")
email_label9.pack(pady=5)
email_entry9 = Entry(page_principale_patient, font=('Courrier', 20))
email_entry9.pack(pady=5)

password_label9 = Label(page_principale_patient, text="Mot de passe", font=('Courrier', 20), bg="#AFE3DD")
password_label9.pack(pady=5)
password_entry9 = Entry(page_principale_patient, font=('Courrier', 20), show="*")
password_entry9.pack(pady=5)

# Ajouter un bouton pour se connecter
login_button2 = Button(page_principale_patient, text="Se connecter", command=login_patient, font=('Courrier', 20), bg="#F1A3A3")
login_button2.pack(pady=15)
#------------------------------------------------------------------------------








#------------------------------------------------------------------------------
# page creation compte -- patient
page_creation_compte2 = tk.Frame(racine, bg="#AFE3DD")

titre3 = Label(page_creation_compte2, text="Entrez vos informations", font=('Courrier', 25), bg="#AFE3DD")
titre3.pack(pady=30)

nom_patient_label = Label(page_creation_compte2, text="Nom", font=('Courrier', 20), bg="#AFE3DD")
nom_patient_label.pack(pady=5)
nom_patient_entry = Entry(page_creation_compte2, font=('Courrier', 20))
nom_patient_entry.pack(pady=5)

prenom_patient_label = Label(page_creation_compte2, text="Prenom", font=('Courrier', 20), bg="#AFE3DD")
prenom_patient_label.pack(pady=5)
prenom_patient_entry = Entry(page_creation_compte2, font=('Courrier', 20))
prenom_patient_entry.pack(pady=5)

email_label8 = Label(page_creation_compte2, text="Email", font=('Courrier', 20), bg="#AFE3DD")
email_label8.pack(pady=5)
email_entry8 = Entry(page_creation_compte2, font=('Courrier', 20))
email_entry8.pack(pady=5)

password_label8 = Label(page_creation_compte2, text="Mot de passe", font=('Courrier', 20), bg="#AFE3DD")
password_label8.pack(pady=5)
password_entry8 = Entry(page_creation_compte2, font=('Courrier', 20), show="*")
password_entry8.pack(pady=5)

password_label7 = Label(page_creation_compte2, text="Confirmer le mot de passe", font=('Courrier', 20), bg="#AFE3DD")
password_label7.pack(pady=5)
password_entry7 = Entry(page_creation_compte2, font=('Courrier', 20), show="*")
password_entry7.pack(pady=5)

valider_bouton2 = Button(page_creation_compte2, text="Valider", command=verif_creation_patient, font=('Courrier', 20), bg="#F1A3A3")
valider_bouton2.pack(pady=10)

# Ajouter un bouton pour créer un compte
create_account_button2 = Button(page_principale_patient, text="Créer un compte", command=create_account_patient, font=('Courrier', 20), bg="#F1A3A3")
create_account_button2.pack(pady=10)

# Bouton retour à la page accueil
bouton_accueil2 = Button(page_principale_patient, text="Retour", command=retour_accueil_patient, font=('Courrier', 10), fg="#FFFEFE", bg="#AFE3DD")
bouton_accueil2.pack(pady=30, side="left")
#------------------------------------------------------------------------------








#------------------------------------------------------------------------------
# page accueil patient
page_accueil_patient = tk.Frame(racine, bg="#AFE3DD")

image6 = Image.open("icone_groupe.png")
image6 = resize_image(image6, 150, 150)
image_label6 = tk.Label(page_accueil_patient, image=image6, bg="#AFE3DD")
image_label6.pack()

titre9 = Label(page_accueil_patient, text="Mon espace", font=('Courrier', 30), fg="#FFFFFF", bg="#AFE3DD")
titre9.pack(pady=0)

bouton_informations = Button(page_accueil_patient, command=page_get_info_patient, text="Mes informations", font=('Courrier', 20), bg="#F1A3A3")
bouton_informations.pack(pady=10)

bouton_effectuer_synthese = Button(page_accueil_patient, command=show_scrollable_page, text="Effectuer une synthèse", font=('Courrier', 20), bg="#F1A3A3")
bouton_effectuer_synthese.pack(pady=10)

bouton_dossiers = Button(page_accueil_patient, command=page_mes_dossiers, text="Mes dossiers", font=('Courrier', 20), bg="#F1A3A3")
bouton_dossiers.pack(pady=10)

bouton_medecin = Button(page_accueil_patient, command=page_mon_medecin, text="Mon médecin", font=('Courrier', 20), bg="#F1A3A3")
bouton_medecin.pack(pady=10)

bouton_page_principale2 = Button(page_accueil_patient, text="Retour", command=retour_principal_patient, font=('Courrier', 10), fg="#FFFEFE", bg="#AFE3DD")
bouton_page_principale2.pack(pady=30, side="left")
#------------------------------------------------------------------------------





#------------------------------------------------------------------------------
# page mon medecin
page_mon_med = tk.Frame(racine, bg="#AFE3DD")


image4 = Image.open("logo_medecin.png")
image4 = resize_image(image4, 150, 150)
image_label_mon_med = tk.Label(page_mon_med, image=image4, bg="#AFE3DD")
image_label_mon_med.pack()

titre_mon_med = Label(page_mon_med, text="Mon medecin", font=('Courrier', 30), fg="#FFFFFF", bg="#AFE3DD")
titre_mon_med.pack(pady=10)

email_mon_med_label = Label(page_mon_med, text="Email de mon médecin", font=('Courrier', 20), bg="#AFE3DD")
email_mon_med_label.pack(pady=10)
email_mon_med_entry = Entry(page_mon_med, font=('Courrier', 20))
email_mon_med_entry.pack(pady=10)
email_mon_med_entry.bind("<KeyRelease>", check_med)


mon_med_label = Label(page_mon_med, text="Cette adresse mail n'est associée à aucun médecin!")
mon_med_label.pack(pady=10)


valider_mon_med = Button(page_mon_med, text="Valider", command=quitter_page_mon_med, font=('Courrier', 20), bg="#F1A3A3")
valider_mon_med.pack(pady=10)
#------------------------------------------------------------------------------





#------------------------------------------------------------------------------
# Page "Informations patient"
page_informations_patient = tk.Frame(racine, bg="#AFE3DD")


image6 = Image.open("icone_groupe.png")
image6 = resize_image(image6, 200, 200)
image_label6 = tk.Label(page_informations_patient, image=image6, bg="#AFE3DD")
image_label6.pack()

titre3 = Label(page_informations_patient, text="Informations Patient", font=('Courrier', 30), bg="#AFE3DD")
titre3.pack(pady=5)

# Ajouter des champs d'entrée pour l'âge, le poids et la taille
age_label = Label(page_informations_patient, text="Âge", font=('Courrier', 20), bg="#AFE3DD")
age_label.pack(pady=5)
age_entry = Entry(page_informations_patient, font=('Courrier', 20))
age_entry.pack(pady=5)


poids_label = Label(page_informations_patient, text="Poids (kg)", font=('Courrier', 20), bg="#AFE3DD")
poids_label.pack(pady=5)
poids_entry = Entry(page_informations_patient, font=('Courrier', 20))
poids_entry.pack(pady=5)


taille_label = Label(page_informations_patient, text="Taille (cm)", font=('Courrier', 20), bg="#AFE3DD")
taille_label.pack(pady=5)
taille_entry = Entry(page_informations_patient, font=('Courrier', 20))
taille_entry.pack(pady=5)


# Ajouter un bouton pour valider les informations
validate_button = Button(page_informations_patient, text="Valider", command=validate_patient_info, font=('Courrier', 20), bg="#F1A3A3")
validate_button.pack(pady=15)

#------------------------------------------------------------------------------





#------------------------------------------------------------------------------
# Page "Mes Patients"

# Création du canevas
canvas = tk.Canvas(racine, bg="#AFE3DD")


# Création d'un cadre à l'intérieur du canevas
page_mes_patients = tk.Frame(canvas, bg="#AFE3DD")
canvas.create_window((0, 0), window=page_mes_patients, anchor="center")


# Fonction pour ajuster la région de défilement du canevas en fonction de la taille de son contenu
def configure_canvas_scrollregion(event):
    canvas.configure(scrollregion=canvas.bbox("all"))
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
# Page 'Mes Dossiers'
page_mes_dossiers = tk.Frame(racine, bg="#AFE3DD")

#------------------------------------------------------------------------------




#------------------------------------------------------------------------------
#Page Initial Chatbot
items = ["Généraux", "Dermatologiques", "Gastro intestinaux", "RespiratoireAAA", "Neurologiques ou musculaire", "Terminer ma synthèse", "Quitter"]
titre = "Bonjour. Nous allons essayer de trouver ensemble vos symptomes. Quel type de symptomes avez-vous ?"
scrollable_frame = create_scrollable_button_list(racine, titre, items)
scrollable_frame.pack_forget()
#------------------------------------------------------------------------------


print(get_list_med())
# Boucle principale
racine.mainloop()
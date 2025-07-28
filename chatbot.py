import random

class SymptomCheckerChatbot:
    def __init__(self, symptoms):
        self.symptoms = symptoms
        self.patient_symptoms = []
        self.symptom_mapping = {
            'malade': ['frissons', 'tremblements', 'forte_fièvre', 'sueur', 'essoufflement'],
            'fatigué': ['fatigue', 'léthargie', 'perte_d_appétit', 'mains_et_pieds_froids', 'changements_d_humeur'],
            'douleur': ['douleur_articulaire', 'douleur_abdominale', 'maux_de_dos', 'douleur_derrière_les_yeux', 'douleur_thoracique'],
            'anxiété': ['anxiété', 'agitation', 'rythme_cardiaque_rapide', 'dépression', 'irritabilité']
        }

    def start_chat(self):
        print("Bienvenue au chatbot de sélection des symptômes.")
        self.ask_initial_symptoms()
        self.ask_associated_symptoms()
        self.ask_additional_symptoms()
        self.summarize_symptoms()

    def ask_initial_symptoms(self):
        symptoms_input = input("\nVeuillez entrer les symptômes initiaux que vous ressentez en les séparant par des virgules : ").strip().lower()
        entered_symptoms = [symptom.strip().replace(' ', '_') for symptom in symptoms_input.split(',')]
        for symptom in entered_symptoms:
            if symptom in self.symptoms and symptom not in self.patient_symptoms:
                self.patient_symptoms.append(symptom.replace("_", " "))

    def ask_associated_symptoms(self):
        for symptom in self.patient_symptoms.copy():
            print(f"\nAvez-vous des symptômes associés à {symptom} ?")
            self.propose_associated_symptoms(symptom.replace(" ", "_"))

    def propose_associated_symptoms(self, symptom):
        associated_symptoms = random.sample(self.symptoms, 5)  # Proposer aléatoirement 5 symptômes associés
        associated_symptoms.append("Aucun")
        while True:
            print(f"\nQuels symptômes associez-vous à {symptom}?")
            choice = self.ask_question(associated_symptoms)

            if choice == len(associated_symptoms):
                break
            else:
                selected_symptom = associated_symptoms[choice - 1]
                if selected_symptom not in self.patient_symptoms:
                    self.patient_symptoms.append(selected_symptom.replace("_", " "))

    def ask_additional_symptoms(self):
        while True:
            print("\nVoulez-vous ajouter d'autres symptômes ? (oui/non)")
            choice = input().strip().lower()
            if choice == 'oui':
                self.ask_other_symptoms()
            else:
                break

    def ask_other_symptoms(self):
        symptoms_input = input("\nVeuillez entrer les autres symptômes que vous ressentez en les séparant par des virgules : ").strip().lower()
        entered_symptoms = [symptom.strip().replace(' ', '_') for symptom in symptoms_input.split(',')]
        for symptom in entered_symptoms:
            if symptom not in self.patient_symptoms:
                self.patient_symptoms.append(symptom.replace("_", " "))

    def ask_question(self, options):
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        choice = input("Entrez le numéro correspondant à votre choix : ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice)
        else:
            print("Choix invalide. Veuillez réessayer.")
            return self.ask_question(options)

    def summarize_symptoms(self):
        if self.patient_symptoms:
            print("\nMerci pour vos réponses. Vos symptômes sélectionnés sont :")
            for symptom in sorted(self.patient_symptoms):
                print(f"- {symptom}")
            print("Je vais partager cette liste avec votre médecin pour un diagnostic plus précis avant votre rendez-vous.")
        else:
            print("Aucun symptôme sélectionné. Prenez soin de vous !")

symptoms = [
    'démangeaison', 'éruption_cutanée', 'éruptions_cutanees_nodulaires', 'éternuements_continues',
    'frissons', 'tremblements', 'douleur_articulaire', 'douleur_abdominale', 'acidité',
    'ulcères_sur_la_langue', 'fonte_musculaire', 'vomissements', 'brûlures_mictionnelles',
    'miction_avec_spots', 'fatigue', 'prise_de_poids', 'anxiété',
    'mains_et_pieds_froids', 'changements_d_humeur', 'perte_de_poids', 'agitation',
    'léthargie', 'plaques_dans_la_gorge', 'niveau_de_sucre_irregulier', 'toux',
    'forte_fièvre', 'yeux_enfoncés', 'essoufflement', 'sueur', 'déshydratation',
    'indigestion', 'mal_de_tête', 'peau_jaunâtre', 'urine_foncée', 'nausée',
    'perte_d_appétit', 'douleur_derrière_les_yeux', 'douleur_dorsale', 'constipation',
    'douleur_abdominale', 'diarrhée', 'fièvre_légère', 'urine_jaune',
    'jaunissement_des_yeux', 'insuffisance_hépatique_aiguë', 'surcharge_hydrique',
    'gonflement_de_l_estomac', 'ganglions_lymphatiques_enflés', 'malaise',
    'vision_floue_et_déformée', 'flegme', 'irritation_de_la_gorge',
    'rougeur_des_yeux', 'pression_des_sinus', 'nez_coulant', 'congestion', 'douleur_thoracique',
    'faiblesse_des_membres', 'rythme_cardiaque_rapide', 'douleur_pendant_les_mouvements_intestinaux',
    'douleur_dans_la_région_anale', 'sang_dans_les_selles', 'irritation_anale', 'douleur_cervicale',
    'vertiges', 'crampes', 'ecchymoses', 'obésité', 'jambes_gonflées',
    'vaisseaux_sanguins_gonflés', 'visage_et_yeux_puants', 'thyroïde_élargie',
    'ongles_cassants', 'extrémités_gonflées', 'faim_excessive',
    'contacts_extra_conjugaux', 'lèvres_sèches_et_picotantes', 'parole_empâtée',
    'douleur_au_genou', 'douleur_articulaire_de_la_hanche', 'faiblesse_musculaire', 'raideur_du_cou',
    'articulations_enflées', 'raideur_des_mouvements', 'mouvements_tournants',
    'perte_déquilibre', 'instabilité', 'faiblesse_dun_côté_du_corps',
    'perte_de_lodorat', 'inconfort_de_la_vessie', 'mauvaise_odeur_de_lurine',
    'sensation_continuelle_duriner', 'passage_des_gaz', 'démangeaisons_internes',
    'aspect_toxique_(typhos)', 'dépression', 'irritabilité', 'douleur_musculaire',
    'altération_sensorielle', 'taches_rouges_sur_le_corps', 'douleur_au_ventre',
    'menstruations_anormales', 'taches_déchromiques', 'larmoiement_des_yeux',
    'augmentation_de_lappétit', 'polyurie', 'antécédents_familiaux_de_diabète',
    'faim_constante', 'rêves_anormaux', 'troubles_du_sommeil', 'endormissement_au_cours_de_la_journée',
    'itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing',
    'shivering', 'chills', 'joint_pain', 'stomach_pain', 'acidity',
    'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition',
    'spotting_urination', 'fatigue', 'weight_gain', 'anxiety',
    'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness',
    'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough',
    'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration',
    'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea',
    'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain', 'constipation',
    'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine',
    'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload',
    'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise',
    'blurred_and_distorted_vision', 'phlegm', 'throat_irritation',
    'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain',
    'weakness_in_limbs', 'fast_heart_rate', 'pain_during_bowel_movements',
    'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus', 'neck_pain',
    'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs',
    'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid',
    'brittle_nails', 'swollen_extremeties', 'excessive_hunger',
    'extra_marital_contacts', 'drying_and_tingling_lips', 'slurred_speech',
    'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck',
    'swelling_joints', 'movement_stiffness', 'spinning_movements',
    'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side',
    'loss_of_smell', 'bladder_discomfort', 'foul_smell_of_urine',
    'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching',
    'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain',
    'altered_sensorium', 'red_spots_over_body', 'belly_pain',
    'abnormal_menstruation', 'dischromic_patches', 'watering_from_eyes',
    'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum',
    'rusty_sputum', 'lack_of_concentration', 'visual_disturbances',
    'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma',
    'stomach_bleeding', 'distention_of_abdomen',
    'history_of_alcohol_consumption', 'blood_in_sputum',
    'prominent_veins_on_calf', 'palpitations', 'painful_walking',
    'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling',
    'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails',
    'blister', 'red_sore_around_nose', 'yellow_crust_ooze', 'prognosis'
]

chatbot = SymptomCheckerChatbot()
chatbot.start_chat()

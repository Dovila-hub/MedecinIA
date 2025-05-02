import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import f1_score, accuracy_score, confusion_matrix
import seaborn as sns
import sys 



df = pd.read_csv('dataset.csv')
df1 = pd.read_csv('Symptom-severity.csv')





df.isna().sum()
df.isnull().sum()

cols = df.columns
data = df[cols].values.flatten()

s = pd.Series(data)
s = s.str.strip()
s = s.values.reshape(df.shape)

df = pd.DataFrame(s, columns=df.columns)

df = df.fillna(0)



# Liste des symptômes
symptoms = df1['Symptom'].unique()



vals = df.values


for i in range(len(symptoms)):
    vals[vals == symptoms[i]] = df1[df1['Symptom'] == symptoms[i]]['weight'].values[0]
    
d = pd.DataFrame(vals, columns=cols)

d = d.replace('dischromic _patches', 0)
d = d.replace('spotting_ urination',0)
df = d.replace('foul_smell_of urine',0)








(df[cols] == 0).all()

df['Disease'].value_counts()

df['Disease'].unique()

data = df.iloc[:,1:].values
labels = df['Disease'].values





x_train, x_test, y_train, y_test = train_test_split(data, labels, shuffle=True, train_size = 0.85)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

model = SVC(probability=True)
model.fit(x_train, y_train)

preds = model.predict(x_test)


def SVM(psymptoms):

    
    while len(psymptoms) < 5:
        psymptoms.append(0)
        
    a = np.array(df1["Symptom"])
    b = np.array(df1["weight"])
    for j in range(len(psymptoms)):
        for k in range(len(a)):
            if psymptoms[j]==a[k]:
                psymptoms[j]=b[k]

    nulls = [0,0,0,0,0,0,0,0,0,0,0,0]
    psy = [psymptoms + nulls]

    # Utilisation de predict_proba pour obtenir les probabilités de chaque classe
    pred_probs = model.predict_proba(psy)[0]

    # Obtenir les indices des 3 classes avec les probabilités les plus élevées
    top_indices = pred_probs.argsort()[-3:][::-1]

    # Récupérer les noms des classes et leurs probabilités
    top_classes = model.classes_[top_indices]
    top_probs = pred_probs[top_indices]

    # Retourner les 3 maladies avec les probabilités les plus élevées
    return list(zip(top_classes, top_probs))
    
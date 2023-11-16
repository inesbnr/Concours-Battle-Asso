from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

# Charger les données initiales depuis le fichier Excel
data = pd.read_excel("battleasso.xlsx")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    # Lire les données depuis le fichier Excel à chaque demande
    data = pd.read_excel("battleasso.xlsx")

    # Trier les données en fonction du nombre de shots consommés
    sorted_data = data.sort_values(by='Nombre_de_Shots', ascending=False)

    # Ajouter le nom de l'association à la structure de données
    sorted_data['Asso'] = sorted_data['Nom_de_l_Association']

    # Convertir les données triées en dictionnaire
    data_dict = sorted_data.to_dict(orient='records')

    return jsonify(data_dict)

if __name__ == '__main__':
    app.run(debug=True)

import os
from flask import Flask, render_template

# Configuration de Flask pour chercher les templates à la racine ('.')
app = Flask(__name__, template_folder='.')

@app.route('/')
def home():
    # Rendu du fichier HTML situé à la racine
    return render_template('projet.html')

if __name__ == '__main__':
    # Railway attribue dynamiquement un port via la variable d'environnement PORT
    port = int(os.environ.get("PORT", 5000))
    # host='0.0.0.0' est obligatoire pour exposer le serveur sur Railway
    app.run(host='0.0.0.0', port=port)

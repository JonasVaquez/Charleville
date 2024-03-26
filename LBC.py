from flask import Flask, send_file
import os
import random

app = Flask(__name__)

# Dossier contenant les images
IMAGE_DIR = r'C:\Users\perru\Pictures\Screenshots'
images = os.listdir(IMAGE_DIR)

# Page d'accueil
@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
    <title>Accueil</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #fff3e0; /* Un fond orange pâle */
            color: #333;
            margin: 0;
            padding: 20px;
            text-align: center; /* Centre le texte */
        }
        h1 {
            color: #f57c00; /* Orange plus saturé pour les titres */
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            margin: 20px 0;
        }
        a {
            text-decoration: none;
            color: #007bff; /* Bleu pour les liens */
            font-size: 24px;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
    </head>
    <body>
        <h1>Le Bulletin Quotidien de Charleville-Mezières</h1>
        <p>Articles par ordre chronologique</p>
        <ul>
            <li><a href="/26-03-24">26/03/2024</a></li>
            <!-- Ajoutez d'autres pages ici -->
        </ul>
    </body>
    </html>
    """

# Page pour l'image dynamique
@app.route('/26-03-24')
def Mar_26_03_24():
    return """
    <!DOCTYPE html>
    <html>
    <head>
    <title>Bulletin du mardi 26/03/2024</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #fff3e0; /* Même fond orange pâle */
            color: #333;
            margin: 0;
            padding: 20px;
            text-align: center; /* Centre tout le contenu */
        }
        h1 {
            color: #f57c00; /* Orange pour le titre */
        }
        button {
            font-size: 18px;
            margin-top: 20px;
            background-color: #007bff; /* Bleu pour le bouton */
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3; /* Bleu plus foncé au survol */
        }
        img {
            margin-top: 20px;
            max-width: 90%; /* Assure que l'image ne déborde pas de l'écran */
            height: auto; /* Maintient le ratio de l'image */
            border: 1px solid #ddd;
            border-radius: 4px;
            padding: 5px;
        }
    </style>
    </head>
    <body>
        <h1>article du mardi 26 mars 2024</h1>
        <img src="/image" id="dynamicImage" alt="Image Dynamique"/>
        <script>
            function reloadImage() {
                var d = new Date();
                document.getElementById("dynamicImage").src = "/image?" + d.getTime();
            }
        </script>
    </body>
    </html>
    """

# Route pour servir l'image
@app.route('/image')
def image():
    selected_image = random.choice(images)
    return send_file(os.path.join(IMAGE_DIR, selected_image), mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True, port = 5001)

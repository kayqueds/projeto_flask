from flask import Flask

app = Flask(__name__)

from app.views import homePage  # Importação feita depois de criar o app

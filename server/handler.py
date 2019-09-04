# METADATA
__author__ = [
    'Henrique Kops',
    'José Goulart',
    'João Vieira',
    'João Etchichury',
    'Carlo José'
]
__date__ = '2019-08-30'
__version__ = '1.0'

# built-in dependencies
import os

# external dependencies
from flask import (
    Flask, 
    request,
    render_template
)

# project dependencies
from .database import DBconnector

builder = Flask('ServidorDosGuri')
builder.root_path = os\
    .path\
    .dirname(
        os\
        .path\
        .abspath(__file__)
    )


class ServerPort:
    """Componente responsável pelo tratamento de eventos"""

    _HOST = 'localhost'
    _PORT = 8080

    # TEMPLATE RENDERING
    @builder.route("/", methods=['GET'])
    def index_page():
        """Índice do servidor"""

        return render_template('index.html')

    @builder.route("/submit", methods=['GET'])
    def submit_page():
        """Ativação de novo leilão"""

        return render_template('submit.html')

    # DB CONNECTION
    @builder.route("/bet", methods=['POST'])
    def realize_bet():
        """Realiza uma aposta"""

        data = request.form
        log = DBconnector.bet(
            data['product'], 
            data['price']
        )

        return render_template('message.html', **log)

    @builder.route("/create", methods=['POST'])
    def insert_product():
        """Insere um novo produto para que as apostas sejam feitas"""
        
        data = request.form
        log = DBconnector.create(
            data['product'],
            data['price']
        )
        return render_template('message.html', **log)

    @builder.route("/auctions", methods=['GET'])
    def show_auctions():
        """Mostra todos os leilões ativos"""

        return render_template('auctions.html', auctions=DBconnector.show())

    # COMPONENT STARTUP
    def startup(self):
        """Inicia o processamento do servidor"""

        return builder.run(
            host=self._HOST, 
            port=self._PORT,
            debug=True
        )
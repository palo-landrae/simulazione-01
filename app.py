from neo4j import GraphDatabase, basic_auth
from flask_cors import CORS
from flask import Flask, jsonify, request
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

neo4j_driver = GraphDatabase.driver(
        os.getenv('NEO4J_URL'),
        auth=basic_auth(
            os.getenv('NEO4J_USERNAME'),
            os.getenv('NEO4J_PASSWORD')))

def read_query(cypher_query):
    with neo4j_driver.session(database="neo4j") as session:
        results = session.read_transaction(
            lambda tx: tx.run(
                cypher_query,).data())
        neo4j_driver.close()
        return results

@ app.route("/")
def index():
    return "Hello world!"

@ app.route('/api/query1', methods=['GET'])
def getQuery1():
    nome=request.args.get('nome')
    cognome=request.args.get('cognome')

    query=f'''
        MATCH (d:Docente)-[i:IDEATO]-(v:Verifica)
        WHERE d.nome = "{nome}" AND d.cognome = "{cognome}"
        RETURN v.titolo as titolo, v.durata as durata, v.difficoltà as difficolta
        ORDER BY v.titolo ASC
    '''

    return jsonify(list(read_query(query)))

if __name__ == "__main__":
    app.run()

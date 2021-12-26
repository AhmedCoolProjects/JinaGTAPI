from flask import Flask, request
from algos.coloration import Coloration
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "<h1 style='color:red' >Greaaaaaaaaaaaat!</h1>"

@app.route('/coloration', methods=['POST'])
def coloration():
    g = request.get_json("mygraph")["mygraph"]
    colorationObject = Coloration(g)
    return {"response":colorationObject.main()}





'''
@app.route('/dijkstra', methods=['POST'])
@app.route('/bellman', methods=['POST'])
@app.route('/kruskal', methods=['POST'])
'''


if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, request
from functions import coloration2
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "<h1 style='color:red' >Greaaaaaaaaaaaat!</h1>"


@app.route('/coloration', methods=['POST'])
def coloration():
    g = request.get_json("mygraph")
    return {"response":coloration2(g["mygraph"])}

'''
@app.route('/coloration', methods=['POST'])
@app.route('/dijkstra', methods=['POST'])
@app.route('/bellman', methods=['POST'])
@app.route('/kruskal', methods=['POST'])
'''


if __name__ == '__main__':
    app.run()


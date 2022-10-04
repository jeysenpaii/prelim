from flask import Flask, jsonify, request
import json
app = Flask(__name__)

glucose = [
    {
    "glucose_id": 1,
    "date": "October 4, 2022",
    "glucose": "90mg/dl"
    },
    {
    "glucose_id": 2,
    "date": "October 4, 2022",
    "glucose": "80mg/dl"
    }
]

@app.route('/addGlucose', methods = ['POST'])

def addGlucose():
    tmp = request.get_json()
    Glucose.append(tmp)
    return {'id':len(Glucose)}, 200

@app.route('/searchGlucose/<int:index>', methods=['GET'])
def getGlucose(index):
    if index < len(Glucose):
        return jsonify(Glucose[index]), 200
    else:
        return "Glucose ID not found", 404

@app.route('/updateGlucose/<int:index>', methods=['POST'])
def updateGlucose(index):
    tmp = request.get_json()
    Glucose.pop(index)
    Glucose.append(tmp)
    return f"Successfully updated Glucose ID {index}", 200

@app.route('/deleteGlucose/<int:index>', methods=['DELETE'])
def delGlucose(index):
    Glucose.pop(index)
    return "Glucose ID successfully deleted", 200

if __name__ == '__main__':
    app.run(debug=True)

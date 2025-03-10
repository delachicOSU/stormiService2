
from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
dataBase = "users2.json"

#Check if the json file exits, and loads data to the file.
#If it doesnt, then it creates the file
def loadData():
    if os.path.exists(dataBase):
        with open(dataBase, "r") as file:
            return json.load(file)
        
    return {"clients": [], "photoshoots": []}

#writes back to the data file using json.dump
def saveInfo(data):
    with open(dataBase, "w") as file:
        json.dump(data, file, indent=4)

#Defines POST endpoint (/clients)
#Extracts data
@app.route("/clients", methods=["POST"])
def addClient():
    data = loadData()
    newClient = request.json

    #if CANCEL is input, then it will display client was CXL, 400
    if not newClient or newClient.get("name") == "CANCEL":
        return jsonify({"message": "Client Canceled"}), 400

    #201, Success, add client
    data["clients"].append(newClient)
    saveInfo(data)
    return jsonify({"message": "Client added successfully"}), 201

#Add new ps post /phootoshoots, similar to clients
@app.route("/photoshoots", methods=["POST"])
def addPS():
    data = loadData()
    newPS = request.json

    #similar thing here, if user inputs CANCEL, then it cancels
    if not newPS or newPS.get("client") == "CANCEL":
        return jsonify({"message": "Photoshoot was Canceled"}), 400

    #save here
    data["photoshoots"].append(newPS)
    saveInfo(data)
    return jsonify({"message": "Photoshoot scheduled successfully"}), 201

# View all scheduled photoshoots (GET /appts)
@app.route("/appts", methods=["GET"])

def viewAppt():
    data = loadData()
    numAppt = len(data["photoshoots"])
    return jsonify({
        "total appts": numAppt,
        "appointments": data["photoshoots"]
    })

#make sure code runs only when executed DIRECTLY
#True enables  a restart
if __name__ == "__main__":
    app.run(debug=True, port=5000)

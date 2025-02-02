from flask import Flask, jsonify, request
from pymongo.mongo_client import MongoClient
import uuid
import datetime
# from pymongo.server_api import ServerApi # don't know why MongoDB suggest this

uri = "mongodb+srv://admin:<joeSydsam>@clusterwuster.rgsli.mongodb.net/?retryWrites=true&w=majority&appName=ClusterWuster"

app = Flask(__name__)

# Create a new client and connect to the server
client = MongoClient(uri)
db = client.blog
collection = db.post

# health check
@app.route('/health', methods=['GET'])
def health_check():
    """Healthy wealthy"""
    return jsonify({
        'status':'healthy',
        'message':'server runnin'
    }), 200

@app.route('/posts', methods=['POST'])
def post():
    data = request.get_json()
    location = data.get("location")
    rating = data.get("rating")
    title = data.get("title")
    subheading = data.get("subheading")
    author = data.get("author")
    text = data.get("text")
    pictures = data.get("pictures")
    id = uuid.uuid4()
    minute = datetime.datetime.now().minute
    hour = datetime.datetime.now().hour
    date = datetime.datetime.now().day
    month = datetime.datetime.now().month
    year = datetime.datetime.now().year

    postDict = {
        "location":location,
        "rating":rating,
        "title":title,
        "subheading":subheading,
        "author":author,
        "text":text,
        "pictures":pictures,
        "id": id,
        "date":[minute, hour, date,month, year]
    }

    try:
        collection.insert_one(postDict)
    except Exception as e:
        return jsonify({'error':str(e)}), 500

    return jsonify({"message":"added a post successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# # except Exception as e:
#     print(e)
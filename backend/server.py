import os
import mysql.connector
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__) #app have all routes so flask need to know where all routes are so that's why we pass __name__to flask here to detect all routes
print(__name__)
CORS(app) #here for now we allowed every origin to access our api but in real project we do like CORS(app, resources={,,})
mydb = mysql.connector.connect(
    host=os.getenv("Database_host"),
    user=os.getenv("Database_user"),
    password=os.getenv("Database_password"),
    database=os.getenv("Database")
)
mycursor = mydb.cursor()
print("Connected to the database successfully!")
with open("queries.sql", "r", encoding="utf-8") as file: #here we read file queries.sql which we write out side of this file
    sql = file.read() #here file will  automatically close file because with open syntax closes the file after whatever task
print("SQL query read from file successfully!")

mycursor.execute(sql)#here we execute the query which we read from queries.sql file
result = mycursor.fetchall()#here we fetch all the records from the executed query
print("Query executed successfully!")
print("Number of records fetched:", len(result))
print("Sample record:", result)

@app.route("/country-address-count")
def get_country_address_count():
    return jsonify(result)#here it gives same result as we get from mysql query so we can write sql query execution code inside this function but we write it outside of this function because we want to execute query only once when server starts and not every time when user hits the api

if __name__ == "__main__":#it only returns true if the script is run directly and not imported as a module in another script
    app.run(port=3000)
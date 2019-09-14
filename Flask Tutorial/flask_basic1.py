from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


print("OK TIS WORKS")

predicted = [1]

if predicted == [1]:
    result = "bad"
else:
    result = "good"

print(result) 
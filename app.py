from flask import Flask
app = Flask(__name__)
import sample

@app.route('/')
def hello_world():
    return sample.sentence()


if __name__ == "__main__":
    app.run()

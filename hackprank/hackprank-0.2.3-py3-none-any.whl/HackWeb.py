from flask import Flask, render_template

app = Flask(__name__)
def webHack():
    @app.route('/')
    def hackweb():
        return render_template("index.html")

    if __name__ == '__main__':
        app.run(debug=True)




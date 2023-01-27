from flask import Flask
import random

app = Flask(__name__)


@app.route("/")
def hello_world():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


random_number = random.randint(0, 9)
colors = ["red", "brown", "yellow", "orange", "purple"]
print(random_number)


@app.route('/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    if int(subpath) == random_number:
        return f'<h1 style="color: green">That is correct!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    elif int(subpath) < random_number:
        return f'<h1 style="color: {random.choice(colors)}">You are lower!</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    else:
        return f'<h1 style="color: {random.choice(colors)}">You are too high!</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'


if __name__ == "__main__":
    # Run the app in debug mode to auto-reload/debug
    app.run(debug=True)

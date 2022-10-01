from flask import Flask

app = Flask(__name__)

#after create obj import controller - order matters
from controllers import controller


if __name__ == "__main__":
    app.run(debug=True)

#create app obj and invoke run method if this file is main

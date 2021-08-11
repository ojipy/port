from flask import Flask


app = Flask(__name__)
app.config.from_object('flap.config')

from flap.application import view
from flap.application import research
from flap.application import inside
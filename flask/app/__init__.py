from flask import Flask


app = Flask(__name__, static_folder='static')
app.url_map.strict_slashes = False

app.jinja_options = app.jinja_options.copy()
app.jinja_options.update({
    'trim_blocks': True,
    'lstrip_blocks': True
})

app.config['JSON_AS_ASCII'] = False
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = \
    '5f0be0bc90b9160b99991d46fbf7f3e924696932925d043c'

from app import views # noqa


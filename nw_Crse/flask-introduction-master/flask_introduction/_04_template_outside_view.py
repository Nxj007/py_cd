"""Moving the template code to a separate file.

Mixing Python code with HTML is ugly. Templates usually live in their own
location. By default, flask will look up for templates in a 'templates'
directory living in the same path as the application.

"""

from flask import Flask
from flask import render_template  # !Important

app = Flask(__name__)


@app.route('/')
def hello_world():
    library_name = "BHY"
    authors_list = ["Alan Poe", "Jorge L. Borges", "Mark Twain", "Stephen King"]

    rendered_html = render_template(
        'index.html', library_name=library_name, authors=authors_list
        )

    return rendered_html

#!/usr/bin/env python
import flask

# Create the application
APP = flask.Flask(__name__)

@APP.route('/')
@APP.route('/index')
def index():
    """ Displays the index page accesible at '/'  """
    return  flask.render_template('index.html', title = 'Home')

if __name__ == '__main__':
    APP.debug=True
    APP.run()

@APP.route('/hello/<name>/')
def hello(name):
    """ Displays the page greats who ever comes to visit it.
    """
    return flask.render_template('hello.html', name=name, title = 'hello page')
    
@APP.route('/blog')
def blog():
    user = {'nickname':'jhona22baz'}
    post = [
        {
            'author':{'nickname':'Jhona'},
            'body':'Something greatefull happend'
        },
        {
            'author':{'nickname':'Vianey'},
            "body": " I'm so prety and cool "
        }
        ]

    return render_template("blog.html",
        title = 'blog',
        user = user,
        posts = posts)    
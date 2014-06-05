#!/usr/bin/env python
from flask import Flask, render_template,request, flash
from forms import ContactForm
# Create the application
APP = Flask(__name__)

APP.secret_key = 'codeLearningKey'

@APP.route('/')
@APP.route('/index')
def index():
    """ Displays the index page accesible at '/'  """
    return  render_template('index.html', title = 'Home')

@APP.route('/hello/<name>/')
def hello(name):
    """ Displays the page greats who ever comes to visit it.
    """
    return render_template('hello.html', name=name, title = 'hello page')
    
@APP.route('/blog')
def blog():
    user = {'nickname':'jhona22baz'}
    post = [
        {
            'author':{'nickname':'Jhona'},
            'titlepost':'beautiful',
            'body':'Something greatefull happend'
        },
        {
            'author':{'nickname':'Vianey'},
            "titlepost":"It's so Cool",
            "body": " I'm so prety and cool "
        }
        ]

    return render_template("blog.html",
        title = 'blog',
        user = user,
        posts = post)    

@APP.route('/about')
def about():
    return render_template("about.html",title = "about")
    
@APP.route('/contact',methods=['GET','POST'])
def contact():
    """
    The contact method
    """
    form = ContactForm()
    
    if request.method == 'POST':
        form = ContactForm(request.form)
        if form.validate():
            render_template('OK')
        else:
            return render_template('contact.html', title = "contatactame", form=form)
    elif request.method == 'GET':
        return render_template('contact.html',title = 'contactame', form=form)

if __name__ == '__main__':
    APP.debug=True
    APP.run(host='0.0.0.0',debug=True,port=80)
    
#host='0.0.0.0',debug=True,port=80    


from flask import Flask, render_template

app = Flask(__name__)

@app.context_processor
def inject_nav_items():
    #puts the list nav items into each template so there is no need to define it outside the function
    nav_items = [
        {'name': 'Home', 'url': '/'},
        {'name':'Team Members','url':'/team'}
    ]
    return dict(nav_items=nav_items)

@app.route('/')
def home():
    #renders the home.html file. Doing it this way allows to use the base template to only defie the basic stuff once
    return render_template('home.html')

@app.route('/team')
def team():
    return render_template('team.html')

if __name__ == '__main__':
    app.run(debug=True)
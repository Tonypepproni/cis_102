from flask import Flask, render_template

app = Flask(__name__)

@app.context_processor
def inject_nav_items():
    #puts the list nav items into each template so there is no need to define it outside the function
    nav_items = [
        {'name': 'Home', 'url': '/'},
        {'name': 'Sign Up', 'url': '/sign_up'},
        {'name':'Team','url':'/team'},
        {'name':'About us','url':'/about_us'},
        {'name':'e-Mitre','url':'/e-mitre'}
    ]
    return dict(nav_items=nav_items)

@app.route('/')
def home():
    #renders the home.html file. Doing it this way allows to use the base template to only defie the basic stuff once
    return render_template('home.html')

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

@app.route('/socials')
def socials():
    return render_template('socials.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/team/team2024')
def team2024():

    with open('team_names/names2024.txt', 'r') as file: #opens name.txt file in read mode
        file_content=file.read()

    file_content = file_content.replace('\n','<br><br>') #replaces the new line character with the break line html tag

    return render_template('team.html',content=file_content)

if __name__ == '__main__':
    app.run(debug=True)
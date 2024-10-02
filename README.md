"# cis_102" 
Group website for non for profit

To use create a venv
Then create a .gitignore file and add "venv/" to it (dont do it if it already exists)
Then activate the virtual enviorment to install dependencies

    Windows: venv\Scripts\activate

    Unix\MacOs: venv/bin/activate
After activating run "pip install -r requirements.txt" to install deoendencies
After installing run "deactivate"
You should be able to run the python program without venv active


Jinja 

    Home and team extend base.html. This means they will take all attributes in html tags
    and anything in {% block example %}{% endblock %} tags. Things in normal html tags are 
    set in stone and can only be changed in the base.html file. Items in {% block example %}{% endblock %}
    tags can be overwritten if they are called in the child file.

    The {% for blank in blank %}{% endfor %} loops through provided variable name

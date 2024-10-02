"# cis_102" 
Group website for non for profit

to activate virtual enviorment to work in and run any programs run:

Windows: venv\Scripts\activate

Unix\MacOs: venv/bin/activate

Jinja 

    Home and team extend base.html. This means they will take all attributes in html tags
    and anything in {% block example %}{% endblock %} tags. Things in normal html tags are 
    set in stone and can only be changed in the base.html file. Items in {% block example %}{% endblock %}
    tags can be overwritten if they are called in the child file.

    The {% for blank in blank %}{% endfor %} loops through provided variable name
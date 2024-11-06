from flask import Flask, render_template
from flask.views import View
import csv

main=Flask(__name__)

class Basic(View):
    def __init__(self,name,template_name):
        self.name=name
        self.template_name = template_name
        self.nav_items=[
            {'name':'Home','url':'/'},
            {'name':'Teams','url':'/team'},
            {'name':'Sign Up','url':'/signup'},
            {'name':'About Us','url':'/aboutus'},
            {'name':'e-Mitre','url':'/emitre'}
        ]
    
    def dispatch_request(self):
        return render_template(
            self.template_name,
            nav_items=self.nav_items,
            name=self.name
        )

class team(Basic):
    def __init__(self, name, template_name,teams):
        super().__init__(name, template_name)
        self.teams=teams

    def dispatch_request(self):
        return render_template(
            self.template_name,
            nav_items=self.nav_items,
            name=self.name,
            teams=self.teams
        )

templates=[]
teams=[]

with open('static/template.csv', mode='r')as file:
    csvFile = csv.DictReader(file)
    for line in csvFile:
        templates.append(line)

with open('static/teams.csv', mode='r')as file:
    csvFile = csv.DictReader(file)
    for line in csvFile:

        with open(f"static/teamNames/name{line['year']}.csv",mode='r') as nameFile:
            name=list(csv.DictReader(nameFile))

        line.update({
                'url':f'team/{line['name'].lower()}',
                'pic':f'team{line['year']}.jpg',
                'name': name
            })
        teams.append(line)

for temp in templates:
    if temp['type']=='basic':
        main.add_url_rule(temp['route'], view_func = Basic.as_view(temp['name'],temp['name'], temp['tempName']))
    elif temp['type']=='team':
        main.add_url_rule(temp['route'],view_func= team.as_view(temp['name'],temp['name'],temp['tempName'],teams))


if __name__ =='__main__':
    main.run(debug=True)
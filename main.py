from flask import Flask, render_template
from flask.views import View
import csv

main=Flask(__name__)

def name_reader(year):
        with open(f"static/teamNames/name{year}.csv",mode='r') as nameFile:
            name=list(csv.DictReader(nameFile))

        return name

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


class teamyear(team):
    def __init__(self, name, template_name,teams,names):
        super().__init__(name, template_name,teams)
        self.names=names

    def dispatch_request(self):
        return render_template(
            self.template_name,
            nav_items=self.nav_items,
            name=self.name,
            teams=self.teams,
            names=self.names
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
        
        line.update({
            'url':f'team/{line['name'].lower()}',
            'pic':f'team{line['year']}.jpg'
        })

        teams.append(line)

i=0

for temp in templates:
    if temp['type']=='basic':
        main.add_url_rule(temp['route'], view_func = Basic.as_view(temp['name'],temp['name'], temp['tempName']))
    elif temp['type']=='team':
        main.add_url_rule(temp['route'],view_func= team.as_view(temp['name'],temp['name'],temp['tempName'],teams))
    elif temp['type']=='teamyear':
        names=name_reader(teams[i]['year'])

        main.add_url_rule(temp['route'],view_func=teamyear.as_view(temp['name'],temp['name'],temp['tempName'],teams[i],names))
        i+=0 #indexs I whenever a team page is generated

if __name__ =='__main__':
    main.run(debug=True)
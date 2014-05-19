from app import app
from flask import render_template, request, redirect,url_for
from factual import Factual 
import random

KEY = "b8l2aLMVJUhmUE68qxp9QeCtHqjrPokyi2mPamvU"
SECRET = "yT3vk8wIqaFDLu4sYVuEwxV6UwkSm5w7wVETRZmh"

@app.route('/', methods = ['GET', 'POST'])
@app.route('/index')

def index():
	rest = {'name': "Jalapeno Mexican Bar and Grill", 'Phone': '704-555-5555', 'website' : 'www.Jalapeno.com', 'url':"https://www.google.com/maps/embed/v1/place?key=AIzaSyA3Ck-0wERwXyfu-MU7MslIXMEThrYEi7A&q=jalapeno+mexican+grill+DC&zoom=14"}
	
	a = random.randint(1,4)

	if 'shrimp' in request.form:

		if a == 1:
			rest = {'name': "Jalapeno Mexican Bar and Grill", 'Phone': '704-555-5555', 'website' : 'www.Jalapeno.com', 'url':"https://www.google.com/maps/embed/v1/place?key=AIzaSyA3Ck-0wERwXyfu-MU7MslIXMEThrYEi7A&q=jalapeno+mexican+grill+DC&zoom=14"}
		
		elif a == 2:
			rest = {'name': "Crisp and Juicy", 'Phone': '790-233-2332', 'website': 'www.crispandjuicy.com', 'url':"htpps://www.google.com/maps/embed/v1/place?key=AIzaSyA3Ck-0wERwXyfu-MU7MslIXMEThrYEi7A&q=crisp+and+juicy+tenleytown+DC&zoom=14"}
		else:
			rest = {'name': "Masala Art", 'Phone': '202-362-4441', 'website':'www.masalaartdc.com', 'url':"https://www.google.com/maps/embed/v1/place?key=AIzaSyA3Ck-0wERwXyfu-MU7MslIXMEThrYEi7A&q=masala+art+tenleytown+DC&zoom=14"}
		
	elif 'nuts' in request.form:

		if a == 1:
			rest = {'name': "Yo! Sushi", 'Phone':'709-938-3822', 'website': 'www.yosushi.com', 'url':"https://www.google.com/maps/embed/v1/place?key=AIzaSyA3Ck-0wERwXyfu-MU7MslIXMEThrYEi7A&q=yo+sushi+DC&zoom=14"}
		elif a == 2:
			rest = {'name': "Tara Thai", 'Phone':'720-223-2111', 'website': 'www.tarathai.com', 'url':"https://www.google.com/maps/embed/v1/place?key=AIzaSyA3Ck-0wERwXyfu-MU7MslIXMEThrYEi7A&q=tara+thai+DC&zoom=14"}
		else:
			rest = {'name': "Redwood Restaurant and Bar", 'Phone':'202-342-2343', 'website':'www.redwoodbethesda.com', 'url':"https://www.google.com/maps/embed/v1/place?key=AIzaSyA3Ck-0wERwXyfu-MU7MslIXMEThrYEi7A&q=redwood+bethesda&zoom=14"}
	elif 'dairy' in request.form:
		
		if a == 1:
			rest = {'name': "McDonald's", 'Phone':'230-392-3898', 'website': 'www.mcdonalds.com', 'url':"https://www.google.com/maps/embed/v1/place?key=AIzaSyA3Ck-0wERwXyfu-MU7MslIXMEThrYEi7A&q=mcdonalds+tenleytown+DC&zoom=14"}
		elif a == 2:
			est = {'name': "Yo! Sushi", 'Phone':'709-938-3822', 'website': 'www.yosushi.com', 'url':"https://www.google.com/maps/embed/v1/place?key=AIzaSyA3Ck-0wERwXyfu-MU7MslIXMEThrYEi7A&q=yo+sushi+DC&zoom=14"}
		else:
			rest = {'name': "Tara Thai", 'Phone':'720-223-2111', 'website': 'www.tarathai.com', 'url':"https://www.google.com/maps/embed/v1/place?key=AIzaSyA3Ck-0wERwXyfu-MU7MslIXMEThrYEi7A&q=tara+thai+DC&zoom=14"}
	user_enabled = False

	return render_template("index.html", rest = rest)



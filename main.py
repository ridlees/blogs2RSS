#!/bin/python3
from flask import Flask, render_template,request, send_from_directory
from flask import make_response

import os
from os.path import join, dirname

app = Flask(__name__, template_folder=".")

@app.route("/skvrnami-rss")
def skvrnamirss():
    rss_xml = render_template('Unoficial skvrnami RSS-rss.xml')
    response = make_response(rss_xml)
    response.headers['Content-Type'] = 'application/rss+xml'
    return response
    
@app.route("/skvrnami-atom")
def skvrnamiatom():
    atom_xml = render_template('Unoficial skvranmi RSS-atom.xml')
    response = make_response(atom_xml)
    response.headers['Content-Type'] = 'application/atom+xml'
    return response

@app.route("/kasparek-rss")
def kasparekrss():
    rss_xml = render_template('kasparek-rss.xml')
    response = make_response(rss_xml)
    response.headers['Content-Type'] = 'application/rss+xml'
    return response
    
@app.route("/kasparek-atom")
def kasparekatom():
    atom_xml = render_template('kasparek-atom.xml')
    response = make_response(atom_xml)
    response.headers['Content-Type'] = 'application/atom+xml'
    return response

@app.route("/tjarnikova-rss")
def tjarnikovarss():
    rss_xml = render_template('Unoficial tjarnikova RSS-rss.xml')
    response = make_response(rss_xml)
    response.headers['Content-Type'] = 'application/rss+xml'
    return response
    
@app.route("/tjarnikova-atom")
def tjarnikovaatom():
    atom_xml = render_template('Unoficial tjarnikova RSS-atom.xml')
    response = make_response(atom_xml)
    response.headers['Content-Type'] = 'application/atom+xml'
    return response

@app.route("/kocourovo-rss")
def kocourovorss():
    atom_xml = render_template('Unoficial kocourovo RSS-rss.xml')
    response = make_response(atom_xml)
    response.headers['Content-Type'] = 'application/rss+xml'
    return response

@app.route("/kocourovo-atom")
def kocourovoatom():
    atom_xml = render_template('Unoficial kocourovo RSS-atom.xml')
    response = make_response(atom_xml)
    response.headers['Content-Type'] = 'application/atom+xml'
    return response

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/")
def index():
    return render_template("index.html")


'''
Created on 2017年6月28日

@author: Administrator
'''
from flask import Flask
app = Flask(__name__)

@app.route('/projects')
@app.route('/projects/<name>')
def projects(name=None):
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

if(__name__ == '__main__'):
    app.run(debug=True)
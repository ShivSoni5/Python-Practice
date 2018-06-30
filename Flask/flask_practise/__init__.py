#!/usr/bin/python3

from flask import Flask, render_template, request
from subprocess import getoutput as run

app = Flask(__name__)

"""
page =  '''
        <h1> Hello World!</h1>
        <h1> WebDev with Flask </h1>
        '''
"""

@app.route('/', methods=['GET','POST'])
def first_page():
    if request.method == 'GET':
        return render_template('main.html')
    else:
        return 'POST method is not allowed babe\n' # curl -X POST http://0.0.0.0:80
#    return page


# @app.route('/cmd')
@app.route('/cmd/<x>', methods = ['GET','POST'])
def command(x):
    output = run(x)
    return (f'<h1> {output} </h1>\n')

if __name__ == '__main__':
#    app.run()
#    app.run('192.168.1.7')
#    app.run('0.0.0.0')
    app.run(host='0.0.0.0', port='80')

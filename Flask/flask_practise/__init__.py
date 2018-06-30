#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

page =  '''
        <h1> Hello World!</h1>
        <h1> WebDev with Flask </h1>
        '''

@app.route('/test')
def first_page():
    return page

@app.route('/')
def link():
    return '<h1><a href="www.google.com">google</a></h1>'  # will search www.google.com inside '/'

if __name__ == '__main__':
#    app.run()
#    app.run('192.168.1.7')
#    app.run('0.0.0.0')
    app.run(host='0.0.0.0', port='80')

#!/usr/bin/env python

import bottle

@bottle.route('/')
def name_page():
    return "Hello world!\n"

bottle.debug(True)
bottle.run(host='localhost', port=8080)

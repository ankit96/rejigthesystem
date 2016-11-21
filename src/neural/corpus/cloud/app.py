__author__ = 'ankit'

import os
from flask import Flask,request, redirect, Response
from final import main





app = Flask(__name__)


@app.route('/tweet', methods=['post'])
def rejig():

    #text = request.values.get('text')
    text = "Indian Defence"
    data = main(str(text))
    print data
    #return Response(str(data),content_type="text/plain; charset=utf-8" )
    
#rejig()

@app.route('/')
def hello():
    return redirect('https://github.com/ankit96/moodler')

if __name__ == '__main__':
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0', port=port)


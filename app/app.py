from ast import Or
from flask import Flask, render_template_string, render_template, send_file, abort
import os
from collections import OrderedDict

app = Flask(__name__)

BASE_DIR = '/usr/src/app/web_hw_files'

# root webpage
'''
@app.route('/', defaults={'req_path': ''})
@app.route('/<path:req_path>')
def root(req_path):
    # Joining the base and the requested path
    print("Start of function")
    abs_path = os.path.join(BASE_DIR, req_path)

    # Return 404 if path doesn't exist
    if not os.path.exists(abs_path):
        print("Can't find path")
        return abort(404)

    # Check if path is a file and serve
    if os.path.isfile(abs_path):
        return downloadFile(abs_path)

    # Show directory contents
    print("abs_path: " + abs_path)
    files = os.listdir(abs_path)
    isFile = []
    for file in files:
        print(os.path.join(abs_path, file))
        print(os.path.isfile(os.path.join(abs_path, file)))
        isFile.append(os.path.isfile(os.path.join(abs_path, file)))
    print("Try to render html")

    return render_template('index.html', zipFiles=zip(files, isFile))
'''

@app.route('/')
def root():
    html = directoryTree(BASE_DIR=BASE_DIR)

    return render_template('index.html', htmlTree=html)

def directoryTree(BASE_DIR):
    html = '<div id="myDIV">'
    currLevel = 0
    for root, dirs, files in os.walk(BASE_DIR, topdown=True):
        level = root.replace(BASE_DIR, '').count(os.sep)
        if level > currLevel:
            currLevel = level
            html += '<div id="myDIV">'
        elif level < currLevel:
            while level < currLevel:
                html += '</div>'
                currLevel -= 1
        indent = '&nbsp;' * 4 * level
        if len(files) == 0:
            html += '<div id="myDIV">' + '{}{}'.format(indent, os.path.basename(root)) + '</div>'
        else:
            html += '{}{}'.format(indent, os.path.basename(root))
            subindent = '&nbsp;' * 4 * (level + 1)
            for f in files:
                html += '<p>' + '{}{}'.format(subindent, f) 
                html += '<a href="/download/{{{{ root }}}}"> Download </a>'
                html += '</p>'

    if level < currLevel:
        while level < currLevel:
            html += '</div>'
            currLevel -= 1
    return html

def previewFile():
    pass

@app.route('/download', defaults={'req_path': ''}, methods=['GET', 'POST'])
@app.route('/download/<path:req_path>', methods=['GET', 'POST'])
def downloadFile(abs_path):  
    return send_file(abs_path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
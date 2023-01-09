from ast import Or
from flask import Flask, render_template_string, render_template, send_file, abort
import os
from collections import OrderedDict

app = Flask(__name__)

BASE_DIR = '/usr/src/app/web_hw_files'

# root webpage
@app.route('/')
def root():
    html = directoryTree(BASE_DIR=BASE_DIR)

    return render_template('index.html', htmlTree=html)

def directoryTree(BASE_DIR):
    html = '<div id="hierarchy">'
    currLevel = 0
    for root, dirs, files in os.walk(BASE_DIR, topdown=True):
        html += '<div class="foldercontainer">' 

        level = root.replace(BASE_DIR, '').count(os.sep)
        if level > currLevel:
            currLevel = level
        elif level < currLevel:
            while level < currLevel:
                html += '</div>'
                currLevel -= 1
   
        if len(files) == 0 and len(dirs) == 0:
            html += '<span class="folder fa-folder">{}</span>'.format(os.path.basename(root))
            html += '<span class="noitems">No Items</span>'
            html += '</div>'
        else:
            html += '<span class="folder fa-folder-o" data-isexpanded="true">{}</span>'.format(os.path.basename(root))
            for f in files:
                html += '<span class="file">{}'.format(f) 
                html += '<a href="/download/{}/{}"> Download </a>'.format(root, f)
                html += '</span>'
            if len(dirs) == 0:
                html += '</div>'

    if level < currLevel:
        while level < currLevel:
            html += '</div>'
            currLevel -= 1
    html += '</div>'
    return html

def previewFile():
    pass

@app.route('/download', defaults={'req_path': ''}, methods=['GET', 'POST'])
@app.route('/download/<path:req_path>', methods=['GET', 'POST'])
def downloadFile(req_path):  
    return send_file('/' + req_path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
from flask import Flask, render_template, send_file
import os

app = Flask(__name__)

# Path to volume containing database files
BASE_DIR = '/usr/src/app/web_hw_files'

# Root webpage
@app.route('/')
def root():
    html = directoryTree(BASE_DIR=BASE_DIR)

    return render_template('index.html', htmlTree=html)

# Creates the HTML showing the directory tree
def directoryTree(BASE_DIR):
    # The below div will used for displaying the preview of a text file
    html = '<div id="iframe", style="border:1px solid black"></div>'

    # The rest of the code below will generate the HTML for the directory tree
    html += '<div id="hierarchy">'
    currLevel = 0
    for root, dirs, files in os.walk(BASE_DIR, topdown=True):
        html += '<div class="foldercontainer">' 

        level = root.replace(BASE_DIR, '').count(os.sep)
        if level > currLevel:
            currLevel = level
        # Creates div end tags for leftover div
        elif level < currLevel:
            while level < currLevel:
                html += '</div>'
                currLevel -= 1

        # For a directory with no files or deeper folders
        if len(files) == 0 and len(dirs) == 0:
            html += '<span class="folder fa-folder">{}</span>'.format(os.path.basename(root))
            html += '<span class="noitems">No Items</span>'
            html += '</div>'
        # For a directory with files and/or deeper folders
        else:
            html += '<span class="folder fa-folder-o" data-isexpanded="true">{}</span>'.format(os.path.basename(root))
            for f in files:
                html += '<span class="file" id="/{}/{}">{}'.format(root, f, f) 
                html += '<a href="/download/{}/{}"> Download </a>'.format(root, f)
                html += '</span>'
            if len(dirs) == 0:
                html += '</div>'

    # Creates div end tags for leftover div
    if level < currLevel:
        while level < currLevel:
            html += '</div>'
            currLevel -= 1
    html += '</div>'
    return html

@app.route('/preview', defaults={'req_path': ''}, methods=['GET', 'POST'])
@app.route('/preview/<path:req_path>', methods=['GET', 'POST'])
def previewFile():
    pass

# Download file from req_path
@app.route('/download', defaults={'req_path': ''}, methods=['GET', 'POST'])
@app.route('/download/<path:req_path>', methods=['GET', 'POST'])
def downloadFile(req_path):  
    return send_file('/' + req_path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
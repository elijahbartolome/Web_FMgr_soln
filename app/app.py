from flask import Flask, render_template_string, render_template, send_file, abort
import os
app = Flask(__name__)

BASE_DIR = '/usr/src/app/web_hw_files'

# root webpage
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
        return send_file(abs_path)

    # Show directory contents
    files = os.listdir(abs_path)
    print("Try to render html")

    return render_template('index.html', files=files)

def directoryTree():
    pass
def previewFile():
    pass
def downloadFile():    
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
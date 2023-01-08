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

def directoryTree():
    pass
def previewFile():
    pass

@app.route('/download', defaults={'req_path': ''}, methods=['GET', 'POST'])
@app.route('/download/<path:req_path>', methods=['GET', 'POST'])
def downloadFile(abs_path):  
    return send_file(abs_path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
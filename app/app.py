from flask import Flask, render_template_string

app = Flask(__name__)

directory = '/var/lib/mysql/'

# root webpage
@app.route('/')
def root():
    return render_template_string('''''')

def directoryTree():
    pass
def previewFile():
    pass
def downloadFile():    
    pass

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
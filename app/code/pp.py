import os
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename
import pacparser as pp


UPLOAD_FOLDER = './uploads/'
ALLOWED_EXTENSIONS = set(['txt', 'pac'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def proxy_test(pac_string, myip, url):
    pp.init()
    if myip:
        pp.setmyip(myip)
    if not url:
        url = 'http://www.google.com'
    pp._pacparser.parse_pac_string(pac_string)
    proxy = pp.find_proxy(url)
    return proxy


@app.route('/api/')
def index(pacfile=None):

    myip = request.args.get('myip', '')
    url = request.args.get('url', 'http://www.google.com')

    pp.init()
    pp.setmyip(myip)
    pp.parse_pac('test.pac')
    proxy = pp.find_proxy(url)

    return proxy


@app.route('/api/upload/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
	    file = request.files['file']
	    if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		#return redirect(url_for('index', pacfile=filename))
		return filename
    return "UPLOAD PAGE"

@app.route('/api/uploadpac/', methods=['GET', 'POST'])
def uploadpac():
    if request.method == 'POST':
        print request.form['pac_string']
        print request.form['myip']
        print request.form['test_url']

        pac_string = request.form['pac_string']
        myip =  request.form['myip']
        test_url = request.form['test_url']
        proxy = proxy_test(pac_string, myip, test_url)
        print proxy
    return "UPLOAD PAGE"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

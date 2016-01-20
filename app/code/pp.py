from flask import Flask
from flask import request

import pacparser as pp


app = Flask(__name__)


@app.route('/api/')
def index():
    myip = request.args.get('myip', '')
    url = request.args.get('url', 'http://www.google.com')

    pp.init()
    pp.setmyip(myip)
    pp.parse_pac('test.pac')
    proxy = pp.find_proxy(url)

    return proxy


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

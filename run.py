import os
from gevent.pywsgi import WSGIServer

from app import app

if __name__ == "__main__":
    if os.environ.get("PRODUCTION") == "True":
        http_server = WSGIServer(("", 8080), app)
        http_server.serve_forever()
    else:
        app.run(host="0.0.0.0", port=8080, debug=True)
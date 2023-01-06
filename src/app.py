import os
import json
from setting import create_app, request
from dotenv import load_dotenv


load_dotenv()
PORT = int(os.environ.get('PORT', 5000))
app = create_app()


@app.route('/')
def test():
    return {"group": "LATFinders"}


if __name__ == '__main__':
    app.run(threaded=True, host=('0.0.0.0'), port=PORT)
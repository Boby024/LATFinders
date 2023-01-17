from setting import jsonify, make_response

def setRep(data, type="l", code=200):
    headers = {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*"
    }

    if type == "m":
        resp = make_response(jsonify(data), code, headers)
    elif type == "o":
        resp = make_response(jsonify(data), code, headers)
    elif type == "f":
        resp = make_response(data, code, headers)

    return resp
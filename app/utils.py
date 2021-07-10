from flask import jsonify
def bad_request(message = "Invalid request."):
    return jsonify(status=False, message=str(message)), 400
    
def response(data = None, status = True):
    return jsonify(status=status, data = data)

def not_found(message = "Not found."):
    return jsonify(status="fail", message = message), 404
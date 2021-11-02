"""
The main Flask application.
"""
import os
from flask import Flask,redirect
from flask import request
from clientdetailsurlbuilder import ClientDetailsURLBuilder

app = Flask(__name__)

@app.route('/iplookup/')
def iplookup(): 
    """Lookup the specified IP"""
    ip_address = request.args.get('ipaddress')
    api_key = os.getenv('api_key') 
    network_id = os.getenv('network_id') 
    client_details_url_builder = ClientDetailsURLBuilder(api_key,network_id) 
    url = client_details_url_builder.get_url_for(ip_address)
    if url != None: 
        return redirect(url, code=302)
    else:
        return f"{ip_address} Not found"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)

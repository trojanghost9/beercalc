from calcapp.calculator import app
from calcapp.settings import web_host_address, web_host_port

app.run(debug=True, host=web_host_address, port=web_host_port)

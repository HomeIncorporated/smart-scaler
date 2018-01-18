from flask import Flask
from api_kubernetes_simulator.status import status
from api_kubernetes_simulator.pods import pods
from api_kubernetes_simulator.smart_scalers import smart_scalers
import logging


# Initialization
app = Flask(__name__)
app.config.from_object("config.Default")

# Configure logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging._nameToLevel[app.config["LOG_LEVEL"]])

# Routes
app.register_blueprint(status)
app.register_blueprint(pods)
app.register_blueprint(smart_scalers)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=app.config["KUBERNETES_PORT"], threaded=True)

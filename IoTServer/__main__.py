from IoTServer import create_app
from IoTServer.configs import ProductionConfig


create_app(config=ProductionConfig).run()

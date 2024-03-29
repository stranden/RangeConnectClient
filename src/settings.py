import os

# Range type
RANGE_TYPE = os.getenv("RANGE_TYPE", default="sius")

# SIUS Data
SIUSDATA_HOST = os.getenv("SIUSDATA_HOST", default="localhost")
SIUSDATA_PORT = os.getenv("SIUSDATA_PORT", default=4000)

# MEGALINK MLRange
MLRANGE_HOST = os.getenv("MLRANGE_HOST", default="localhost")
MLRANGE_PORT = os.getenv("MLRANGE_PORT", default=8088)
MLRANGE_WS_URI = f"ws://{MLRANGE_HOST}:{MLRANGE_PORT}/tv/ws"
MLRANGE_HTTP_URI = f"http://{MLRANGE_HOST}:{MLRANGE_PORT}/tv"

# RabbitMQ
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", default="localhost")
RABBITMQ_USER = os.getenv("RABBITMQ_USER", default="rangeconnect")
RABBITMQ_PASS = os.getenv("RABBITMQ_PASS", default="Uivq9ACXS49W")
RABBITMQ_URI = f"amqp://{RABBITMQ_USER}:{RABBITMQ_PASS}@{RABBITMQ_HOST}/"

# Shooting Range ID
# EBA2ED57-BF56-47DE-91F8-DEA032843FE3 is our test range
SHOOTING_RANGE_ID = os.getenv("SHOOTING_RANGE_ID", default="EBA2ED57-BF56-47DE-91F8-DEA032843FE3")
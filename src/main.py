import asyncio
import settings
import services.sius.message_parser
from util import *


async def tcp_client():
    logging.info(f"RANGE_TYPE is: \"{settings.RANGE_TYPE}\"")
    if settings.RANGE_TYPE == "sius":
        logging.info("Connecting to shooting range")
        reader, writer = await asyncio.streams.open_connection(
            settings.SIUSDATA_HOST, settings.SIUSDATA_PORT)

        SiusMessageParser = services.sius.message_parser.SiusMessageParser()
        
        while(True):
            data = await reader.readline()

            await SiusMessageParser.message_parser(data.decode(encoding="iso-8859-1"))

            #Publish = services.messaging.publisher.Publisher(settings.RABBITMQ_URI, settings.RANGE_TYPE)
            #await Publish.publish_range_events(message)
    else:
        logging.error(f"RANGE_TYPE is NOT supported - value: \"{settings.RANGE_TYPE}\"")

async def main():
    if check_shooting_range_id(settings.SHOOTING_RANGE_ID) == True:
        logging.info(f"SHOOTING_RANGE_ID is valid - value: \"{settings.SHOOTING_RANGE_ID}\"")
        logging.info("Creating Streaming task")

        task_stream = asyncio.create_task(
            tcp_client()
        )

        logging.info("Executing Streaming task")
        await task_stream
    else:
        logging.error(f"SHOOTING_RANGE_ID is NOT valid - value: \"{settings.SHOOTING_RANGE_ID}\"")

asyncio.run(main())

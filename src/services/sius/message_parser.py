from ..messaging import publisher
import settings
import logging
class SiusMessageParser:

    async def message_parser(self,message):
        if message:
            scoreEventType = message.split(";")[0]
            Publish = publisher.Publisher(settings.RABBITMQ_URI)
            if scoreEventType == "_GRPH":
                result = await self.group_event(message)
                if result:
                    await Publish.publish_range_events(result)
            elif scoreEventType == "_SHID":
                result = await self.shooter_event(message)
                if result:
                    await Publish.publish_range_events(result)
            elif scoreEventType == "_NAME":
                result = await self.name_event(message)
                if result:
                    await Publish.publish_range_events(result)
            elif scoreEventType == "_PRCH":
                result = await self.practice_event(message)
                if result:
                    await Publish.publish_range_events(result)
            elif scoreEventType == "_SHOT":
                result = await self.shot_event(message)
                if result:
                    await Publish.publish_range_events(result)
            elif scoreEventType == "_SNAT":
                result = await self.nation_event(message)
                if result:
                    await Publish.publish_range_events(result)
            elif scoreEventType == "_TEAM":
                result = await self.team_event(message)
                if result:
                    await Publish.publish_range_events(result)
            else:
                logging.warning(f"Could not process event type - message: {str(message).rstrip()}")
        else:
            logging.error("Message in 'message_parser' is empty - aborting!")
            raise Exception(f"ABORTING! Message in 'message_parser' is empty - connection to shooting range is lost!")
        
    async def group_event(self,message):
        eventData = message.split(";")
        if len(eventData) == 15:
            eventDict = dict()
            if int(eventData[3]) != 0:
                eventDict['shootingRangeID'] = str(settings.SHOOTING_RANGE_ID)
                eventDict['shootingRangeType'] = str(settings.RANGE_TYPE).upper()
                eventDict['scoreEventType'] = str("GROUP")
                ##eventDict['laneID'] = int(eventData[1])
                eventDict['firingPointID'] = str(eventData[2])
                eventDict['shooterID'] = int(eventData[3])
                eventDict['sequenceNumber'] = int(eventData[5])
                eventDict['timestamp'] = str.strip(eventData[6])
                eventDict['eventType'] = int(eventData[7])
                eventDict['groupOrdinal'] = int(eventData[9])
                if int(eventData[10]) == 0:
                    eventDict['firingType'] = str("SIGHTERS")
                elif int(eventData[10]) == 1:
                    eventDict['firingType'] = str("SINGLE_SHOT")
                elif int(eventData[10]) == 2:
                    eventDict['firingType'] = str("RAPID_FIRE")
                eventDict['expectedNumberOfShots'] = int(eventData[11])
                logging.info(f"Processed GROUP (_GRPH) event: {eventDict}")
            else:
                logging.info(f"Skipped GROUP (_GRPH) event on firingPointID {str(eventData[2])} because shooterID is 0")
            return eventDict

    async def shooter_event(self,message):
        eventData = message.split(";")
        if len(eventData) == 6:
            eventDict = dict()
            if int(eventData[3]) != 0:
                eventDict['shootingRangeID'] = str(settings.SHOOTING_RANGE_ID)
                eventDict['shootingRangeType'] = str(settings.RANGE_TYPE).upper()
                eventDict['scoreEventType'] = str("SHOOTER")
                ##eventDict['laneID'] = int(eventData[1])
                eventDict['firingPointID'] = str(eventData[2])
                eventDict['shooterID'] = int(eventData[3])
                #eventDict['aRandomNumber'] = int(eventData[4])
                #eventDict['duplicate-shooterID'] = int(eventData[5])
                logging.info(f"Processed SHOOTER (_SHID) event: {eventDict}")
            else:
                logging.info(f"Skipped SHOOTER (_SHID) event on firingPointID {str(eventData[2])} because shooterID is 0")
            return eventDict

    async def name_event(self,message):
        eventData = message.split(";")
        if len(eventData) == 6:
            eventDict = dict()
            if int(eventData[3]) != 0:
                eventDict['shootingRangeID'] = str(settings.SHOOTING_RANGE_ID)
                eventDict['shootingRangeType'] = str(settings.RANGE_TYPE).upper()
                eventDict['scoreEventType'] = str("NAME")
                ##eventDict['laneID'] = int(eventData[1])
                eventDict['firingPointID'] = str(eventData[2])
                eventDict['shooterID'] = int(eventData[3])
                eventDict['shooterName'] = str.rstrip(eventData[5])
                logging.info(f"Processed NAME (_NAME) event: {eventDict}")
            else:
                logging.info(f"Skipped NAME (_NAME) event on firingPointID {str(eventData[2])} because shooterID is 0")
            return eventDict
    
    async def practice_event(self,message):
        eventData = message.split(";")
        if len(eventData) == 26:
            eventDict = dict()
            if int(eventData[3]) != 0:
                eventDict['shootingRangeID'] = str(settings.SHOOTING_RANGE_ID)
                eventDict['shootingRangeType'] = str(settings.RANGE_TYPE).upper()
                eventDict['scoreEventType'] = str("PRACTICE")
                ##eventDict['laneID'] = int(eventData[1])
                eventDict['firingPointID'] = str(eventData[2])
                eventDict['shooterID'] = int(eventData[3])
                eventDict['sequenceNumber'] = int(eventData[5])
                eventDict['timestamp'] = str.rstrip(eventData[6])
                eventDict['eventType'] = int(eventData[7])
                eventDict['practiceSequenceNumber'] = int(eventData[11])
                eventDict['shootCode'] = int(eventData[13])
                eventDict['practiceCode'] = int(eventData[14])
                logging.info(f"Processed PRACTICE (_PRCH) event: {eventDict}")
            else:
                logging.info(f"Skipped PRACTICE (_PRCH) event on firingPointID {str(eventData[2])} because shooterID is 0")
            return eventDict

    async def shot_event(self,message):
        eventData = message.split(";")
        if len(eventData) == 24:
            eventDict = dict()
            if int(eventData[3]) != 0:
                eventDict['shootingRangeID'] = str(settings.SHOOTING_RANGE_ID)
                eventDict['shootingRangeType'] = str(settings.RANGE_TYPE).upper()
                eventDict['scoreEventType'] = str("SHOT")
                ##eventDict['laneID'] = int(eventData[1])
                eventDict['firingPointID'] = str(eventData[2])
                eventDict['shooterID'] = int(eventData[3])
                eventDict['sequenceNumber'] = int(eventData[5])
                eventDict['timestamp'] = str.rstrip(eventData[6])
                eventDict['eventType'] = int(eventData[7])
                eventDict['shotAttr'] = int(eventData[9])
                eventDict['shotValue'] = int(eventData[10])
                eventDict['shotValueDecimal'] = int(eventData[11])
                eventDict['shotID'] = int(eventData[13])
                eventDict['xCoord'] = float(eventData[14])
                eventDict['yCoord'] = float(eventData[15])
                eventDict['shotTimestamp'] = int(eventData[20])
                eventDict['caliber'] = int(eventData[22])
                logging.info(f"Processed SHOT (_SHOT) event: {eventDict}")
            else:
                logging.info(f"Skipped SHOT (_SHOT) event on firingPointID {str(eventData[2])} because shooterID is 0")
            return eventDict

    async def nation_event(self,message):
        eventData = message.split(";")
        if len(eventData) == 6:
            eventDict = dict()
            if int(eventData[3]) != 0:
                if len(str.rstrip(eventData[5])) > 0:
                    eventDict['shootingRangeID'] = str(settings.SHOOTING_RANGE_ID)
                    eventDict['shootingRangeType'] = str(settings.RANGE_TYPE).upper()
                    eventDict['scoreEventType'] = str("NATION")
                    ##eventDict['laneID'] = int(eventData[1])
                    eventDict['firingPointID'] = str(eventData[2])
                    eventDict['shooterID'] = int(eventData[3])
                    eventDict['shooterNation'] = str.rstrip(eventData[5])
                    logging.info(f"Processed NATION (_SNAT) event: {eventDict}")
                else:
                    logging.info(f"Skipped NATION (_SNAT) event on firingPointID {str(eventData[2])} because shooterNation is empty")
            else:
                logging.info(f"Skipped NATION (_SNAT) event on firingPointID {str(eventData[2])} because shooterID is 0")
            return eventDict

    async def team_event(self,message):
        eventData = message.split(";")
        if len(eventData) == 6:
            eventDict = dict()
            if int(eventData[3]) != 0:
                if len(str.rstrip(eventData[5])) > 0:
                    eventDict['shootingRangeID'] = str(settings.SHOOTING_RANGE_ID)
                    eventDict['shootingRangeType'] = str(settings.RANGE_TYPE).upper()
                    eventDict['scoreEventType'] = str("TEAM")
                    ##eventDict['laneID'] = int(eventData[1])
                    eventDict['firingPointID'] = str(eventData[2])
                    eventDict['shooterID'] = int(eventData[3])
                    eventDict['shooterTeam'] = str.rstrip(eventData[5])
                    logging.info(f"Processed TEAM (_TEAM) event: {eventDict}")
                else:
                    logging.info(f"Skipped TEAM (_TEAM) event on firingPointID {str(eventData[2])} because shooterTeam is empty")
            else:
                logging.info(f"Skipped TEAM (_TEAM) event on firingPointID {str(eventData[2])} because shooterID is 0")
            return eventDict

    
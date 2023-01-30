from dataclasses import dataclass, field, asdict
from typing import Dict, List, Generic, TypeVar
from abc import ABC, abstractmethod

from nerualpha.webhookEvents.whatsapp.IMessageEventContext import IMessageEventContext
from nerualpha.webhookEvents.whatsapp.IProfileName import IProfileName
from nerualpha.webhookEvents.whatsapp.IReplyObject import IReplyObject
from nerualpha.webhookEvents.whatsapp.IWhatsappReplyEvent import IWhatsappReplyEvent

@dataclass
class WhatsappReplyEvent(IWhatsappReplyEvent):
    to: str
    timestamp: str
    message_uuid: str
    from_: str
    channel: str
    message_type: str
    reply: IReplyObject
    profile: IProfileName = None
    context: IMessageEventContext = None
    provider_message: str = None
    def __init__(self):
        pass
    def reprJSON(self):
        result = {}
        dict = asdict(self)
        keywordsMap = {"from_":"from","del_":"del","import_":"import","type_":"type"}
        for key in dict:
            val = getattr(self, key)

            if val is not None:
                if type(val) is list:
                    parsedList = []
                    for i in val:
                        if hasattr(i,'reprJSON'):
                            parsedList.append(i.reprJSON())
                        else:
                            parsedList.append(i)
                    val = parsedList

                if hasattr(val,'reprJSON'):
                    val = val.reprJSON()
                if key in keywordsMap:
                    key = keywordsMap[key]
                result.__setitem__(key.replace('_hyphen_', '-'), val)
        return result

from dataclasses import dataclass, field, asdict
from typing import Dict, List, Generic, TypeVar
from abc import ABC, abstractmethod

from nerualpha.providers.voice.contracts.IConversationPayloadWithCallback import IConversationPayloadWithCallback
from nerualpha.session.IWrappedCallback import IWrappedCallback

@dataclass
class ConversationPayloadWithCallback(IConversationPayloadWithCallback):
    conversationId: str
    callback: IWrappedCallback
    def __init__(self,callback,conversationId):
        self.callback = callback
        self.conversationId = conversationId
    
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

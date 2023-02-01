from typing import Optional
from .objects.database_async import AsyncDatabase
from .objects.database_sync import SyncDatabase
from .objects.config import DatabaseConfig

def init_db(url:str,min_size:int=2,max_size:int=20,is_async:bool=False,db_config:Optional[DatabaseConfig]=None):
    config = DatabaseConfig(url=url,min_size=min_size,max_size=max_size) if db_config is None else db_config
    return (AsyncDatabase if is_async else SyncDatabase)(config=config)
        

        
        
            
        




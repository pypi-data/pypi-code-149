import json
from ..lib import MCLib
from error.file_format_error import FileFormatError

class MetaParser:
    def __init__(self, path: str):
        self.path = path

    def parse(self) -> dict:
        with open(self.path, "r", encoding="utf-8") as file:
            parsed_prop = {}
            file_json = json.load(file)
            
            pack_format = -1
            if "version" in file_json:
                pack_format = MCLib.convert_version(file_json["version"])
            elif "pack_format" in file_json:
                pack_format = file_json["pack_format"]
            else:
                return FileFormatError("{} 파일에 올바른 version 또는 pack_format이 명시되어 있지 않습니다".format(property_file))

            parsed_prop["pack"] = {}
            parsed_prop["pack"]["pack_format"] = pack_format
            return parsed_prop

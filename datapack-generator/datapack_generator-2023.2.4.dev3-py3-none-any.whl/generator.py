import json
from pathlib import Path
from parser.meta import MetaParser

def generate(path: str = ".", property_file: str = "pack.json", gen_dir: str = "generated"):
    gen_path = Path(gen_dir)

    if not gen_path.is_file():
        gen_path.mkdir(exist_ok=True)
    else:
        gen_path.unlink(missing_ok=True)
        gen_path.mkdir()

        parsed_prop = MetaParser(property_file).parse()
        with open(gen_path.as_posix() + "/pack.mcmeta", "w") as pack_meta:
            json.dump(parsed_prop, pack_meta)
import yaml
from collections import OrderedDict
from os import PathLike
from typing import Union
from urllib.parse import urlparse
import requests
import shutil
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def dump_yaml(*args, **kwargs):
    """A thin wrapper over yaml.dump which forces `OrderedDict`s to be
    serialized as mappings

    Otherwise behaves identically to yaml.dump
    """

    class OrderedDumper(yaml.Dumper):
        """A modified yaml serializer that forces pyyaml to represent
        an OrderedDict as a mapping instead of a sequence.
        """

        pass

    OrderedDumper.add_representer(OrderedDict, yaml.representer.SafeRepresenter.represent_dict)

    return yaml.dump(*args, Dumper=OrderedDumper, **kwargs)

def is_url(value: Union[PathLike, str]) -> bool:
    try:
        result = urlparse(str(value))
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def server_ok(url):
    # exception block
    try:
        response = requests.get(url)
         
        # check the status code
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.ConnectionError as e:
        return False

def download(url, target) -> bool:
    try:
        r = requests.get(url, verify=False, stream=True)
        r.raw.decode_content = True
        with open(target, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
        return True
    except:
        return False
    



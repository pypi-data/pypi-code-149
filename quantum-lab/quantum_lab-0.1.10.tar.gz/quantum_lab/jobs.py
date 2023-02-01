import requests
import json


def error_handler(response):
    print(f"Status: {response.status_code}")
    print(f"ErrorMessage: {response.json()['error']}")
    return {response.json()['error']}

def create( 
        userID: str, 
        uploadType: str, 
        shot: int, 
        resourceId: int,
        filePath: str, 
        volumeName: str, 
        resourceName: str
    ):
    url = "http://sdt-api.qcc.svc.cluster.local"
    url_path = f"{url}/qcc/notebook/job"

    headers = {
        "Content-Type": "application/json",
        "email": userID,
    }

    body = json.dumps({
        "uploadType": uploadType,
        "shot": shot,
        "resourceId": resourceId,
        "filePath": filePath,
        "volumeName": volumeName,
        "resourceName": resourceName
    })

    response = requests.post(f"{url_path}", headers=headers, data=body) 
    if response.status_code != 200:
        return error_handler(response)
    
    data = response.json()
    
    print("{:<15} {:<5}".format("ID", "Status"))
    print("{:<15} {:<5}".format(data["jobId"], data["status"]))
    
    return data["jobId"]

def getList(userID: str, limit = 0):
    url = "http://sdt-api.qcc.svc.cluster.local"
    url_path = f"{url}/qcc/notebook/jobs"

    headers = {
        "Content-Type": "application/json",
        "email": userID,
    }
    response = requests.get(f"{url_path}",headers=headers)
    
    if response.status_code != 200:
        return error_handler(response)
    
    data = response.json()

    print("{:<5} {:<10} {:<10} {:<12} {:<9} {:<8} {:<5} {:<11} {:<17} {:<30} {:<30}".format(
        "ID", 
        "JobID", 
        "ResourceID", 
        "ResourceName", 
        "RegStatus", 
        "Status", 
        "Shot",
        "UploadType",
        "FilePath", 
        "CreatedAt",
        "RunningAt"
        )
    )
    index = 0
    for ele in data["jobs"]:
        print("{:<5} {:<10} {:<10} {:<12} {:<9} {:<8} {:<5} {:<11} {:<17} {:<30} {:<30}".format(
            ele["id"], 
            ele["jobId"], 
            ele["resourceId"], 
            ele["resourceName"], 
            ele["jobRegStatus"], 
            ele["jobStatus"], 
            ele["jobShot"],
            ele["jobUploadType"],
            ele["jobFilePath"].split('/')[-1],
            ele["createdAt"],
            ele["runningAt"]
            )
        )
        index += 1 
        if limit != 0 and index > limit:
            break

    return data["jobs"]

def getJob(userID: str, id: int):
    url = "http://sdt-api.qcc.svc.cluster.local"
    url_path = f"{url}/qcc/notebook/job/{id}"

    headers = {
        "Content-Type": "application/json",
        "email": userID,
    }
    response = requests.get(f"{url_path}", headers=headers)
    
    if response.status_code != 200:
        return error_handler(response)

    data = response.json()
    print("{:<5} {:<10} {:<10} {:<12} {:<9} {:<8} {:<5} {:<11} {:<17} {:<30} {:<30}".format(
        "ID", 
        "JobID", 
        "ResourceID", 
        "ResourceName", 
        "RegStatus", 
        "Status", 
        "Shot",
        "UploadType",
        "FilePath", 
        "CreatedAt",
        "RunningAt"
        )
    )
    print("{:<5} {:<10} {:<10} {:<12} {:<9} {:<8} {:<5} {:<11} {:<17} {:<30} {:<30}".format(
        data["id"], 
        data["jobId"], 
        data["resourceId"], 
        data["resourceName"], 
        data["jobRegStatus"], 
        data["jobStatus"], 
        data["jobShot"],
        data["jobUploadType"],
        data["jobFilePath"].split('/')[-1],
        data["createdAt"],
        data["runningAt"]
        )
    )
     
    return data

def delete(userID: str, id: str):
    url = "http://sdt-api.qcc.svc.cluster.local"
    url_path = f"{url}/qcc/noteboo/job/{id}"

    headers = {
        "Content-Type": "application/json",
        "email": userID,
    }
    response = requests.delete(f"{url_path}", headers=headers)
    if response.status_code != 200:
        return error_handler(response)

    print(f"Deleted job : {response.text}")

    return response.text


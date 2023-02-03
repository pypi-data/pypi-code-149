import getmac
from datetime import datetime, timedelta
from cryptography.fernet import Fernet

class Cert:
    def __init__(self):
        print("Start to verify to use abba models")
        try:
            with open('.key', 'r') as f:
                self.key, self.encrypted_text = f.read().splitlines()
        except FileNotFoundError as f:
            print(f"Not found Key file")

    def _decrypto(self, key, encrypted_text):
        cipher_suite = Fernet(key)
        decrypted_text = cipher_suite.decrypt(encrypted_text).decode('utf-8')
        return decrypted_text
    
    
    def _expired_date(self, expired_date):
        is_expired = False
        if datetime.today() <= datetime.strptime(expired_date, '%Y%m%d'):
            is_expired = True
        
        # print(f"is expired: {is_expired} (expire to {expired_date})")
        return is_expired
    
    
    def _compare_key(self, key1, key2):
        is_samekey = False
        if key1 == key2:
            is_samekey = True
        
        # print(f"is same key : {is_samekey}")
        return is_samekey
    
    
    def _compare_mac_addr(self, mac_addr):
        THIS_MAC_ADDR = getmac.get_mac_address()
        is_same_mac = False
        if mac_addr == THIS_MAC_ADDR:
            is_same_mac = True
            
        # print(f"is same mac addr ? {is_same_mac}")
        return is_same_mac
    
    
    def _compare(self, *args):
        _, EXPIRED_DATE, MAC_ADDRESS, DEC_KEY, _ = args
        if not self._expired_date(EXPIRED_DATE) and self._compare_key(self.key, DEC_KEY) and self._compare_mac_addr(MAC_ADDRESS):
            return True 
        
        return False
    
    
    def certificate(self):
        decrypted_text = self._decrypto(self.key, self.encrypted_text)
        items = decrypted_text.split('-*-')
        if self._compare(*items):
            return True
        
        return False
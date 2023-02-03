from abba.cert import Cert

try:
    c = Cert()
    if c.certificate():
        raise BaseException("Invalid permission, Check certifiaction")
    print("It's valid certification")
except Exception as e:
    print(f"{e}")
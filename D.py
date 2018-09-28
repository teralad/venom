import base64
import sys

class D:
    def decode(self,LocationID):
        try:
            decoded_value = base64.b64decode(LocationID).decode("utf-8")
            return decoded_value.replace("Location:","")
        except:
            return "Exception while decode"

if __name__ == '__main__':
    d = D()
    print(d.decode(sys.argv[1]))

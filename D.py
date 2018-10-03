import base64
import sys

class D:
    def decode(self,LocationID):
        try:
            decoded_value = base64.b64decode(LocationID).decode("utf-8")
            db_id = decoded_value.split(":")[-1]
            return db_id
        except Exception as e:
            print("Error while decoding the key: {}".format(e))

if __name__ == '__main__':
    d = D()
    print(d.decode(sys.argv[1]))

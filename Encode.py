import base64
import sys

class Encode:
    def encode(self,klass_id):
        try:
            encoded_value = base64.b64encode(bytes((f'{klass_id}'), 'utf-8'))
            return encoded_value.decode("utf-8")
        except:
            return "Exception during encode"

if __name__ == '__main__':
    e = Encode()
    print(e.encode(sys.argv[1]))

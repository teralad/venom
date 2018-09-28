import base64
import sys

class E:
    def encode(self,Location):
        try:
            encoded_value = base64.b64encode(bytes((f'Location:{Location}'), 'utf-8'))
            return encoded_value.decode("utf-8")
        except:
            return "Exception during encode"

if __name__ == '__main__':
    e = E()
    print(e.encode(sys.argv[1]))

import base64

string = "This is a Message"

string_bytes = string.encode('ascii')
b64_bytes = base64.b64encode(string_bytes)

b64_string = b64_bytes.decode('ascii')

print("Base64 Encoded String: ", b64_string)


b64_string = "VGhpcyBpcyBhIE1lc3NhZ2U="
b64_bytes = b64_string.encode("ascii")

string_bytes = base64.b64decode(b64_bytes)
string  = string_bytes.decode("ascii")

print("Decoded String: ",string)
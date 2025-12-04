from black_mirror.core import BlackMirror

bm = BlackMirror()

result = bm.lookup("email", "support@github.com")

print(result)
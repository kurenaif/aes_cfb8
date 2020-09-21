from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import copy


iv = b"\x00" * 16

def encrypt(bs: bytes, key: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_ECB)
    res = list(iv + bs)
    iv_len = len(iv)

    for i in range(len(bs)):
        res[iv_len + i] = cipher.encrypt(bytes(res[i:i+iv_len]))[0] ^ res[iv_len + i]

    return bytes(res[iv_len:])

def decrypt(bs: bytes, key: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_ECB)
    res = list(iv + bs)
    iv_len = len(iv)

    for i in range(len(bs)-1, -1, -1):
        res[iv_len + i] = cipher.encrypt(bytes(res[i:i+iv_len]))[0] ^ res[iv_len + i]

    return bytes(res[iv_len:])

cnt = 0
for i in range(10000):
    key = get_random_bytes(32)
    m = b"\x00" * 8
    if encrypt(m, key) == m:
        cnt += 1

print("score: ", cnt)
print("probability: ", cnt/10000)
print("1/256: ", 1/256)

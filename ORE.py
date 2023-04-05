import hashlib

class ORE:

    def __init__(self, key, size = 16, LEN  = 16):
        self.key = key
        self.LEN = LEN
        self.size = size

    def __prf(self, msg):
        pad = "0" * (self.LEN - len(msg))
        return int(hashlib.sha256((str(msg) + pad + str(self.key)).encode()).hexdigest(), 16)

    def encode(self, data):
        m = bin(data)[2:]
        m = "0"*(self.size - len(m)) + m
        tmp_m = ""
        tmpres = ""
        for i in m:
            tmp_m += i
            tmpres += str((self.__prf(tmp_m[:-1]) + int(tmp_m[-1])) % 3)
        return tmpres

    def compare(self, u, v):
        if u == v:
            return 0
        L = len(u)
        cnt = 0
        while u[cnt] == v[cnt]:
            cnt += 1
        if (int(u[cnt]) + 1) % 3 == int(v[cnt]):
            return -1
        else:
            return 1

    def decode(self, c):
        tmp_m = ""
        for i in range(len(c)):
            for j in [0, 1]:
                if (self.__prf(tmp_m) + j) % 3 == int(c[i]):
                    tmp_m += str(j)
                    break
        return int(tmp_m, 2)


# Inspired by https://github.com/kpatsakis/OrderRevealingEncryption
# and https://icerm.brown.edu/materials/Slides/tw19-1-es/Order-Revealing_Encryption_-_Definitions,_Constructions,_and_Challenges_]_David_Wu,_University_of_Virginia.pdf

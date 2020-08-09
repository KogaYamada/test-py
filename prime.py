import math


# 素数か素数でないかを判定する関数
def is_prime(n):
    if n < 3:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

import requests
from Crypto.Util.number import *

n = 79044710342705724226901406661979796331640340763264041228241901614110403486399197120635416893468070883202621988087158531521779292067257089453999614736189911959778380748298383360529637181603656694599163077760634122250356978083170437776814469181318085912465814423415093802972642378268877109640032723461308359367

url = "http://127.0.0.1:5000/guess_bit"

k = 15

def send(a):
    payload = {'bit': a}
    return eval(requests.get(url, params=payload).content.decode())['guess']

def check(a):
    if a >=  n//2: return 1
    return 0

if __name__ == "__main__":
    s = ''
    i = 0
    try:
        while 1:
            if all([check(send(i)) for _ in range(k)]):
                s += '0'
            else:
                s += '1'
            i += 1
    except Exception as e:
        print(repr(e))
    a = int(s, 2)
    print(long_to_bytes(a))



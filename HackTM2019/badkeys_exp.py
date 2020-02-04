from gmpy import next_prime
from Crypto.Util.number import *
from pwn import *

#finds the inital value of p
def exploit(mp) :
    p = mp - 9000000
    while True :
        q = n//p
        if p*q == n :
            return p,q
        p = next_prime(p)

# gets the faulty prime generated using next_prime()
def get_mp(r) :
    d = -1
    while d<0 :
        r.recv()
        r.sendline('k')
        (e,n),(d,n) = eval(r.recvline_startswith("((65537"))
        try :
            k = RSA.construct((n,long(e),d))
            if str(k.p).startswith("12117717634661447") :
                return k.p
            else :
                return k.q
        except :
            continue



if __name__ == "__main__" :
    r = remote("138.68.67.161",60005)
    (p,q) = exploit(get_mp(r))
    phi = (p-1)*(q-1)
    (e,n) = eval(open('RSA_PUB').read())
    d = inverse(e,phi)
    flag = long_to_bytes(pow(eval(open('flag.enc').read().strip()),d,n))
    print "Flag :" + flag


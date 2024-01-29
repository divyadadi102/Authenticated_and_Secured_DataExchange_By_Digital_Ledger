#import hashlib
#import lib.common
#from model import Model
#from lib.common import pubkey_to_address
import rsa
from rsa import PrivateKey, PublicKey
import os
client_loc =str('C:/Users/acer/Desktop/majorproject/venv/projectcode/client/')
server_loc = str('C:/Users/acer/Desktop/majorproject/venv/projectcode/server/')
def generate_keys(username):
    (pubKey, privKey) = rsa.newkeys(1024)
    os.makedirs(client_loc+username)
    with open(client_loc+str(username)+'/pubkey.pem', 'wb') as f:
        f.write(pubKey.save_pkcs1('PEM'))
    f.close()
    with open(client_loc+str(username)+'/privkey.pem', 'wb') as f:
        f.write(privKey.save_pkcs1('PEM'))
    f.close()
    with open(client_loc+str(username)+'/data.txt', 'w') as fp:
        pass
    fp.close()
    with open(server_loc+'accounts.txt', 'a') as fp:
        fp.write(str(username)+'\n')
    fp.close()
def load_keys(username):
    with open(client_loc+str(username)+'/pubkey.pem', 'rb') as f:
        pubKey = rsa.PublicKey.load_pkcs1(f.read())

    with open(client_loc+str(username)+'/privkey.pem', 'rb') as f:
        privKey = rsa.PrivateKey.load_pkcs1(f.read())

    return pubKey, privKey
def new_account(user_name):
    generate_keys(user_name)
    #publickey,privatekey = load_keys(user_name)
    #print(publickey)

user_name = input('Enter username  :')
new_account(user_name)
'''if user_name in users:
    print("user exist")
else:
    users.append(user_name)
    new_account()'''
#!/usr/bin/python

import sys, time, jwt
from struct import *

from pymongo import MongoClient

SECRET_KEY = "geheimnisDesGrauens"
mongoUrl = "mongodb://localhost:27017/friendscomm"

def log(string):
    a = open('auth.log', 'a')
    a.write(string + '\n')
	
def from_ejabberd():
    input_length = sys.stdin.read(2)
    (size,) = unpack('>h', input_length)
    return sys.stdin.read(size).split(':')

def to_ejabberd(bool):
    answer = 0
    if bool:
        answer = 1
    token = pack('>hh', 2, answer)
    log('writing token ' + str(token) + ' to stdout')
    log('answer' + str(answer))
    sys.stdout.write(token)
    sys.stdout.flush()

def auth(username, server, password):
	auth_token = password
	nickname = get_nickname(auth_token)
	log('doing auth for:' + nickame)
	client = MongoClient(mongoUrl)
	collection = client.users
	result = str(client.user.find_one({"Nickname":nickname}))
	comp = str('None')
	if result == comp:
		log('access granted')
		return False
	else:
		log('access denied invalid user')
		return True 

def isuser(username, server):
    return True

def setpass(username, server, password):
    return True



def get_nickname(auth_token):
    try:
        payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
        return payload['nickname']
    except jwt.ExpiredSignatureError:
		log('Signature expired.')
        return False
    except jwt.InvalidTokenError:
		log('Invalid token.')
        return False


	
while True:
    data = from_ejabberd()
    success = False
    if data[0] == "auth":
        success = auth(data[1], data[2], data[3])
    elif data[0] == "isuser":
        success = isuser(data[1], data[2])
    elif data[0] == "setpass":
        success = setpass(data[1], data[2], data[3])
    to_ejabberd(success)
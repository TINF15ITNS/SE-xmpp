#!/usr/bin/python



import sys, time

from struct import *



def log(string):
    a = open("$EJABBERD_HOME/auth.log", 'a')
    a.write(string + '\n')



def from_ejabberd():
    print 'in from_ejabberd'
    input_length = sys.stdin.read(2)
    (size,) = unpack('>h', input_length)
    return sys.stdin.read(size).split(':')



def to_ejabberd(bool):
    print 'in to_ejabberd'
    answer = 0
    if bool:
        answer = 1
    token = pack('>hh', 2, answer)
    log('writing token ' + str(token) + ' to stdout')
    log('answer' + str(answer))
    sys.stdout.write(token)
    sys.stdout.flush()



def auth(username, server, password):
    print 'in auth'
    log('doing auth:' + username + ':' + server + ':' + password)
    return True



def isuser(username, server):
    print 'in isuser'
    return True



def setpass(username, server, password):
    print 'in setpass'
    return True

def tryregister(username, server, password):
    print 'in tryregister'
    return True


exitcode=0

while True:
    print 'in infiniteloop'
    data = from_ejabberd()
    success = False
    try:
        if data[0] == "auth":
            print 'in infinite auth'
            success = auth(data[1], data[2], data[3])
    
        elif data[0] == "isuser":
            print 'in infinite isuser'
            success = isuser(data[1], data[2])
    
        elif data[0] == "setpass":
            print 'in infinite setpass'
            success = setpass(data[1], data[2], data[3])

        elif data[0] == "tryregister":
            print 'in infinite tryregister'
            success = tryregister(data[1], data[2], data[3])
    except Exception:
         pass
    print 'before to_ejabberd in infinteloop'
    to_ejabberd(success)

print 'before sys.exit'
sys.exit(exitcode)
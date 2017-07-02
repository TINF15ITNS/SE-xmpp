# Setup

import sys, logging, struct, jwt, yaml

from pymongo import MongoClient

sys.stderr = open('/var/log/ejabberd/extauth_err.log', 'a')
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='/var/log/ejabberd/extauth.log',
                    filemode='a')

config = yaml.load(open("/etc/friendscomm.yml", 'r'))

database_name = config['mongodb']['uri'].rsplit('/', 1)[1]

key = config['server']['key']

db = MongoClient(config['mongodb']['uri'])[database_name].users

logging.info('extauth script started, waiting for ejabberd requests')

class EjabberdInputError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

# Declarations

def ejabberd_in():
    logging.debug("trying ti read 2 bytes from ejabberd:")
    input_length = sys.stdin.read(2)

    if len(input_length) is not 2:
        logging.debug("ejabberd sent us wrong things!")
        raise EjabberdInputError('Wrong input from ejabberd!')

    logging.debug('got 2 bytes via stdin: %s'%input_length)

    (size,) = struct.unpack('>h', input_length)
    logging.debug('size of data: %i'%size)

    income=sys.stdin.read(size).split(':')
    logging.debug("incoming data: %s"%income)

    return income

def ejabberd_out(bool):
    logging.debug('Ejabberd gets: %s' %bool)

    answer = 0
    if bool:
        answer = 1
    token = struct.pack('>hh', 2, answer)

    logging.debug("sent bytes: %#x %#x %#x %#x" % (ord(token[0]), ord(token[1]), ord(token[2]), ord(token[3])))

    sys.stdout.write(token)
    sys.stdout.flush()

def get_nickname(token):
    logging.debug('extracting nickname from token: %s' %token)
    try:
        payload = jwt.decode(token, key)
    except jwt.ExpiredSignatureError:
        logging.debug('Signature expired.')
        return False
    except jwt.InvalidTokenError:
        logging.debug('Invalid token.')
        return False

    nickname = payload['nickname']
    logging.debug('Extracted nickname: %s' %nickname)

def auth(username, server, password):
    logging.debug('Attempting Authentication')
    nickname = get_nickname(password)

    result = db.find_one({"nickname":nickname}).count()
    if result == 1:
        logging.debug('Authenticated, return True')
        return True
    else:
        logging.debug('Authentication denied')
        return False

def isuser(username, server):
    return True

def setpass(username, server, password):
    return True

# Main Loop

exitcode=0

while True:
    logging.debug("start of infinite loop")

    try:
        ejab_request = ejabberd_in()
    except EOFError:
        break
    except Exception as e:
        logging.exception("Exception occured while reading stdin")
        raise

    logging.debug('operation: %s' % (":".join(ejab_request)))

    op_result = False
    try:
        if ejab_request[0] == "auth":
            op_result = auth(ejab_request[1], ejab_request[2], ejab_request[3])
        elif ejab_request[0] == "isuser":
            op_result = isuser(ejab_request[1], ejab_request[2])
        elif ejab_request[0] == "setpass":
            op_result = setpass(ejab_request[1], ejab_request[2], ejab_request[3])
        # elif ejab_request[0] == "tryregister":
            # op_result = tryregister(ejab_request[1], ejab_request[2], ejab_request[3])
        # elif ejab_request[0] == "removeuser":
            # op_result = removeuser(ejab_request[1], ejab_request[2])
        # elif ejab_request[0] == "removeuser3":
            # op_result = removeuser3(ejab_request[1], ejab_request[2], ejab_request[3])
    except Exception:
        logging.exception("Exception occured")

    ejabberd_out(op_result)
    logging.debug("successful" if op_result else "unsuccessful")

logging.debug("end of infinite loop")
logging.info('extauth script terminating')
database.close()
sys.exit(exitcode)

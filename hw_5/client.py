from socket import *
import pickle
import argparse
import time

import logging
import log.client_log_config

logger = logging.getLogger('client')


def parser_init():
    try:
        parser = argparse.ArgumentParser(description='Client')
        parser.add_argument('--addr', type=str, default='localhost', help='ip')
        parser.add_argument('--port', type=int, default=7777, help='tcp-port')
        logger.info('parser init success')
        return parser.parse_args()
    except:
        logger.error('parser init error', exc_info=True)


def socket_init(addr, port):
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((addr, port))
        logger.info('socket init success')
        return s
    except:
        logger.error('socket init error', exc_info=True)


def main(new_socket):
    msg = {
        "action": "presence",
        "time": time.time(),
        "type": "status",
        "user": {
            "account_name": "User_1",
            "status": "Online"
        }
    }

    try:
        new_socket.send(pickle.dumps(msg))
        logger.info('message sent to the server')
    except:
        logger.error('message sent error', exc_info=True)

    data = new_socket.recv(1024)
    response = pickle.loads(data)['response']
    new_socket.close()
    return response


if __name__ == '__main__':
    args = parser_init()
    socket = socket_init(args.addr, args.port)
    main(socket)

from socket import *
import pickle
import argparse
import time

import logging
import log.server_log_config

logger = logging.getLogger('server')


def parser_init():
    try:
        parser = argparse.ArgumentParser(description='Server')
        parser.add_argument('--port', type=int, default=7777, help='tcp-port')
        parser.add_argument('--addr', type=str, default='localhost', help='ip')
        logger.info('parser init success')
        return parser.parse_args()
    except:
        logger.error('parser init error', exc_info=True)


def socket_init(addr, port):
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.bind((addr, port))
        s.listen(5)
        s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        logger.info('socket init success')
        return s
    except:
        logger.error('socket init error', exc_info=True)


def main(new_socket, testing=False):
    while True:
        if testing:
            new_socket.close()
            return 'OK'

        client, addr = new_socket.accept()
        data = client.recv(1024)
        logger.info('message from client: %s', pickle.loads(data))

        resonse = {
            "response": 200,
            "time": time.time(),
            "alert": "Вы online"
        }
        try:
            client.send(pickle.dumps(resonse))
            client.close()
            logger.info('reply sent to the client')
        except:
            logger.error('reply sent error', exc_info=True)


if __name__ == '__main__':
    args = parser_init()
    socket = socket_init(args.addr, args.port)
    main(socket)

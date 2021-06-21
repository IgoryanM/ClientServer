from socket import *
import argparse
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


def read_messages(socket):
    data = socket.recv(1024).decode('utf-8')
    print(data)


def write_messages(socket):
    msg = input('Ваше сообщение: ')
    if msg == 'exit':
        return 'exit'
    try:
        socket.send(msg.encode('utf-8'))
        logger.info('message sent to the server')
    except:
        logger.error('message sent error', exc_info=True)


def main(client_socket, ctype: str):
    with client_socket as sock:
        if ctype == 'r':
            while True:
                read_messages(sock)
        elif ctype == 'w':
            while True:
                if write_messages(sock) == 'exit':
                    break
                write_messages(sock)


if __name__ == '__main__':
    args = parser_init()
    socket = socket_init(args.addr, args.port)
    client_type = input('Please, choose client type - only read (r) or only write (w): ')
    main(socket, client_type)

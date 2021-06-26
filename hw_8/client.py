from socket import *
import argparse
import logging
from threading import Thread
import datetime
import pickle

import log.client_log_config
import jim

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
    while True:
        data = socket.recv(1024)
        if data:
            print(pickle.loads(data))


def write_messages(socket):
    msg = jim.presence
    msg['time'] = str(datetime.datetime.now().replace(microsecond=0))
    socket.send(pickle.dumps(msg))

    name = input('Введите ваше имя: ')

    while True:
        command = input(
            'Введите команду (j - вступить в чат, lv - выйти из чата, q - отключиться, m - отправить сообщение:\n')

        if command == 'q':
            msg = jim.quit_server
            socket.send(pickle.dumps(msg))
            break
        try:
            if command == 'j':
                msg = jim.join
                msg['time'] = str(datetime.datetime.now().replace(microsecond=0))
                socket.send(pickle.dumps(msg))
            elif command == 'lv':
                msg = jim.leave
                msg['time'] = str(datetime.datetime.now().replace(microsecond=0))
                socket.send(pickle.dumps(msg))
            elif command == 'm':
                msg = jim.msg
                msg['time'] = str(datetime.datetime.now().replace(microsecond=0))
                msg['to'] = 'user_2'
                msg['from'] = name
                msg['message'] = input('Введите ваше сообщение: ')
                socket.send(pickle.dumps(msg))

            logger.info('message sent to the server')
        except:
            logger.error('message sent error', exc_info=True)


def main(client_socket):
    r_thread = Thread(target=read_messages, args=(client_socket,))
    r_thread.daemon = True
    r_thread.start()

    w_thread = Thread(target=write_messages, args=(client_socket,))
    w_thread.start()


if __name__ == '__main__':
    args = parser_init()
    socket = socket_init(args.addr, args.port)
    main(socket)

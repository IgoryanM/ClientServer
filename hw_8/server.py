import pickle
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
import logging
import log.server_log_config
import select
import argparse

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
        s.settimeout(0.2)
        s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        logger.info('socket init success')
        return s
    except:
        logger.error('socket init error', exc_info=True)


def read_requests(r_clients, all_clients):
    requests = {}
    for sock in r_clients:
        try:
            data = pickle.loads(sock.recv(1024))
            requests[sock] = data
        except:
            print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
            all_clients.remove(sock)
    return requests


def write_responses(requests, w_clients, all_clients):
    for sock in w_clients:
        if sock in requests:
            try:
                if requests[sock]['action'] == 'msg':
                    time = requests[sock]['time']
                    name = requests[sock]['from']
                    message = requests[sock]['message']
                    resp = pickle.dumps(f'{time} - {name}: {message}')
                    print(resp)
                    for client in w_clients:
                        if client != sock:
                            client.send(resp)
            except:
                print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
                sock.close()
                all_clients.remove(sock)


def main(socket, testing=False):
    clients = []

    while True:
        if testing:
            socket.close()
            return 'OK'

        try:
            conn, addr = socket.accept()
        except OSError as e:
            pass
        else:
            print("Получен запрос на соединение от %s" % str(addr))
            clients.append(conn)
        finally:
            wait = 10
            r = []
            w = []
            try:
                r, w, e = select.select(clients, clients, [], wait)
            except:
                pass

            requests = read_requests(r, clients)
            if requests:
                write_responses(requests, w, clients)


if __name__ == '__main__':
    args = parser_init()
    socket = socket_init(args.addr, args.port)
    main(socket)

from socket import *
import pickle
import argparse
import time


def parser_init():
    parser = argparse.ArgumentParser(description='Server')
    parser.add_argument('-p', type=int, default=7777, help='tcp-port')
    parser.add_argument('-a', type=str, default='', help='ip')
    return parser.parse_args()


def socket_init(addr, port):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((addr, port))
    s.listen(5)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    return s


def main(new_socket):
    while True:
        client, addr = new_socket.accept()
        data = client.recv(1024)
        print('Сообщение от клиента: ', pickle.loads(data))

        resonse = {
            "response": 200,
            "time": time.time(),
            "alert": "Вы online"
        }

        client.send(pickle.dumps(resonse))
        client.close()


if __name__ == '__main__':
    args = parser_init()
    socket = socket_init(args.a, args.p)
    main(socket)

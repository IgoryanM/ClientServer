from socket import *
import pickle
import argparse
import time


def parser_init():
    parser = argparse.ArgumentParser(description='Client')
    parser.add_argument('--addr', type=str, default='localhost', help='ip')
    parser.add_argument('--port', type=int, default=7777, help='tcp-port')
    return parser.parse_args()


def socket_init(addr, port):
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((addr, port))
    return s


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

    new_socket.send(pickle.dumps(msg))
    data = new_socket.recv(1024)
    response = pickle.loads(data)['response']
    new_socket.close()
    print(response)
    return response


if __name__ == '__main__':
    args = parser_init()
    socket = socket_init(args.addr, args.port)
    main(socket)

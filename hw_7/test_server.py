import unittest
import server


class TestServer(unittest.TestCase):
    def test_parser_init(self):
        self.assertEqual(server.parser_init().__str__(), "Namespace(addr='localhost', port=7777)")

    def test_main_server(self):
        self.assertEqual(server.main(server.socket_init('localhost', 7777), testing=True), 'OK')


if __name__ == "__main__":
    unittest.main()

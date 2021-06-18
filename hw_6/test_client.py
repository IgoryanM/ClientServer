import unittest
import client


class TestClient(unittest.TestCase):
    def test_parser_init(self):
        self.assertEqual(client.parser_init().__str__(), "Namespace(addr='localhost', port=7777)")

    def test_main_client(self):
        self.assertEqual(client.main(client.socket_init('localhost', 7777)), 200)


if __name__ == "__main__":
    unittest.main()

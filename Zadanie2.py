import unittest
from unittest.mock import *

class Subscriber:
    def __init__(self):
        self.clients = []

    def addClient(self, client):
        if type(client) is not str:
            raise Exception("Client must be str")
        self.clients.append(client)
        return self.clients
    
    def deleteClient(self, client):
        if type(client) is not str:
            raise Exception("Client must be str")
        elif client not in self.clients:
            raise Exception("Client not in client list")
        self.clients.remove(client)
        return self.clients

    def sendMessageToClient(self, client, message):
        pass

class TestSubscriber(unittest.TestCase):
    def setUp(self):
        self.temp = Subscriber()

    def test_add_client(self):
        self.temp.addClient = MagicMock(return_value=["Client"])
        self.assertEqual(["Client"], self.temp.addClient())

    def test_add_client_exception_client_not_str_but_int(self):
        self.temp.addClient = MagicMock(side_effect=Exception("Client must be str"))
        with self.assertRaisesRegex(Exception, "Client must be str"):
            self.temp.addClient(1)

    def test_add_client_exception_client_not_str_but_float(self):
        self.temp.addClient = MagicMock(side_effect=Exception("Client must be str"))
        with self.assertRaisesRegex(Exception, "Client must be str"):
            self.temp.addClient(43.34123)

    def test_add_client_exception_client_not_str_but_list(self):
        self.temp.addClient = MagicMock(side_effect=Exception("Client must be str"))
        with self.assertRaisesRegex(Exception, "Client must be str"):
            self.temp.addClient([])

    def test_add_client_exception_client_not_str_but_tuple(self):
        self.temp.addClient = MagicMock(side_effect=Exception("Client must be str"))
        with self.assertRaisesRegex(Exception, "Client must be str"):
            self.temp.addClient(())

    def test_add_client_exception_client_not_str_but_dict(self):
        self.temp.addClient = MagicMock(side_effect=Exception("Client must be str"))
        with self.assertRaisesRegex(Exception, "Client must be str"):
            self.temp.addClient({})

    def test_delete_client(self):
        self.temp.deleteClient = MagicMock(return_value=[])
        self.assertEqual([], self.temp.deleteClient("Client"))

    def test_delete_client_exception_client_not_str_but_int(self):
        self.temp.deleteClient = MagicMock(side_effect=Exception("Client must be str"))
        with self.assertRaisesRegex(Exception, "Client must be str"):
            self.temp.deleteClient(1)

    def test_delete_client_exception_client_not_str_but_float(self):
        self.temp.deleteClient = MagicMock(side_effect=Exception("Client must be str"))
        with self.assertRaisesRegex(Exception, "Client must be str"):
            self.temp.deleteClient(43.34123)

    def test_delete_client_exception_client_not_str_but_list(self):
        self.temp.deleteClient = MagicMock(side_effect=Exception("Client must be str"))
        with self.assertRaisesRegex(Exception, "Client must be str"):
            self.temp.deleteClient([])

    def test_delete_client_exception_client_not_str_but_tuple(self):
        self.temp.deleteClient = MagicMock(side_effect=Exception("Client must be str"))
        with self.assertRaisesRegex(Exception, "Client must be str"):
            self.temp.deleteClient(())

    def test_delete_client_exception_client_not_str_but_dict(self):
        self.temp.deleteClient = MagicMock(side_effect=Exception("Client must be str"))
        with self.assertRaisesRegex(Exception, "Client must be str"):
            self.temp.deleteClient({})

    def test_delete_client_exception_client_not_in_list(self):
        self.temp.deleteClient = MagicMock(side_effect=Exception("Client not in client list"))
        with self.assertRaisesRegex(Exception, "Client not in client list"):
            self.temp.deleteClient("Client1234")

    def test_send_message_to_client(self):
        self.temp.sendMessageToClient = MagicMock(return_value = True)
        self.assertTrue(self.temp.sendMessageToClient("Client", "Hello"))

    def test_send_message_to_client_exception_client_not_str_but_int(self):
        self.temp.sendMessageToClient = MagicMock(side_effect=Exception("Client must be str"))
        with self.assertRaisesRegex(Exception, "Client must be str"):
            self.temp.sendMessageToClient(8, "Hello")

    def test_send_message_to_client_exception_client_not_str_but_list(self):
        self.temp.sendMessageToClient = MagicMock(side_effect=Exception("Client must be str"))
        with self.assertRaisesRegex(Exception, "Client must be str"):
            self.temp.sendMessageToClient([], "Hello")

    def test_send_message_to_client_exception_client_not_str_but_float(self):
        self.temp.sendMessageToClient = MagicMock(side_effect=Exception("Client must be str"))
        with self.assertRaisesRegex(Exception, "Client must be str"):
            self.temp.sendMessageToClient(8.532, "Hello")

    def test_send_message_to_client_exception_client_not_str_but_dict(self):
        self.temp.sendMessageToClient = MagicMock(side_effect=Exception("Client must be str"))
        with self.assertRaisesRegex(Exception, "Client must be str"):
            self.temp.sendMessageToClient({}, "Hello")

    def test_send_message_to_client_exception_client_not_str_but_tuple(self):
        self.temp.sendMessageToClient = MagicMock(side_effect=Exception("Client must be str"))
        with self.assertRaisesRegex(Exception, "Client must be str"):
            self.temp.sendMessageToClient((), "Hello")

    def test_send_message_to_client_exception_message_not_str_but_int(self):
        self.temp.sendMessageToClient = MagicMock(side_effect=Exception("Client must be str"))
        with self.assertRaisesRegex(Exception, "Client must be str"):
            self.temp.sendMessageToClient("Client", 4)

    def test_send_message_to_client_exception_message_not_str_but_float(self):
        self.temp.sendMessageToClient = MagicMock(side_effect=Exception("Client must be str"))
        with self.assertRaisesRegex(Exception, "Client must be str"):
            self.temp.sendMessageToClient("Client", 3.42341)

    def test_send_message_to_client_exception_message_not_str_but_tuple(self):
        self.temp.sendMessageToClient = MagicMock(side_effect=Exception("Client must be str"))
        with self.assertRaisesRegex(Exception, "Client must be str"):
            self.temp.sendMessageToClient("Client", ())

    def test_send_message_to_client_exception_message_not_str_but_list(self):
        self.temp.sendMessageToClient = MagicMock(side_effect=Exception("Client must be str"))
        with self.assertRaisesRegex(Exception, "Client must be str"):
            self.temp.sendMessageToClient("Client", [])

    def test_send_message_to_client_exception_message_not_str_but_dict(self):
        self.temp.sendMessageToClient = MagicMock(side_effect=Exception("Client must be str"))
        with self.assertRaisesRegex(Exception, "Client must be str"):
            self.temp.sendMessageToClient("Client", {})
    
    def test_send_message_to_client_value_error(self):
        self.temp.sendMessageToClient = MagicMock(side_effect=Exception("Client not in client list"))
        with self.assertRaisesRegex(Exception, "Client not in client list"):
            self.temp.sendMessageToClient("Client2132", "Hello")

    def tearDown(self):
        self.temp = None
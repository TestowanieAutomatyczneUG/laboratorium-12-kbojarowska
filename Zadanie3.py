import unittest
from unittest.mock import *

class Messenger:
    def __init__(self):
        self.TemplateEngine = TemplateEngine()
        self.MailServer = MailServer()

    def sendMessage(self, receiver, message):
        return self.MailServer.sendMessage(receiver, self.TemplateEngine.create(message))

    def receiveMessage(self):
        return self.MailServer.receiveMessage()

class TemplateEngine:
    def create(self, message):
        pass

class MailServer :
    def sendMessage(self, receiver, message):
        pass
    
    def receiveMessage(self):
        pass

class TestMessenger(unittest.TestCase):
    def setUp(self):
        self.temp = Messenger()

    def test_send_message(self):
        self.temp.TemplateEngine = MagicMock()
        self.temp.MailServer = MagicMock()
        self.temp.TemplateEngine.create.side_effect = "Hello"
        self.temp.MailServer.sendMessage.return_value = True
        self.assertTrue(self.temp.sendMessage("Client", "Hello"))

    def test_send_message_not_send(self):
        self.temp.TemplateEngine = MagicMock()
        self.temp.MailServer = MagicMock()
        self.temp.TemplateEngine.create.side_effect = "Hello"
        self.temp.MailServer.sendMessage.return_value = False
        self.assertFalse(self.temp.sendMessage("Client", "Hello"))

    def test_send_message_not_send_receiver_not_str_but_int(self):
        self.temp.TemplateEngine = MagicMock()
        self.temp.MailServer = MagicMock()
        self.temp.TemplateEngine.create.side_effect = "Hello"
        self.temp.MailServer.sendMessage.side_effect = Exception("Client must be str")
        with self.assertRaisesRegex(Exception, "Client must be str"):
            self.temp.sendMessage(4, "Hello")

    def test_send_message_not_send_receiver_not_str_but_list(self):
        self.temp.TemplateEngine = MagicMock()
        self.temp.MailServer = MagicMock()
        self.temp.TemplateEngine.create.side_effect = "Hello"
        self.temp.MailServer.sendMessage.side_effect = Exception("Client must be str")
        with self.assertRaisesRegex(Exception, "Client must be str"):
            self.temp.sendMessage([], "Hello")

    def test_send_message_not_send_receiver_not_str_but_dict(self):
        self.temp.TemplateEngine = MagicMock()
        self.temp.MailServer = MagicMock()
        self.temp.TemplateEngine.create.side_effect = "Hello"
        self.temp.MailServer.sendMessage.side_effect = Exception("Client must be str")
        with self.assertRaisesRegex(Exception, "Client must be str"):
            self.temp.sendMessage({}, "Hello")

    def test_send_message_not_send_receiver_not_str_but_float(self):
        self.temp.TemplateEngine = MagicMock()
        self.temp.MailServer = MagicMock()
        self.temp.TemplateEngine.create.side_effect = "Hello"
        self.temp.MailServer.sendMessage.side_effect = Exception("Client must be str")
        with self.assertRaisesRegex(Exception, "Client must be str"):
            self.temp.sendMessage(4.423, "Hello")

    def test_send_message_not_send_receiver_not_str_but_tuple(self):
        self.temp.TemplateEngine = MagicMock()
        self.temp.MailServer = MagicMock()
        self.temp.TemplateEngine.create.side_effect = "Hello"
        self.temp.MailServer.sendMessage.side_effect = Exception("Client must be str")
        with self.assertRaisesRegex(Exception, "Client must be str"):
            self.temp.sendMessage((), "Hello")

    def test_send_message_not_send_message_not_str_but_int(self):
        self.temp.TemplateEngine = MagicMock()
        self.temp.MailServer = MagicMock()
        self.temp.TemplateEngine.create.side_effect = "Hello"
        self.temp.MailServer.sendMessage.side_effect = Exception("Message must be str")
        with self.assertRaisesRegex(Exception, "Message must be str"):
            self.temp.sendMessage("Client", 4)

    def test_send_message_not_send_message_not_str_but_float(self):
        self.temp.TemplateEngine = MagicMock()
        self.temp.MailServer = MagicMock()
        self.temp.TemplateEngine.create.side_effect = "Hello"
        self.temp.MailServer.sendMessage.side_effect = Exception("Message must be str")
        with self.assertRaisesRegex(Exception, "Message must be str"):
            self.temp.sendMessage("Client", 4.432)

    def test_send_message_not_send_message_not_str_but_list(self):
        self.temp.TemplateEngine = MagicMock()
        self.temp.MailServer = MagicMock()
        self.temp.TemplateEngine.create.side_effect = "Hello"
        self.temp.MailServer.sendMessage.side_effect = Exception("Message must be str")
        with self.assertRaisesRegex(Exception, "Message must be str"):
            self.temp.sendMessage("Client", [])

    def test_send_message_not_send_message_not_str_but_dict(self):
        self.temp.TemplateEngine = MagicMock()
        self.temp.MailServer = MagicMock()
        self.temp.TemplateEngine.create.side_effect = "Hello"
        self.temp.MailServer.sendMessage.side_effect = Exception("Message must be str")
        with self.assertRaisesRegex(Exception, "Message must be str"):
            self.temp.sendMessage("Client", {})

    def test_send_message_not_send_message_not_str_but_tuple(self):
        self.temp.TemplateEngine = MagicMock()
        self.temp.MailServer = MagicMock()
        self.temp.TemplateEngine.create.side_effect = "Hello"
        self.temp.MailServer.sendMessage.side_effect = Exception("Message must be str")
        with self.assertRaisesRegex(Exception, "Message must be str"):
            self.temp.sendMessage("Client", {})

    def test_receiveMessage(self):
        self.temp.MailServer = MagicMock()
        self.temp.MailServer.receiveMessage.return_value = "Hello"
        self.assertEqual("Hello", self.temp.receiveMessage())

    def test_receiveMessage_message_not_received(self):
        self.temp.MailServer = MagicMock()
        self.temp.MailServer.receiveMessage.return_value = False
        self.assertFalse(self.temp.receiveMessage())
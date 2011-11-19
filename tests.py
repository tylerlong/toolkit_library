# coding=utf-8
"""
    toolkit_library.tests
    ~~~~~~~~~~~~~~~~~~~~~
    Unit tests for code quality.
"""
import unittest


from toolkit_library.mail_server import MailServer
class MailServerTestCase(unittest.TestCase):
    """Test mail_server.py"""

    def setUp(self):
        """Initiate the smtp mail server"""
        self.server = MailServer(host = 'smtp.gmail.com', port = 587, tls = True, account = 'wendaren.service@gmail.com', password = 'wendaren123')

    def test_send_mail(self):
        """send an email"""
        with self.server:
            self.server.send_mail('tyler4long@gmail.com', 'unittest of python', 'greetings from unittest of python')


from toolkit_library.encryption import Encryption
class EncryptionTestCase(unittest.TestCase):
    """Test encryption.py"""

    def setUp(self):
        self.password = '123456'

    def test_generate_password(self):
        """Ensure generated salt and password could authenticate the original password"""
        hashcode, salt = Encryption.generate_hashcode_and_salt(self.password)
        assert Encryption.check_password(self.password, hashcode, salt)

    def test_different_hashcode(self):
        """Ensure everytime a different hashcode is generated. This is for preventing Rainbow-tables cracking"""
        hashcode1 = Encryption.generate_hashcode_and_salt(self.password)[0]
        hashcode2 = Encryption.generate_hashcode_and_salt(self.password)[0]
        assert hashcode1 != hashcode2


def greetings(a, b = 'default b'):
    print 'hello', a
    print 'hello', b
import sys
from toolkit_library.inspector import ModuleInspector
class InspectorTestCase(unittest.TestCase):
    """Test inspector.py"""
    def test_invoke(self):
        """method invoking using inspector"""
        inspector = ModuleInspector(sys.modules[__name__])
        inspector.invoke()
        inspector.invoke('greetings')
        inspector.invoke('greetings', 'aaa')
        inspector.invoke('greetings', 'aaa', 'bbb')
        inspector.invoke(None, 'aaa')
        inspector.invoke(None, 'aaa', 'bbb')
        inspector.invoke(None, 'aaa', 'bbb', 'ccc')


from toolkit_library.string_util import StringUtil
class StringUtilTestCase(unittest.TestCase):
    """test string_util.py"""
    def test_camelcase_to_underscore(self):
        """convert camel case to underscore"""
        assert StringUtil.camelcase_to_underscore('StringUtilTestCase') == 'string_util_test_case'
        assert StringUtil.camelcase_to_underscore('ModelQuestion') == 'model_question'

    def test_html_br_and_p(self):
        """Break text into HTML line breaks and paragraphs"""
        assert StringUtil.html_br_and_p('aaa\nbbb') == '<p>aaa<br/>\nbbb</p>'
        assert StringUtil.html_br_and_p('aaa\n\nbbb') == '<p>aaa</p>\n\n<p>bbb</p>'


def default_test_suite():
    """Which test cases to test"""
    suite = unittest.TestSuite()
    #suite.addTest(unittest.makeSuite(MailServerTestCase))
    #suite.addTest(unittest.makeSuite(InspectorTestCase))
    suite.addTest(unittest.makeSuite(EncryptionTestCase))
    suite.addTest(unittest.makeSuite(StringUtilTestCase))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest = 'default_test_suite')

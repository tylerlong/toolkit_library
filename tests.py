# coding=utf-8
"""
    tests
    ~~~~~
    Unit tests for code quality.
"""
import unittest


from toolkit_library.mail_server import MailServer
class MailServerTestCase(unittest.TestCase):
    """Test mail_server.py"""

    def setUp(self):
        """Initiate the smtp mail server"""
        self.server = MailServer(host = 'smtp.gmail.com', port = 587, tls = True, account = 'toolkit.library.feedback@gmail.com', password = 'password')

    def test_send_mail(self):
        """send an email"""
        with self.server:
            self.server.send_mail('toolkit.library.feedback@gmail.com', 'toolkit_library mail_server', 'This message is sent via toolkit_library.mail_server')


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


from toolkit_library.text_converter import TextConverter
class TextConverterTestCase(unittest.TestCase):
    """test text_converter.py"""
    def test_text_to_html(self):
        """Break text into HTML line breaks and paragraphs"""
        assert TextConverter.text_to_html('aaa\nbbb') == '<p>aaa<br/>\nbbb</p>'
        assert TextConverter.text_to_html('aaa\n\nbbb') == '<p>aaa</p>\n\n<p>bbb</p>'
        assert TextConverter.text_to_html('aaa\n\n\n\nbbb') == '<p>aaa</p>\n\n<p>bbb</p>'

    def test_html_to_text(self):
        """Convert html source code to text, like you copy the text from a browser"""
        assert TextConverter.html_to_text('<p>aaa<br/>\nbbb</p>') == '\naaa\n bbb\n'
        assert TextConverter.html_to_text('<div>aaa<br/>\nbbb</div>') == 'aaa\n bbb\n'
        assert TextConverter.html_to_text('<div>aaa\n\n\n\nbbb</div>') == 'aaa bbb\n'


def default_test_suite():
    """Which test cases to test"""
    suite = unittest.TestSuite()
    #suite.addTest(unittest.makeSuite(MailServerTestCase))
    #suite.addTest(unittest.makeSuite(InspectorTestCase))
    suite.addTest(unittest.makeSuite(EncryptionTestCase))
    suite.addTest(unittest.makeSuite(StringUtilTestCase))
    suite.addTest(unittest.makeSuite(TextConverterTestCase))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest = 'default_test_suite')

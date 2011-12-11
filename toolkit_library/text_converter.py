"""
    toolkit_library.text_converter
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Convert text from one format to another
"""
import re
from HTMLParser import HTMLParser


class TextConverter(object):
    @staticmethod
    def html_to_text(html):
        """Convert html to text"""
        parser = MyHTMLParser()
        parser.feed(html)
        parser.close()
        return parser.text()

    
    paragrap_pattern = re.compile(ur'(?:\r\n|\r|\n){2,}')
    line_break_pattern = re.compile(ur'(?:\r\n|\r|\n)')
    @staticmethod
    def text_to_html(text):
        """Convert text to html"""
        if isinstance(text, unicode):
            text = text.encode('utf-8')
        result = '\n\n'.join('<p>{0}</p>'.format('<br/>\n'.join(TextConverter.line_break_pattern.split(paragraph))) for paragraph in TextConverter.paragrap_pattern.split(text))
        return result.decode('utf-8')


blank_pattern = re.compile(ur'\s+')
class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.tokens = []

    def handle_data(self, data):
        self.tokens.append(blank_pattern.sub(' ', data))

    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.tokens.append('\n')

    def handle_endtag(self, tag):
        if tag == 'p' or tag == 'div':
            self.tokens.append('\n')


    def handle_startendtag(self, tag, attrs):
        if tag == 'br':
            self.tokens.append('\n')

    def text(self):
        return ''.join(self.tokens)

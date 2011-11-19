"""
    toolkit_library.string_util
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Utilities to deal with strings
"""
import re

class StringUtil(object):
    """Methods in this class are all static methods. Deal with strings."""

    first_cap_pattern = re.compile('(.)([A-Z][a-z]+)')
    all_cap_pattern = re.compile('([a-z0-9])([A-Z])')
    @staticmethod
    def camelcase_to_underscore(name):
        """Convert CamelCase to camel_case"""
        temp = StringUtil.first_cap_pattern.sub(r'\1_\2', name)
        return StringUtil.all_cap_pattern.sub(r'\1_\2', temp).lower()

    
    paragrap_pattern = re.compile(ur'(?:\r\n|\r|\n){2,}')
    line_break_pattern = re.compile(ur'(?:\r\n|\r|\n)')
    @staticmethod
    def html_br_and_p(text):
        """Break text into HTML line breaks and paragraphs
        Parameter text should be unicode or utf-8 str
        Returns unicode
        """
        if isinstance(text, unicode):
            text = text.encode('utf-8')
        result = '\n\n'.join('<p>{0}</p>'.format('<br/>\n'.join(StringUtil.line_break_pattern.split(paragraph))) for paragraph in StringUtil.paragrap_pattern.split(text))
        return result.decode('utf-8')

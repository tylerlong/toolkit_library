"""
    toolkit_library.string_util
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Utilities to deal with strings
"""
import re

class StringUtil(object):
    """Methods in this class are all static methods. Deal with strings."""

    first_cap_pattern = re.compile(ur'(.)([A-Z][a-z]+)')
    all_cap_pattern = re.compile(ur'([a-z0-9])([A-Z])')
    @staticmethod
    def camelcase_to_underscore(name):
        """Convert CamelCase to camel_case"""
        temp = StringUtil.first_cap_pattern.sub(r'\1_\2', name)
        return StringUtil.all_cap_pattern.sub(r'\1_\2', temp).lower()

    trim_pattern = re.compile("^\W+|\W+$|['`]")
    and_pattern = re.compile('\s*&\s*')
    at_pattern = re.compile('\s*@\s*')
    hyphen_pattern = re.compile('\W+')
    @staticmethod
    def slugify(s, max_length = 80):
        """create slug which could be used in url for a string"""
        s = StringUtil.trim_pattern.sub('', s.lower())
        s = s[0:max_length]
        s = StringUtil.and_pattern.sub('-and-', s)
        s = StringUtil.at_pattern.sub('-at-', s)
        s = StringUtil.hyphen_pattern.sub('-', s)
        return s
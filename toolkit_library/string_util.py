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

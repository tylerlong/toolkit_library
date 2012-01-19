# coding=utf-8
"""
    toolkit_library.input_util
    ~~~~~~~~~~~~~~~~~~~~~~~~~~
    get inputs from user and validate them 
"""
import re


class InputUtil(object):
    """get inputs from user and validate them"""

    @staticmethod
    def get_input(name, default = None, pattern = None):
        """get inputs from user and validate them
        If user enters empty and default value is not None, default value will be returned.
        if user enters non-empty and pattern is not None, user input should match the regex pattern.
        Otherwise user will be prompt to enter again.
        """
        assert type(name) == str and len(name) > 0
        prompt = name
        if pattern is not None:
            prompt = '{0} ({1})'.format(prompt, pattern)
        if default is not None:
            prompt = '{0} [{1}]'.format(prompt, default)
        prompt = 'Please enter {0}: '.format(prompt)

        while True:
            result = raw_input(prompt)
            if not result:
                if default is not None:
                    return default
                else:
                    print 'Please enter sth, as there is no default value available.'
            else:
                if pattern is None:
                    return result
                else:
                    if re.match(pattern, result):
                        return result
                    else:
                        print 'What you just entered is not valid, please try again.'

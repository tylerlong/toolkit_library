# coding=utf-8
"""
    toolkit_library.web_client
    ~~~~~~~~~~~~~~~~~~~~~~~~~~
    Web client for fetching web resources.
"""
import urllib2

class WebClient(object):
    """web client for fetching web resources."""

    @staticmethod
    def download_binary(url):
        """dowload web resources in binary format"""
        socket = urllib2.urlopen(url)
        data = socket.read()
        socket.close()
        return data

# coding=utf-8
"""
    toolkit_library.web_client
    ~~~~~~~~~~~~~~~~~~~~~~~~~~
    Web client for fetching web resources.
"""
import urllib2, contextlib

class HeadRequest(urllib2.Request):
    def get_method(self):
        return 'HEAD'

class WebClient(object):
    """web client for fetching web resources."""

    @staticmethod
    def download_binary(url):
        """dowload web resources in binary format"""
        with contextlib.closing(urllib2.urlopen(url)) as socket:
            return socket.read()

    @staticmethod
    def head(url):
        """http HEAD request"""
        with contextlib.closing(urllib2.urlopen(HeadRequest(url))) as socket:
            return socket.info()
# coding=utf-8
"""
    toolkit_library.mail_server
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Connect to a SMTP server and send email
"""
import smtplib
from email.mime.text import MIMEText


class MailServer(object):
    """Mail server, or smtp server in particular
    Example usage:
        server = MailServer(host = 'localhost', port = 25, tls = False, account = 'username', password = 'password')
        with server:
            server.send_mail('test@localhost', 'subject', 'content')
            server.send_mail('test@localhost', 'subject2', 'content2')
    """

    def __enter__(self):
        """Connect to mail server"""
        self.connect()
        return self

    def __exit__(self, type, value, traceback):
        """Disconnect from mail server"""
        self.disconnect()
    
    required_options = { #must provide these options when initialize MailServer
        'host': 'host name of the smtp server', 
        'port': 'running port of the smtp server', 
        'tls': 'does the smtp server use tls? True or False', 
        'account': 'login account to the smtp server', 
        'password': 'password to login the smtp server'
    }

    def __init__(self, **options):
        """**options should contain all of the fields in required_options"""
        for option in MailServer.required_options:
            if not option in options:
                raise ValueError('missing option: "%s: %s"' % (option, MailServer.required_options[option]))
        self.options = options

    def connect(self):
        """Connect to remote smtp server"""
        self.server = smtplib.SMTP(self.options['host'], self.options['port'])
        self.server.ehlo_or_helo_if_needed()
        if(self.options['tls']):
            self.server.starttls()
        self.server.login(self.options['account'], self.options['password'])

    def send_mail(self, to, subject, content):
        """Send email"""
        message = MIMEText(content.encode('utf-8'), _charset='utf-8')
        message['From'] = self.options['account']
        message['To'] = to
        message['Subject'] = subject
        self.server.sendmail(self.options['account'], to, message.as_string())

    def disconnect(self):
        """Disconnect from remote smtp server"""
        self.server.quit()

# encoding: utf-8

'''zone_check

A wrapper around 'named-checkzone' for checking the validity and syntax of zone files.

Example::

    >>> from easyzone.zone_check import ZoneCheck
    >>> c = ZoneCheck()
    >>> c.isValid('example.com', '/var/named/zones/example.com')
    True
    >>> c.isValid('foo.com', '/var/named/zones/example.com')
    False
    >>> c.error
    'Bad syntax'
    >>> 
    >>> c = ZoneCheck(checkzone='/usr/sbin/named-checkzone')
    >>> c.isValid('example.com', '/var/named/zones/example.com')
    True
    >>>
'''

__author__ = 'Chris Miles'
__copyright__ = '(c) Chris Miles 2007'
__id__ = '$Id: zone_check.py 800 2008-04-24 14:59:25Z chris $'
__url__ = '$URL: https://hugo.thoh.net/svn/psychofx/Projects/Python/easyzone/trunk/easyzone/zone_check.py $'
__version__ = '1.0'


# ---- Imports ----

# - Python Modules -
import subprocess


# ---- Exceptions ----


# ---- Classes ----

class ZoneCheck(object):
    '''A wrapper around bind's named-checkzone utility, used for checking the
    syntax of a zone file.
    
    `checkzone` : string containing path to named-checkzone binary.  Or leave
    as "named-checkzone" to search with default PATH.
    '''
    def __init__(self, checkzone='checkzone'):
        self.checkzone = checkzone
        self.error = None
    
    def isValid(self, zonename, filename):
        '''Ask named to check the syntax of a zone file by calling the
        named-checkzone commmand.
        '''
        cmd = [
            self.checkzone,
            '-q',
            zonename,
            filename
        ]
        
        r = subprocess.call(cmd)
        
        if r != 0:
            self.error = 'Bad syntax'
            return False
        
        else:
            self.error = None
            return True
    


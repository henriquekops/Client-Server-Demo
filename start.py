#METADATA
__author__ = [
    'Henrique Kops', 
    'José Goulart', 
    'João Vieira', 
    'João Etchichury',
    'Carlo José'
]
__date__ = '2019-08-30'
__version__ = '1.0'

# project dependencies
from server.handler import ServerPort


if __name__ == '__main__':
    # SERVER STARTUP (WSGI)
    ServerPort().startup()
    
    
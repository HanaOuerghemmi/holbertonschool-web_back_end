#!/usr/bin/env python3
"""
define a _hash_password method
"""
from bcrypt import hashpw, gensalt

def _hash_password(password: str) -> str:
    """ 
    Returns a salted hash of the input password 
    """
    return hashpw(password.encode('utf-8'), gensalt())

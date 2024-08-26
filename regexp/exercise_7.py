"""
check mail.address
"""

import re

def check_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9](-?[a-zA-Z0-9_\.]){5,31}@[a-zA-Z0-9]+(\.[a-zA-Z0-9]+){2}$'
    if re.match(pattern, email):
        return True
    else:
        return False

print(check_email('oleh.rad4enko@gmail.com.ua'))




"""

"""
res = r'^Rb+r$' # Rbbbbbbbr
res = r'^\d{4}\-\d{4}\-\d{4}\-\d{3}$'
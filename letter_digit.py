
import re

def letterAndDigit(s):
    if s is None or len(s) == 0 or not isinstance(s,str):
        return False
    return {'DIGITS':len([i for i in s if re.match('\d', i)]),'LETTERS':len([i for i in s if re.match('[A-Za-z]', i)])}

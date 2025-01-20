"""
>>> import timeutil
>>> timeutil.validate("112 a.m.")  #Envoke line 8&9 No colon in sting time
False
>>> timeutil.validate("zz:00") # Envoke line 12&13 hour is not a digit
False
>>> timeutil.validate("09:59 a.m.") # Envoke line 16&17 int(hour[0])== 0
False
>>> timeutil.validate("12:11 mor")  # Envoke line sufix is not a.m and is not p.m.
False
>>> timeutil.validate("11:2344 a.m.") # Envoke line 24&25 len(minutes)> 2
False
>>> timeutil.validate("12:59 a.m.")  # Envoke line 29 all coditions are true
True

"""

import doctest
doctest.testmod(verbose=True)

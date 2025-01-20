#testnumberuntil
"""
>>> import numberutil
>>> numberutil.aswords(0) # n = 0
'zero'
>>> numberutil.aswords(7) # envoke lines 16 & 17, 0<n<21
'seven'
>>> numberutil.aswords(23) # envoke lines 16, then lines 19
'twenty three'
>>> numberutil.aswords(50) # envoke lines
'fifty'
>>> numberutil.aswords(100) # envoke lines
'one hundred'
>>> numberutil.aswords(107) # envoke lines
'one hundred and seven'
>>> numberutil.aswords(240) #envoke lines
'two hundred and forty'
>>> numberutil.aswords(342)# envoke lines
'three hundred and forty two'

"""

import doctest
doctest.testmod(verbose=True)
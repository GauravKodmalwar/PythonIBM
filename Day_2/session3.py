from globalP.CONSTANTS import *
#from globalP.CONSTANTS import multiArguments, multiArguments2
from globalP import *
import globalP.CONSTANTS

addition()
_multiArguments()

print(CONSTANTS._PI)
print(CONSTANTS._multiArguments("Hi ", "How are you?", " Had a good lunch"))
print(CONSTANTS._multiArguments2(var1 = "Hi ", var2 = "How are you?", var3 = " Had a good lunch"))

import sys
print(sys.path)
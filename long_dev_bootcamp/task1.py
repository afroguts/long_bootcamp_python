lst = list(range(0,101)) # we can do it without the list in the new version of python

import time
for x in lst:

    if x % 2 == 0: 

        print (x)

        time.sleep(3)  #delaying time 
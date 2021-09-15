from probables import (CuckooFilter)
from probables import (CountingCuckooFilter)
cko = CuckooFilter(capacity=100, max_swaps=10)
cko.add('google.com')
cko.check('facebook.com')  # should return False
cko.check('google.com')  # should return True

cck = CountingCuckooFilter(capacity=100, max_swaps=10)
cck.add("google")
cck.add("google")
cck.add("google")
print(cck.check("google"))
cck.remove("google")
print(cck.check("google"))

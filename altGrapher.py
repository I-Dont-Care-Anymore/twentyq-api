import pandas as pd
import matplotlib.pyplot as plt

f = plt.figure()
plt.plot(range(7), columns = ['2007', '2008', '2009', '2010', '2011', '2012', '2013'])
plt.show()

f.savefig("foo.html", bbox_inches='tight')



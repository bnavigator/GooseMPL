import numpy             as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

plt.style.use(['goose', 'goose-latex'])

x = np.linspace(0,10,101)
y = x**2.

fig, ax = plt.subplots()

ax.plot(x, y)

ax.yaxis.set_major_formatter(ticker.StrMethodFormatter(r'${x:.1e}$'))

plt.savefig('tick-formatter.svg')
plt.show()


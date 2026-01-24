import numpy as np
from tabulate import tabulate

twopi = 2*np.pi

x = np.linspace(0, twopi, 1000)
y = np.sin(x)

data = [(a, b) for a, b in zip(x, y)]
headers = ["x", "sin(x)"]

table = tabulate(data, tablefmt="grid", headers=headers, floatfmt=".3f")

def main():
	print(table)

if __name__ == '__main__':
	main()
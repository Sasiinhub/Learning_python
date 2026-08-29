import matplotlib.pyplot as plt

fruits = ['banana','quava', 'papaya','mango','neem','karai']
rate = [30,40,100,120,0,0]

plt.bar(fruits, rate, color = 'yellow')

plt.title("Fruits rate")
plt.xlabel('Fruits')
plt.ylabel('Rate')


plt.show()

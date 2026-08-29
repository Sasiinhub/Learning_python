# https://www.geogebra.org/math/diagrams#upper-elementary
# awesome interactive graphs available on this site..


import matplotlib.pyplot as plt

# Define data
fruits = ['Apples', 'Bananas', 'Cherries', 'Dates']
sales = [400, 350, 300, 450]

# Create vertical bar chart
plt.bar(fruits, sales, color='skyblue')

# Add labels and title
plt.title('Fruit Sales Overview')
plt.xlabel('Fruits')
plt.ylabel('Sales (Units)')

# Display the chart
plt.show()

'''
fruits = ['Apples', 'Bananas', 'Cherries', 'Dates']
sales = [400, 350, 300, 450]

# Create horizontal bar chart
plt.barh(fruits, sales, color='salmon')

plt.title('Fruit Sales Overview')
plt.xlabel('Sales (Units)')
plt.ylabel('Fruits')

plt.show()

'''


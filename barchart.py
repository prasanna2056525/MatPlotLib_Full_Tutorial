import matplotlib.pyplot as plt 

product = ['A', "B", 'C', "D"]
sales = [1000,800,500,1500]

plt.hbar(product,sales, color= 'Blue', label="sales 2026")
plt.xlabel('Product')
plt.ylabel("Total sales")
plt.title("Sales of Product in 2026")
plt.legend()

plt.show()
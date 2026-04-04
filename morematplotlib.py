import matplotlib.pyplot as plt 

month = [1,2,3,4,5]
sales = [100,500,1300,1800,300]

plt.plot( month, sales, color='blue', linestyle='--', linewidth = 2, marker='o', label='2025 sales data of first five month')
plt.xlabel('Months')
plt.ylabel('Total Sales')
plt.title('Monthly sales Data')
plt.legend(loc='upper left', fontsize=12)
plt.grid( color='grey', linestyle=':',linewidth=1)
plt.xlim(0,6)
plt.ylim(0,2000)
plt.xticks([1,2,3,4,5],['m1','m2','m3','m4','m5'])
plt.show()
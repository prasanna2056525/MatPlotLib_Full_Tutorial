import matplotlib.pyplot as plt 

hours_std = [1,2,3,4,5,6,7,8]
marks = [ 50,55,60,65,70,75,80,85]

plt.scatter( hours_std,marks, color="green", marker='o', label="Student Data")

plt.xlabel('Hours Studied')
plt.ylabel("Gained Marks")
plt.title('Marks Accn to Study Hours')
plt.legend()
plt.grid(True)
plt.show()

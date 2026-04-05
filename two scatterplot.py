import matplotlib.pyplot as plt 

hours_std = [1,2,3,4,5,6,7,8]
marks1= [ 50,55,60,65,70,75,80,85]
marks2 = [52,58,61,67,73,79,81,88]

plt.scatter( hours_std,marks1, color="green", marker='^gi', label="Student Data Group 1")
plt.scatter( hours_std,marks2, color="red", marker='o', label="Student Data Group 2")

plt.xlabel('Hours Studied')
plt.ylabel("Gained Marks")
plt.title(' Comparision of two group students accn to marks and hours')
plt.legend()
plt.grid(True)
plt.show()
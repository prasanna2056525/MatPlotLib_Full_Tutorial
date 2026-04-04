import matplotlib.pyplot as plt 

scores = [45,54,58,67,77,89,95,90,40,85,66,81,99,49,88,72,64,94]

plt.hist(scores, bins=6, color="blue" , edgecolor ="Black")

plt.xlabel("Scores Range")
plt.ylabel ('Number of Student')
plt.title('Score Distribution of Scores')
plt.show()
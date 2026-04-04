import matplotlib.pyplot as plt 

regions =['Pokhara','Kathmandu','Jhapa','Chitwan']

revenue =[ 1000,2500,800,1800]
plt.pie( revenue, labels=regions, autopct='%1.1f%%', colors=['Green','purple','Orange','Grey'])

plt.title("Revenues from top 4 City of Nepal")

plt.show()
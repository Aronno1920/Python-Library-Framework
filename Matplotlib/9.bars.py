import matplotlib.pyplot as plt

name = ['Sanaya', 'Ahmed', 'Aairah', 'Selim', 'Afsara']
age = [5,6,10,37,29]

# plt.bar(name,age)
# plt.xlabel('Name')
# plt.ylabel('Age')
# plt.title("Bar Plot")
# plt.show()

plt.bar(name,age, color=['red','green','blue','grey','black'])
plt.xlabel('Name')
plt.ylabel('Age')
plt.title("Customize Bar Plot")
plt.show()
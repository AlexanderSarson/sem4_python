import matplotlib.pyplot as plt

x = ['Maths', 'Physics', 'Chemistry']

y1 = [95, 88, 45]


plt.plot(x, y1, label="John")

y2 = [67, 45, 56]


plt.plot(x, y2, label="David")


y3 = [28, 67, 90]

plt.plot(x, y3, label="Tom")

plt.xlabel('Subjects')
plt.ylabel('Marks')

plt.title('Three lines on same graph!')

plt.legend()

plt.show()

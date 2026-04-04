import matplotlib.pyplot as plt
import numpy as np
 
# --- 1. Line Chart ---
x = [1, 2, 3, 4, 5]
y = [10, 25, 15, 40, 30]
 
plt.subplot(2, 2, 1)
plt.plot(x, y, color='blue', marker='o')
plt.title('Line Chart')
plt.xlabel('X'); plt.ylabel('Y')
 
# --- 2. Bar Chart ---
subjects = ['Maths', 'Science', 'English']
marks    = [85, 90, 78]
 
plt.subplot(2, 2, 2)
plt.bar(subjects, marks, color=['red', 'green', 'blue'])
plt.title('Bar Chart')
plt.ylabel('Marks')
 
# --- 3. Pie Chart ---
items  = ['Food', 'Transport', 'Savings']
values = [40, 30, 30]
 
plt.subplot(2, 2, 3)
plt.pie(values, labels=items, autopct='%1.1f%%')
plt.title('Pie Chart')
 
# --- 4. Scatter Plot ---
hours = np.random.randint(1, 10, 20)
score = hours * 8 + np.random.randint(-5, 5, 20)
 
plt.subplot(2, 2, 4)
plt.scatter(hours, score, color='green')
plt.title('Scatter Plot')
plt.xlabel('Hours'); plt.ylabel('Score')
 
plt.tight_layout()
plt.show()
 

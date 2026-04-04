import matplotlib.pyplot as plt

x=[1,2,3,4]
y=[20,40,60,90]

categories=['A','B','C','D']
values=[1,3,5,7]

labels=['CARS','BIKES','CYCLES','LORRIES']
count=[23,17,15,26]    

#Subplot Layout
plt.figure(figsize=(10,8))

#1.Line plot
plt.subplot(2,2,1)
plt.plot(x,y,marker='o',color='blue')
plt.title("Line Plot")

#2.Bar Chart
plt.subplot(2,2,2)
plt.bar(categories,values,color='green')
plt.title("Bar Chart")

#3.Scatter Plot
plt.subplot(2,2,3)
plt.scatter(x,y,color='m',alpha=0.5)
plt.title("Scatter Plot")

#4.Pie Chart
plt.subplot(2,2,4)
plt.pie(count,labels=labels,autopct='%1.1f%%')
plt.title("Pie chart")

plt.tight_layout()

#Show all plots
plt.show()



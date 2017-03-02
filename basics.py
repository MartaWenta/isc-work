import matplotlib.pyplot as plt
times = range(7)
co2conc = [250, 265, 272, 260, 300, 320, 389]
temp = [14.1, 15.5, 16.3, 18.1, 17.3, 19.1, 20.2] 
plt.plot(times, co2conc, 'r',
        times, temp, 'g--')
plt.title('exercise 2')
plt.xlabel('times')
plt.ylabel('conc')
plt.show()


 


    

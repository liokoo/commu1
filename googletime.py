import requests
import matplotlib.pyplot as plt
times=[]
for _ in range(10):
    r = requests.get('http://www.google.com')
    times.append(r.elapsed.microseconds/1000)
print('Minimum response time:', min(times))
print('Average response time:', sum(times)/len(times))
print('Minimum response time:', max(times))

plt.figure()
plt.plot(times)
plt.ylim([0,1.1*max(times)])
plt.xlabel('ID requested')
plt.ylabel('[ms]')
plt.title('Test http://www.google.com')
plt.grid()
plt.show()

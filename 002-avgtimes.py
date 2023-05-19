import requests

def average(stat):
    avg=sum(stat)/len(stat)
    return avg
    
sites =['http://www.google.com', 'http://www.youtube.com', 'http://www.wikipedia.org', 'http://www.polimi.it', 'http://www.amazon.com', 'http://www.twitter.com']
avg=[]

for url in sites:
    print('Test:', url)
    times=[]
    for _ in range(10):
        r=requests.get(url)
        times.append(r.elapsed.microseconds/1000)
    average_time=average(times)
    print('Avg:', average_time)
    avg.append(average_time)
print(sites[avg.index(min(avg))], min(avg))

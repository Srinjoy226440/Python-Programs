print("Enter the 5 cities and their geographical co-ordinates: ")
for i in range(0,5):
    t1=tuple(input().split(","))
    lat,lon=map(float,input().split())
    location=(lat,lon)
d=dict(zip(t1,location))
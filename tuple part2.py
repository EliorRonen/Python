Weather = (0,1,0,1,1,0,1)

for item in range(0,10):
    sunny = 0
    rainy = 0
if Weather[item == 1]:
    rainy += 1
else:
    sunny += 1
if sunny>rainy:
    print("it's a good weather today")
else:
    print("the weather's bad today")
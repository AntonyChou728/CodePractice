warm = ['red', 'yellow', 'orange']
hot  = warm
hot.append('pink')
print(warm)
print(hot)

cold = ['blue', 'white', 'black']
chill  = list(cold)
chill.append('green')
print(cold)
print(chill)

print('---')

warm = ['red', 'yellow', 'orange']
sortedwarm = warm.sort()
print(warm)
print(sortedwarm)

cold = ['blue', 'white', 'black']
sortedcold = sorted(cold)
print(cold)
print(sortedcold)
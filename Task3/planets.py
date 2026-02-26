masses = [1.9891e+30, 1.8986e+27, 
          5.6846e+26, 1.0243e+26, 8.6810e+25,
          5.9736e+24, 4.8685e+24, 6.4185e+23, 
          3.3022e+23, 7.349e+22, 1.25e22]
pit= []
for i in masses:
    print(i)
    if i <= (7.349e+22):
        continue
    pit.append(i)

print(pit)
pot = masses[6:11]
print(pot)

avg = (sum(pot)/len(pot))
print(avg)
    

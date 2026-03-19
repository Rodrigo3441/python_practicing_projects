students = [
    ["Alice", 8.5, 7.0, 9.0],
    ["Bob", 6.0, 5.5, 6.5],
    ["Carol", 4.0, 5.0, 4.5],
    ["Dave", 9.0, 9.5, 10.0]
]

results = []

#extract individually grades and names
for name, g1, g2, g3 in students:
    avg = round((g1+g2+g3)/3,2)

    if avg >= 7:
        status = 'Approved'
    elif avg >= 5 and avg < 7:
        status = 'Recovery'
    else:
        status = 'Failed'

    #print and append into results list
    print(name,'|', avg,'|', status)
    results.append([name,avg,status])

#take one student 
name, avg, status = results[0]

print('Name:', name)
print('Average:', avg)
print('Status:', status)

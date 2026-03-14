employee_data={
    'Abhinav':2000,
    'Abin':100000,
    'Johan':500000,
    'Jaison':25000,
    }
print("The employees earning more than 50000 are:")
for name in employee_data:
    salary=employee_data[name]
    if salary>50000:
        print(name)

employee_data={
    'Abhinav':25000,
    'Abin':10000,
    'Johan':5000,
    'Jaison':25000,
    }
print("The employees earning more than 10000 are:")
for name in employee_data:
    salary=employee_data[name]
    if salary>10000:
        print(name)

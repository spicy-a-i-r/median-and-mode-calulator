data =[]

def add_data():
    amount_of_data = int(input("how many data groups are there? "))

    for i in range(amount_of_data):
        value = int(input("what's the value "))
        frequency = int((input("whats the frequency ")))
        for i in range(frequency):
            data.append(value)
            
        print(f"{value} added")


def clean(data):
    sorted_data = sorted(data)
    return sorted_data

def find_middle(data):

    clean_data = clean(data)

    n = 0
    total = 0

    for i in range(len(clean_data)):
        total += clean_data[i] 
        n += 1
    
    mean = total / n

    if len(clean_data) % 2 == 0:
        half = n // 2
        n1 = clean_data[half - 1]
        n2 = clean_data[half]
        median = (n1 + n2) / 2
    else:
        median = clean_data[n // 2]
    return (f"mean: {mean}, median: {median}")


add_data()
print(find_middle(data))
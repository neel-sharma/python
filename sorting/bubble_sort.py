# Code
def bubble_sort(total,data):
    for i in range(total-1):
        for j in range(total - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

'''
# Driver Code

# Individually enter each value

total=int(input('Total sum of numbers? '))
data = []                      
for i in range(0,total):       
    data.append(int(input()))

# Enter all values together

#collective_data = input("Enter numbers separated by a comma:").strip()
#data = [int(i) for i in collective_data.split(",")]
#total=len(data)


data=bubble_sort(total,data)
print(data)
'''

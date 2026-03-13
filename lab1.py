import numpy as np

# 1
arr1 = np.arange(10, 51, 5)
print(arr1)

# 2
arr2 = np.zeros((4, 6))
arr2[2] = 99          
print("\n", arr2)

#3
arr = np.array([12, 45, 7, 19, 88, 3, 56, 91, 24, 67])
print(arr[arr > 50])  

#4
eye = np.eye(5)
np.fill_diagonal(eye, [10, 20, 30, 40, 50])
print("\n", eye)

# 5
x = np.arange(1, 21).reshape(4, 5)
print("\n", x)
print("\n", x[-2:, :])
print(x[:, 2])
print("\n", x[:3, 2:])
a = np.array([1, 2, 3, 4])           
b = np.array([[10], [20], [30]])      
print( a + b)

#7 
data = np.array([150, 220, 90, 300, 180, 45])
normalized = (data - data.min()) / (data.max() - data.min())
print(normalized)

#8
data = np.array([150, 220, 90, 300, 180, 45])
standardized = (data - data.mean()) / data.std()
print(standardized)

#9
mat = np.array([
    [ 4,  8,  1, 12],
    [ 7,  3,  9,  5],
    [11,  2,  6, 10],
    [15,  0, 14, 13]
])
row_means = mat.mean(axis=1)
print(row_means)  
col_sums = mat.sum(axis=0)
print(col_sums)     
max_val = mat.max()
pos = np.unravel_index(mat.argmax(), mat.shape) 
print(f"9c max={max_val} at row={pos[0]}, col={pos[1]}")

#10
arr10 = np.arange(36).reshape(3, 4, 3)
print( arr10.shape)     
print(arr10)

#11
arr = np.arange(1, 17).reshape(4, 4)
print(arr)
flipped = arr[::-1, ::-1]   
print(flipped)
#12
ages  = np.array([23, 45, 19, 34, 28, 51, 17, 39])
names = np.array(["ali","sara","omar","lina","khaled","nour","yara","hassan"])

mask = (ages >= 25) & (ages <= 40)  
print("12:", names[mask])            

#13
ages_copy = ages.copy()              
ages_copy[ages_copy < 20] = 20
print("13:", ages_copy)

#14
np.random.seed(123)                  
arr14 = np.random.randint(1, 101, size=(6, 6))  
print("14:",arr14)

#15
samples = np.random.normal(loc=100, scale=15, size=10)
print("15:", samples)

#16
colors = ["red", "blue", "green", "yellow", "purple"]
chosen = np.random.choice(colors, size=3, replace=False)
print("16:", chosen)

#17
nums = np.arange(1, 21)
np.random.shuffle(nums)   
print("17:", nums)
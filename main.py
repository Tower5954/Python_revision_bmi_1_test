# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


height_input = float(height)
weight_input = float(weight)

result = weight_input / (height_input ** 2)

print(int(result))
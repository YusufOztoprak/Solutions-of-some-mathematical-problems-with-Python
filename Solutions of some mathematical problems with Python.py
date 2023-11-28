#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Program to add two numbers and display the result

# Input two numbers from the user
number1 = float(input("Enter the first number:"))
number2 = float(input("Enter the second number:"))

# Adding the two numbers
sum_result = number1 + number2

# Displaying the result
print("The sum of", number1, "and", number2, "is:", sum_result)


# In[1]:


# Program to find the voltage(V) value of the circuit given the current(I) and resistance(R) values

#Get the value of current(I) from the user
current = float(input("Enter the value of current(I):"))

#Get the value of resistance(R) from the user
resistance = float(input("Enter the value of resistance(R):"))

# Calculate the voltage (V)
voltage = current * resistance

#Display the calculated voltage(V) value 
print("Voltage value of the circuit given current and resistance values:",voltage)


# In[34]:


#Program that calculates the area and perimeter of a rectangle whose short and long sides length are entered

# Get the length of the short and long sides from the user
short_side = float(input("Enter the length of the short side: "))
long_side = float(input("Enter the length of the long side: "))

# Calculate the area
area = short_side * long_side

# Calculate the perimeter
perimeter = 2 * (short_side + long_side)

# Display the calculated values of the area and the perimeter
print("Area of the rectangle:", area)
print("Perimeter of the rectangle:", perimeter)


# In[13]:


#Program that calculates the area of a circle given its radius

#Get the length of radius(r)
radius=float(input("Enter the length of radius:"))

#Calculate the area
area = 3.14*radius**2

#Display the calculated value of the area
print("Area of the circle:",area)


# In[2]:


#Program that calculates the equivalent of the entered number of days in years and months

#Get the number of days entered
day_number=int(input("Enter the number of the days:"))

#Calculate the year number
year_number=day_number/365

#Calculate the month number
month_number=year_number*12


#Display the calculated numbers of years and months
print("Year equivalent of the entered number of days:",year_number)
print("Month equivalent of the entered number of days:",month_number)


# In[7]:


#Program that reverses an entered 3-digit number

#Get the entered number
number=input("Enter a 3-digit number:")

#Reverse the number
reversed_number=number[::-1]


#Display the reversed version of the 3-digit number
print("Reversed version of the entered number :",reversed_number)


# In[9]:


#Program that converts the grade of the student whose grade was entered into the 100-point system into the 5-point system

#Get the entered grade of the student in the 100-point system
Grade100=int(input("Enter the grade:"))

#Convert the grade into the 5-point system
Grade5=Grade100 / 20


#Display the converted version of the grade
print("Students point from the 5-point system:",Grade5)


# In[13]:


#Program that prints the total price of the product whose price and VAT rate are entered on the screen

#Get the entered price of the product
price=float(input("Enter the price of the product:"))
            
#Get the entered VAT rate of the product
VAT=float(input("Enter the VAT rate:"))

#Calculate the total price
total_price=price * (VAT + 100) / 100
            
#Display the total price of the product
print("Total price of the product:",total_price)


# In[15]:


#Program that calculates the selling price of a product using the purchase price, tax and profit rates

#Get the entered purchase price of the product
purchase_price=float(input("Enter the purchase price of the product:"))

#Get the entered tax rate
tax_rate=float(input("Enter the tax rate:"))

#Get the profit rate
profit_rate=float(input("Enter the profit rate:"))

#Calculate the selling price of the product
selling_price=(purchase_price*(100+tax_rate)/100)*(100+profit_rate)/100

#Display the selling price of the product
print("Selling price of the product:",selling_price)


# In[18]:


#Program that prints the place values of 3-digit numbers entered from the keyboard

#Get the entered number
number=input("Enter a 3-digit number:")


#Display the place values of the entered number
print("Value of the hundreds place of the number:",number[0])
print("Value of the tens place of the number:",number[1])
print("Value of the ones place of the number:",number[2])


# In[21]:


#Program that swaps variables A and B without changing a third variable

#Get the variable A
A=float(input("Enter the variable A:"))

#Get the variable B
B=float(input("Enter the variable B:"))

#Swap the variables without using a third variable
A,B=B,A

#Display swapped values
print("Return of the variable A:",A)
print("Return of the variable B:",B)


# In[31]:


#Program that calculates the sum of the series k + 2k + 3k + ...+nk 

#Get the value of n from the user
n=float(input("Enter the value of n:"))

#Get the value of k from the user
k=float(input("Enter the value of k:"))

#Calculate the sum of the series(k+2k+3k...nk)
sum_of_series=(n * (n + 1) / 2) * k

#Display the answer
print("Sum of the series(k+2k+3k+..nk):",sum_of_series)


# In[33]:


#Program that finds the end point coordinates of a line given the starting and midpoint coordinates

#Get the starting coordinates
starting_x=float(input("Enter the starting coordinate of the x:"))
starting_y=float(input("Enter the starting coordinate of the y:"))

#Get the midpoint coordinates
midpoint_x=float(input("Enter the midpoint coordinate of the x:"))
midpoint_y=float(input("Enter the midpoint coordinate of the y:"))

#Calculate the end point coordinate of the line
end_x=(midpoint_x*2)-starting_x
end_y=(midpoint_y*2)-starting_y

#Display the end point coordinates of the line
print("End point coordinates of the program:",end_x,",",end_y)


# In[ ]:





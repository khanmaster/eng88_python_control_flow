# Control Flow with if, elif and else - loops

weather = "sunny"

if weather == "thinking": # if this condition is False execute the next line of code
     print("Enjoy the weather ") # if true this line will get executed
if weather != "sunny":
     print(" waiting for the sunshine")
if weather == "cloudy":
    print(" still waiting for sunshine")
else:
    print("Opps sorry something went wrong .. please try later") # If false this line will get executed

# add a condition to use elif when the condition is False

#Loops are used to ITERATE through data
 #Lists, Dict, sets

list_data = [1, 2, 3, 4, 5]
 print(list_data)
#First iteration
for list in list_data:
     if list == 3:
         print("I found 3")
     if list == 2:
         print(" now I found 2")
     if list == 5:
         print(" this is the last number and I found it as well - 5")
 else:
     print("Better Luck next time")

# Second Iteration

student_1 = {
     "name": "Shahrukh",
     "key": " value ",
     "stream": "Cyber Security ", # string
     "completed_lessons": 3, # int
     "complete_lessons_names": ["variables", "operators", "data_collections"] # list
}
 for data in student_1.values():
     if data == " value ":
         break
     print(data)
#
#
#
#
#
# user_prompt = True
#
# while user_prompt:
#     age = input("What is your age? ")
#     if age.isdigit():
#         user_prompt = False
#     else:
#         print("Please provide your answer in digits")
#
# print(f"Your age is {age}")


# While loops

user_prompt = True

while user_prompt:
 age = input("Please enter your age? ")
 if age.isdigit():
     user_prompt = False
 else:
     print("Please provide your answer in digits")
print(f"Your age is {age}")










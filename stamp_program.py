"""
start 
get the number of sheets
sheets / 5
round answer to the next number
output the result to the user
end
"""
def calculate(sheet):
  answer = sheet / 5
  rounded = round(answer, 1)
  print("sheet is : ", sheet)
  print("The answer is: ", answer)
  print("rounded is: ", rounded)
  print("========================")
  return rounded 

output = calculate(10000)

print("the return statement is: ", output)
def BMI():
  name = str(input("Enter your name: "))
  if name:
      height = int(input("Enter your height in cm: "))
      weight = int(input("Enter your weight in kg: "))
      bmi = weight / (height/100)**2
      print(bmi)
      if bmi < 18.0:
          print(name + " you are underweight")
      elif bmi < 25.0:
          print(name + " you are healthy")
      elif bmi < 30.0:
          print(name + " you are overweight")
      elif bmi > 30:
          print(name + " you are obese follow healthy diet and do some exercises")
  else:
    print("Please enter required details to know your BMI") 
  return 
BMI()

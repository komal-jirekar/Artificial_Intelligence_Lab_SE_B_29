subject1=(input("Enter the first subject"))
subject2=(input("Enter the second subject"))
if(subject1=="maths" and subject2=="physics"):
  print("Mechanical Engineering")
elif(subject1=="Programming" and subject2=="maths"):
  print("Computer Engineering")  
elif(subject1=="biology" and subject2=="chemistry"):
  print("Biotechnology Engineering")  
elif(subject1=="circuits" and subject2=="maths"):
  print("Electrical Engineering")  
elif(subject1=="Programming" and subject2=="statistics"):
  print("Artificial intelligence and data science Engineering")
elif(subject1=="Programming" and subject2=="AI concepts"):
  print("Artificial intelligence and machine learning Engineering")
else:
  print("Invalid")

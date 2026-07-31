while True:
  print("\n------STUDENT MANAGEMENT SYSTEM------")
  print("1. Add student")
  print("2. Update student")
  print("3. View student")
  print("4. Delete student")
  print("5. Search student")
  print("6. Exit")

  choice = input("Enter your choice: ")

  from database import(
  add_student,
  update_student,
  view_student,
  delete_student,
  search_student,
)

  if choice == "1":

    name = input("enter name : ")
    age  = int(input("enter age: "))
    branch = input("enter branch: ")

    add_student(name ,age , branch )
    print("Student Data added succesfully !")

  elif choice == "2":

    student_id = int(input("Enter the Student ID: "))
    age = int(input("Enter New Age: "))
    branch = input("Enter New Branch: ")

    update_student(student_id,  age , branch)
    print("Updated Data Successfully!")

  elif choice == "3":
    students = view_student()
    if students:
      for student in students:
        print(student)
    else:
      print("No records found")
      

  elif choice == "4":
    
    student_id = int(input("Enter Student ID: "))
    delete_student(student_id)

    print('Student data deleted successfully')

  elif choice == "5":
    name = input("enter student name: ")
    students = search_student(name)
    
    if students:
      for student in students:
        print(student)
    else:
      print("No students found!")


  elif choice == "6":
    print("Thank you!")
    break
  else:
    print("Invalid choice")

 

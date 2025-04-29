import requests

# This api add/creates a new student in the system
## json is the data we send as json in the body of the request
## headers contains information for the server needed to execute the request. In this case, we specify that we are sending content in the form of json.
#ADD STUDENT
student1 = requests.post(
    "http://127.0.0.1:5000/students",
    json={'name': 'Test Student 1', 'contact_info': {'email': 'test1@example.com', 'phone': '+49-555-1010'}},
    headers={'Content-Type': 'application/json'},
    proxies={"http": None, "https": None}  # Disable proxy
)
print(f"Response of POST to '/students': {student1.json()}")
#ADD STUDENT2
student2 = requests.post(
    "http://127.0.0.1:5000/students",
    json={'name': 'Test Student 2', 'contact_info': {'email': 'test2@example.com', 'phone': '+49-555-2020'}},
    headers={'Content-Type': 'application/json'},
    proxies={"http": None, "https": None}  # Disable proxy
)
print(f"Response of POST to '/students': {student2.json()}")

#GET STUDENTS
get_students_response = requests.get("http://127.0.0.1:5000/students")
print(f"Response of GET to '/students': {list(get_students_response.json()['students'])}")

#GET STUDENT1
student_specific=requests.get("http://127.0.0.1:5000/students/{student1['student_id']}").json()
print(f"Response of GET to '/students/student_id': {student_specific}")

#ADD TEACHER
teacher1 = requests.post(
    "http://127.0.0.1:5000/teachers",
    json={'name': 'Jane Smith', 'contact_info': {'email': 'jane@example.com', 'phone': '123-456-7890'},
          'specializations': ['math', 'physics']},
    headers={'Content-Type': 'application/json'},
    proxies={"http": None, "https": None}  # Disable proxy
)
print(f"Response of POST to '/teachers': {teacher1.json()}")
#GET TEACHERS
get_teachers_response = requests.get("http://127.0.0.1:5000/teachers")
print(f"Response of GET to '/teachers': {list(get_teachers_response.json()['teachers'])}")

#ADD MATH COURSE
math_course = requests.post(
    "http://127.0.0.1:5000/courses",
    json={'type': 'math', 'name': 'Advanced Calculus', 'max_capacity': 30, 'difficulty_level': 'advanced', 'materials_required':""},
    headers={'Content-Type': 'application/json'},
    proxies={"http": None, "https": None}  # Disable proxy
)
print(f"Response of POST math to '/courses- math': {math_course.json()}")

#ADD ART COURSE
art_course = requests.post(
    "http://127.0.0.1:5000/courses",
    json={'type': 'art', 'name': 'Intro to Painting', 'max_capacity': 20, 'difficulty_level': '',
          'materials_required': ['canvas', 'paint brushes', 'acrylic paint']},
    headers={'Content-Type': 'application/json'},
    proxies={"http": None, "https": None}  # Disable proxy
)
print(f"Response of POST to '/courses- art': {art_course.json()}")

#GET COURSES
get_courses_response = requests.get("http://127.0.0.1:5000/courses")
print(f"Response of GET to '/courses': {list(get_courses_response.json()['courses'])}")

#ENROLL student to MATH course
enroll_student_math = requests.post(
        f"http://127.0.0.1:5000/courses/{math_course.json()['id']}/students/{student1.json()['student_id']}",
        headers={'Content-Type': 'application/json'},
        proxies={"http": None, "https": None}  # Disable proxy
    )


#ENROLL student2 to MATH course
enroll_student2_math = requests.post(
        f"http://127.0.0.1:5000/courses/{math_course.json()['id']}/students/{student2.json()['student_id']}",
        headers={'Content-Type': 'application/json'},
        proxies={"http": None, "https": None}  # Disable proxy
    )
 #WITHDRAW
withdraw_student2_math = requests.post(
        f"http://127.0.0.1:5000/courses/{math_course.json()['id']}/students/{student2.json()['student_id']}",
        headers={'Content-Type': 'application/json'},
        proxies={"http": None, "https": None}  # Disable proxy
    )


#ASSIGN teacher to math course
assign_teacher_math = requests.post(
        f"http://127.0.0.1:5000/courses/{math_course.json()['id']}/teacher/{teacher1.json()['teacher_id']}",
        headers={'Content-Type': 'application/json'},
        proxies={"http": None, "https": None}  # Disable proxy
)

#RECORD attendance
attendance = requests.post(
    f"http://127.0.0.1:5000/courses/{math_course.json()['id']}/attendance",
    json={'date': '2023-10-01', 'present_student_ids': [student1.json()['student_id'], student2.json()['student_id']]},
    headers={'Content-Type': 'application/json'},
    proxies={"http": None, "https": None}  # Disable proxy
)
print(f"Response of RECORDING ATTENDANCE': {attendance.status_code}")


#ASSIGN grade
assign_grade = requests.post(
    f"http://127.0.0.1:5000/courses/{math_course.json()['id']}/grades/{student1.json()['student_id']}",
    json={"grade": 95},
    headers={'Content-Type': 'application/json'},
    proxies={"http": None, "https": None}  # Disable proxy
)
print(f"Response of Assigning grade': {assign_grade.status_code}")

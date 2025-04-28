from typing import Dict, Any, Set
from datetime import date
import uuid

class Course:
    def __init__(self, name: str, max_capacity: int, course_type: str,
                 difficulty_level: str = None, materials_required: Set[str] = None):
        self.id = str(uuid.uuid4())
        self.name = name
        self.max_capacity = max_capacity
        self.course_type = course_type
        self.difficulty_level = difficulty_level
        self.materials_required = materials_required or set()
        self.students = set()  # Set of student IDs
        self.teacher_id = None
        self.attendance = {}  # Dictionary mapping dates to sets of present student IDs
        self.grades = {}  # Dictionary mapping student IDs to their grades
        self.validate()

    def validate(self):
        """Validate course data"""
        # TODO: Implement the validate method
        # 1. Validate that name is a non-empty string
        # 2. Validate that max_capacity is a positive integer
        # 3. Validate that course_type is either 'math' or 'art'
        # 4. For math courses:
        #    - Validate that difficulty_level is one of: 'beginner', 'intermediate', 'advanced'
        # 5. For art courses:
        #    - Validate that materials_required is a set
        #    - Validate that all materials are strings
        if not self.name or not isinstance(self.name,str):
            raise ValueError("Course name should not be empty")

        if not isinstance(self.max_capacity, int) or self.max_capacity<=0:
            raise ValueError("Max capacity should be a positive integer")

        if self.course_type=='math':
            if self.difficulty_level not in['beginner','intermediate','advanced']:
                raise ValueError("Math course: Difficulty level does not match")

        if self.course_type=='art':
            if not isinstance(self.materials_required,set):
                raise ValueError("Art course: Materials_required must be a set")
            if not all(isinstance(item,str) for item in self.materials_required):
                raise ValueError("Art course: Materials are not string in materials_required")

    def take_attendance(self, date: date, present_student_ids: Set[str]):
        """Record attendance for a specific date"""
        # TODO: Implement the take_attendance method
        # 1. Validate that present_student_ids is a set
        # 2. Validate that all IDs in present_student_ids are strings
        # 3. Check that number of present students doesn't exceed enrolled students
        # 4. Verify all present students are enrolled in the course
        # 5. Record the attendance for the given date

        if not isinstance(present_student_ids,set):
           raise ValueError("present_student_ids is not a set")

        if not all(isinstance(items,str)for items in present_student_ids):
            raise ValueError("Take attendance: Materials are not string in present_student_ids")

        if len(present_student_ids)>=len(self.students):
            raise ValueError("Number of present students more than enrolled students")

        if not all(student_id in self.students for student_id in present_student_ids):
            raise ValueError("Some students are not enrolled in the course")

        self.attendance[date]=present_student_ids

    def assign_grade(self, student_id: str, grade: float):
        """Assign a grade to a student"""
        # TODO: Implement the assign_grade method
        # 1. Check if student is enrolled in the course
        # 2. Validate that grade is a number
        # 3. Validate that grade is between 0 and 100
        # 4. Assign the grade to the student
        if student_id not in self.students:
            raise ValueError("Student is not enrolled in course")

        if not isinstance(grade,int) or 0<=grade<=100:
            raise ValueError("Grade should be a number and should be between 0 and 100")

        self.grades[student_id]=grade

    def to_dict(self) -> Dict[str, Any]:
        """Convert course data to dictionary"""
        # TODO: Implement the to_dict method
        # 1. Create a dictionary with the course's basic information:
        #    - id, name, course_type, max_capacity, current enrollment, teacher_id
        # 2. For math courses: include difficulty_level
        # 3. For art courses: include materials_required as a list
        # 4. Return the dictionary
        course_dict={
            'id':self.id,
            'name':self.name,
            'course_type':self.course_type,
            'max_capacity':self.max_capacity,
            'current_enrollment':len(self.students),
            'teacher_id':self.teacher_id
        }
        if self.course_type=='math':
            course_dict['difficult_level']=self.difficulty_level

        if self.course_type=='art':
            course_dict['materials_required']=list(self.materials_required)

        return course_dict
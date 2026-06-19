#this file contains all API For student management system
from fastapi import FastAPI,Depends,HTTPException
#fastapi is used to create the app
#depends helps to use the depedency function
from pydantic import BaseModel
#this is used to deal with the data  validation
from database import Base,engine,SessionLocal
import models#this is used to deal with the models
#importing the session
from sqlalchemy.orm import Session
#--creation of app--
app=FastAPI()
#---create all tables in the database---
Base.metadata.create_all(engine)
#--creation of a student---
class AddStudent(BaseModel):#data validation
    name:str
    age:int
#--creation of a course
class AddCourse(BaseModel):
    course_name:str
#---enrollment of a student in a course----
class EnrollStudent(BaseModel):
    student_id:int
    course_id:int
#--dependency function
def get_db():
    db=SessionLocal()#this enables a Local connection to the database
    try:
        yield db    
    finally:
        db.close()
#--home page--
@app.get('/')
def home():
    return {'Welcome to Student Management System'}
#---1. Create Student---
@app.post('/students',tags=['Adding Students'])
def add_student(*,db:Session=Depends(get_db),add:AddStudent):#*, if i didnt keep this it will raise an error like: non-default must come before default
    student=models.Student(name=add.name,age=add.age)#collect data through request body
    db.add(student)#adding the student to the session
    #commiting the data
    db.commit()
    db.refresh(student)
    return {
    "message": "Added Successfully",
    "student": {
        "id": student.id,
        "name": student.name,
        "age": student.age
    }
}
#---2. Create Course---
@app.post('/courses',tags=['Course Creation'])
def course_creation(*,db:Session=Depends(get_db),add:AddCourse):
    course=models.Course(course_name=add.course_name)
    #adding to the session
    db.add(course)
    db.commit()
    db.refresh(course)
    return {
        'message':'Added Successfully',
        'Course':{
            'id':course.id,
            'course_name':course.course_name
        }
    }
#3. Enroll Student in Course
@app.post('/enroll',tags=['Enrolling a Student'])
def enroll(*,db:Session=Depends(get_db),enroll:EnrollStudent):
    enrolling=models.Enrollments(student_id=enroll.student_id,course_id=enroll.course_id)
    student_exists = db.query(models.Student).filter(models.Student.id == enroll.student_id).first()
    course_exists = db.query(models.Course).filter(models.Course.id == enroll.course_id).first()
    if student_exists and course_exists:
        #adding to the session
        db.add(enrolling)
        #committing to the database
        db.commit()
        #refreshing
        db.refresh(enrolling)
        return{
            'message':'Enrolled Successfully',
            'Enrollment':{
                'student id':enrolling.student_id,
                'course id':enrolling.course_id
            }
        }
    else:
        raise HTTPException(status_code=404,detail='Invalid Student id or Course id')
#----4. Get All Students----
@app.get('/students',tags=['Get All Students'])
def all_students(db:Session=Depends(get_db)):
    students=db.query(models.Student).all()
    if students:
        return{
        'message':'All Students Fetched Successfully',
        'Students':students
            }
    else:
        raise HTTPException(status_code=404,detail='No Records Found')
#---5. Get Courses of a Student---
@app.get('/students/{id}/courses',tags=['Get Course of a student'])
def Course_of_Student(id:int,db:Session=Depends(get_db)):
    studentCoursesID=db.query(models.Enrollments.course_id).filter(models.Enrollments.student_id==id).all()
    course_ids = [row[0] for row in studentCoursesID]
    if studentCoursesID:
        name_of_student=db.query(models.Student.name).filter(models.Student.id==id).scalar()
        courses_names=db.query(models.Course.course_name).filter(models.Course.id.in_(course_ids)).all()
        result={}
        result['student']=name_of_student
        result['courses']=[c[0] for c in courses_names]
        return result
    raise HTTPException(status_code=404,detail='No Record Found')
#----6.Get Students in a Course----
@app.get('/courses/{id}/students',tags=['Get Students in a Course'])
def get_students_in_course(id: int, db: Session = Depends(get_db)):
    # Step 1: Checking whether  if course exists or not
    course = db.query(models.Course).filter(models.Course.id == id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    # Step 2: JOIN Student with Enrollments
    students = db.query(models.Student.name)\
        .join(models.Enrollments, models.Student.id == models.Enrollments.student_id)\
        .filter(models.Enrollments.course_id == id)\
        .all()
    # Step 3: Extract names from tuples
    student_names = [s[0] for s in students]
    return {
        "Course": course.course_name,
        "Students": student_names
    }
#this file contains all the models that we use in this  project
from database import Base
#Base helps to recognize class as table
from sqlalchemy.orm import relationship
#this will maintain the relationship among the tables
from sqlalchemy import Column,Integer,String,ForeignKey
#column is used to create columns
#integer,string are datatypes
#foreign key are used to link the tables

#--First model--
#student Table
class Student(Base):
    __tablename__='Students'
    id=Column(Integer,primary_key=True)#this is the id of the student which is unique
    name=Column(String,nullable=False)#name of the student,and it cannot be null
    age=Column(Integer)#this is the age of the student
    enrollments=relationship('Enrollments',back_populates='student')
#--second model--
#course Table
class Course(Base):
    __tablename__='Courses'
    id=Column(Integer,primary_key=True)#hey this is the course id which is unique
    course_name=Column(String)#this is the name of the course
    enrollments=relationship('Enrollments',back_populates='course')
#--final model--
#enrollments Table
class Enrollments(Base):
    __tablename__='Enrollments'
    id=Column(Integer,primary_key=True)#this is the unique id of each course enrollment for a student
    student_id=Column(Integer,ForeignKey('Students.id'))#this will refer the student id in the student table
    course_id=Column(Integer,ForeignKey('Courses.id'))#this will refer the course id in the course table
    student=relationship('Student',back_populates='enrollments')
    course=relationship('Course',back_populates='enrollments')
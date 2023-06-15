from flask import jsonify
from flask_restx import Namespace, Resource
from core.dependencies import db

from core.lib.api_model import *
from core.models.models import Course, Student

ns1 = Namespace(name="Hello ", description="Hello Rest X")

dic_data = lambda **args: args


@ns1.route("/hello")
class HelloRest(Resource):
    def get(self):
        return dic_data(hello="REST-X")


@ns1.route("/courses")
class CourseList(Resource):
    @ns1.marshal_list_with(course_model)
    def get(self):
        return Course.query.all()

    @ns1.expect(course_input_model)
    @ns1.marshal_with(course_model)
    def post(self):
        course = Course(name=ns1.payload["name"])
        db.session.add(course)
        db.session.commit()
        return course


@ns1.route("/courses/<int:id>")
class CourseAPI(Resource):
    @ns1.marshal_with(course_model)
    def get(self, id):
        return Course.query.get(id)


@ns1.route("/student")
class StudentsListAPI(Resource):
    @ns1.marshal_list_with(student_model)
    def get(self):
        return Student.query.all()

    @ns1.expect(student_input_model)
    @ns1.marshal_with(student_model)
    def post(self):
        student = Student(name=ns1.payload["name"], course_id=ns1.payload["course_id"])
        db.session.add(student)
        db.session.commit()
        return student, 201


@ns1.route("/student/<int:id>")
class StudentsAPI(Resource):
    @ns1.marshal_with(student_model)
    def get(self, id):
        student = Student.query.get(id)
        return student

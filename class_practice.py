class Courses(object):
    
    def __init__(self, course_name_list, instructor_name_list, num_students_list):
        self.courses_dict = {}
        
        for i, cname in enumerate(course_name_list): # cname is equivalent to course name
            instructor_nstudents_tuple = (instructor_name_list[i], num_students_list[i])
            self.courses_dict[cname] = instructor_nstudents_tuple

    
    
    def addCourse(self, course_name, instructor_name, num_stusents):
        if course_name not in self.courses_dict:
            self.courses_dict[course_name] = (instructor_name, num_stusents)
                    
    
    def addStudents(self, course_name, num_stusents):
        if course_name in self.courses_dict:
            self.courses_dict[course_name] = (self.getInstructor(course_name), num_stusents + self.getNumStudents(course_name))
            
    
    def adjustInstructor(self, course_name, instructor_name):
        if course_name in self.courses_dict:
            self.courses_dict[course_name] = (instructor_name, self.getNumStudents(course_name))
    
            
    
    def getInstructor(self, course_name):
        if course_name not in self.courses_dict:
            return None
        else:
            return self.courses_dict[course_name][0]
            
    
    def getNumStudents(self, course_name):
        if course_name not in self.courses_dict:
            return None
        else:
            return self.courses_dict[course_name][1]
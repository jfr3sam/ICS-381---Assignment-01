if __name__ == "__main__":
#     # from function_practice import *
    
#     # ############################### test function_practice
#     # A = [3, 2, 1, 0, -1, -2, -3]
#     # A_sorted = bubble_sort(A)
#     # tmin = third_min(A)
#     # smax = second_max(A)
#     # print(A, A_sorted)  # note that A should be original unsorted
#     # print(tmin, smax)
#     # print()
    
#     # A = [79, 31, -73, -47, -18, -25, 45, 89]
#     # A_sorted = bubble_sort(A)
#     # tmin = third_min(A)
#     # smax = second_max(A)
#     # print(A, A_sorted)  # note that A should be original unsorted
#     # print(tmin, smax)
    
#     # print('_______________________________________________________________________')
    
    ############################## test class_practice
    from class_practice import *
    
    course_names = ['ICS-501', 'ICS-502', 'ICS-104', 'MATH-101']
    instructor_names = ['Moayad', 'Irfan', 'Ahmed', 'Khalid']
    num_students = [28, 16, 36, 45]
    
    courses_221 = Courses(course_names, instructor_names, num_students)
    
    for course in courses_221.courses_dict:
        print('{}, {}, {}'.format(course, courses_221.getInstructor(course), courses_221.getNumStudents(course)))
        
    # do some adjustments then print
    print('--------------Making changes--------------')
    courses_221.adjustInstructor('ICS-104', 'Mohammed')
    courses_221.adjustInstructor('ICS-501', 'Moataz')
    courses_221.addStudents('ICS-502', 16)
    courses_221.addStudents('ICS-104', 100)
    
    for course in courses_221.courses_dict:
        print('{}, {}, {}'.format(course, courses_221.getInstructor(course), courses_221.getNumStudents(course)))
    
#     print('_______________________________________________________________________')
#     ############################### test ac_simulation
#     from ac_simulation import *
#     ac_agent = SimpleACReflexAgent(min_threshold=0, max_threshold=100)
#     ac_env = SimpleACEnvironment(ac_agent, starting_temp=50)
    
#     print("AC simulation #1 starting conditions:")
#     print("min-max thresholds: {}, {}".format(ac_agent.min_threshold, ac_agent.max_threshold))
#     print("env temperature: {}, num_agent_actions: {}, is_ac_on: {}".format(ac_env.temperature, ac_env.num_agent_actions, ac_env.is_ac_on))
    
#     print("-----simulating for 60 timesteps-----")
#     ac_env.simulate(60) # expecting temperature: 90, num_agent_actions: 1, is_ac_on: True
#     print("env temperature: {}, num_agent_actions: {}, is_ac_on: {}".format(ac_env.temperature, ac_env.num_agent_actions, ac_env.is_ac_on))
#     print('______________________')
    
#     ac_agent = SimpleACReflexAgent(min_threshold=15, max_threshold=25)
#     ac_env = SimpleACEnvironment(ac_agent, starting_temp=20)
#     print("AC simulation #2 starting conditions:")
#     print("min-max thresholds: {}, {}".format(ac_agent.min_threshold, ac_agent.max_threshold))
#     print("env temperature: {}, num_agent_actions: {}, is_ac_on: {}".format(ac_env.temperature, ac_env.num_agent_actions, ac_env.is_ac_on))
    
#     print("-----simulating for 48 timesteps-----")
#     ac_env.simulate(48) # expecting temperature: 18, num_agent_actions: 5, is_ac_on: True
#     print("env temperature: {}, num_agent_actions: {}, is_ac_on: {}".format(ac_env.temperature, ac_env.num_agent_actions, ac_env.is_ac_on))
#     print('_______________________________________________________________________')
    
    ############################# test server_simulation
    
    # from server_simulation import *
    # import random
    # random.seed(20220829) # set the seed to be able to reproduce results
    
    # server_agent = ServerAgent(small_count=5, medium_count=5, large_count=10)
    # server_env = ServerEnvironment(server_agent)
    
    # print("Server simulation #1 starting conditions:")
    # print("small, medium, large counts: {}, {}, {}".format(server_agent.small_count, server_agent.medium_count, server_agent.large_count))
    # # print("env num_agent_actions: {}".format(server_env.num_agent_actions))
    
    # print("-----simulating until storage is done-----")
    
    
    # server_env.simulate() 
    # print("env num_agent_actions: {}".format(server_env.num_agent_actions))
    # print('______________________')
    
    # random.seed(20220829) # set the seed to be able to reproduce results
    
    # server_agent = ServerAgent(small_count=100, medium_count=50, large_count=50)
    # server_env = ServerEnvironment(server_agent)
    
    # print("Server simulation #2 starting conditions:")
    # print("small, medium, large counts: {}, {}, {}".format(server_agent.small_count, server_agent.medium_count, server_agent.large_count))
    # print("env num_agent_actions: {}".format(server_env.num_agent_actions))
    
    # print("-----simulating until storage is done-----")
    # server_env.simulate() 
    # print("env num_agent_actions: {}".format(server_env.num_agent_actions))
    # print('______________________')
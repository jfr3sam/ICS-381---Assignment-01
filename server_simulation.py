import random

class ServerAgent(object):
    
    def __init__(self, small_count = 10, medium_count = 10, large_count = 10):
        self.small_count = small_count
        self.medium_count = medium_count
        self.large_count = large_count
                
        
    def select_action(self, percept):
        if 0 <= percept and percept <= 33:
            if self.large_count > 0:
                self.large_count = self.large_count - 1
                return "large"
            else:
                return None
            
        elif 34 <= percept and percept <= 66:
            if self.medium_count > 0:
                self.medium_count = self.medium_count - 1
                return "medium"
            else:
                return None
        
        elif 67 <= percept and percept <= 99:
            if self.small_count > 0:
                self.small_count = self.small_count - 1
                return "small"
            else:
                return None
            
        elif percept >= 100:
            return None
            
    def storage_empty(self):
        if self.small_count == 0 and self.medium_count == 0 and self.large_count == 0:
            return True
        else:
             return False
               
         
class ServerEnvironment(object):
  
    def __init__(self, server_agent):
        self.server_agent = server_agent
        self.num_agent_actions = 0
        
                
        
    def tick(self):
        percept = random.randint(0, 130)
        self.server_agent.select_action(percept)
        self.num_agent_actions = self.num_agent_actions + 1
        


    def simulate(self):
            while self.server_agent.storage_empty() is not True:
                self.tick()
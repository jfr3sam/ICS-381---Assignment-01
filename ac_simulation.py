
class SimpleACReflexAgent(object):
    
    def __init__(self, min_threshold, max_threshold):
        self.min_threshold = min_threshold
        self.max_threshold = max_threshold
                
        
    def select_action(self, percept):
        if percept[1] == True and  percept[0] >= self.max_threshold:
            return "TurnOff"
            
        elif percept[1] == False and percept[0] <= self.min_threshold:
            return "TurnOn"
        
        else:
            return None
        
        
class SimpleACEnvironment(object):
    
    def __init__(self, ac_agent, starting_temp = 28):
        self.ac_agent = ac_agent # Is the AC reflex agent
        self.temperature = starting_temp # Is the current temperature.
        self.num_agent_actions = 0 # Is the number of time the agent performed "TurnOn" & "TurnOff"
        self.is_ac_on = False 
        
        
    def tick(self):
        percept = [self.temperature, self.is_ac_on]  
        ac_state =  self.ac_agent.select_action(percept)
        
        if ac_state == "TurnOn":
            self.is_ac_on = True
            self.num_agent_actions = self.num_agent_actions + 1
            
        elif ac_state == "TurnOff":
            self.is_ac_on = False
            self.num_agent_actions = self.num_agent_actions + 1
            
        if self.is_ac_on is True:
            self.temperature = self.temperature + 1
            
        elif self.is_ac_on is False:
            self.temperature = self.temperature - 1
              
    def  simulate(self, num_timesteps):
        for i in range(0, num_timesteps):
            self.tick()
     
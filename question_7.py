class Engine():

    def Start(self):
        return "Car started"
    
    def Stop(self):
        return "Car stopped"
    
class Car():
    def __init__(self):
      self.engine = Engine()
    
    def start_engine(self):
        # Use the Engine's start method
        return self.engine.Start()

    def stop_engine(self):
        # Use the Engine's stop method
        return self.engine.Stop()

   
# Demonstration
car = Car()

# Starting the engine through the Car class
print(car.start_engine())  # Should print "Engine started."

# Stopping the engine through the Car class
print(car.stop_engine())  # Should print "Engine stoppe  

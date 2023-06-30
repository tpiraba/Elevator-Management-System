class Door:

    def __init__(self):
        self.state = False # The door initially closed 
        self.timeToOpen = 5 
        self.timeToClose = 5 

    def openDoor(self):
        """
        Sets door's state to True when opened
        """
        self.state = True 

    
    def closeDoor(self):
        """
        Sets door's state to False when closed
        """
        self.state = False 
   
    def getDoorStatus(self):
        pass
    
   
    def setDoorStatus(self, input):
       pass
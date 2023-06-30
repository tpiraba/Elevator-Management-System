class ElevatorControl:

    def __init__(self, insidePanel): # InsidePanel object is passed into constructor
        self.queue = insidePanel.requestList
        self.elevators = [] 
        

    def manageFloorRequestsUp(self):
        """
        Sorts floor request queue in increasing order when the elevator goes up.
        Returns nothing 
        """
        self.queue.sort()


    def manageFloorRequestsDown(self):
        """
        Sorts floor request queue in decreasing order when the elevator goes down.
        Returns nothing 
        """
        self.queue.sort(reverse=True)

    def updateElevatorStatus(self):
        pass

    def sendElevator(self):
        pass

    def assignElevator(self):
        pass

    def getElevatorStatus(self):
        pass


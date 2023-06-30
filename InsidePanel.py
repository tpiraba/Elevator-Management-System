class InsidePanel: 
    def __init__(self):
        self.buttonList = [1,2,3,4,5] # Floor buttons
        self.requestList = [] # Used for queueing up floors

    # button gets added to the request list
    def pressButton(self, button):
        """
        button gets added to the request list (queue)
        """
        self.requestList.append(button) 
    
    
    def getFloorRequestList(self):
        """
        Returns request list
        """
        return self.requestList
    
    
    def clearFloorRequestList(self):
        """
        Resets request list
        """
        self.requestList = []

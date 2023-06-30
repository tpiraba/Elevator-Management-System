class OutsidePanel:

    def __init__(self):
        self.button = "" # button is initialized to nothing
        self.buttonList = ["Up", "Down"]
      
    def requestUp(self):
        """
        Sets button to "Up" when the up button has been pressed from outside the elevator
        """
        self.button = "Up"

    def requestDown(self):
        """
        Sets button to "Down" when the down button has been pressed from outside the elevator
        """
        self.button = "Down"
    
    def is_button_pressed(self):
        pass

    # Did not use
    def setButton(self, button):
        pass

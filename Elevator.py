class Elevator:

  def __init__(self, carID, currentFloor):
    self.carID = carID # Elevator car ID (initialized when object is created)
    self.currentFloor = currentFloor # Elevator's current floor (initialized when object is created)
    self.destinationFloor = None
    self.direction = ""
    self.doorStatus = None

    
  def move(self, new_floor):
    """
    Changes currentFloor to new_floor
    """
    self.currentFloor = new_floor

  
  # Returns currentFloor
  def getCurrentFloor(self):
    """
    Returns currentFloor
    """
    return self.currentFloor 
class Track:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def move(self, delt_x, delt_y):
        return Track(self.x + delt_x, self.y + delt_y)
    
    def distance(self, other_track):
        delt_x = self.x - other_track.x
        delt_y = self.y - other_track.y
        
        return (delt_x**2 + delt_y**2)**0.5
class home(Controller):
    'Home controller'
    
    
    def __init__(self):
        self.myname = self.__class__.__name__
        
    def main(self, *args):
        return {'name' : 'ali'};
    




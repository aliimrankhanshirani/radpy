from radboot import *

class Controller:
    'Base controller of RADPY - Raapy'

    def __init__(self):
        print "controller created\n\n\n"
        
    def render(self,tpl='none',area='CONTENT'):
        print tpl, area, "\n"

    def me(self):
        print self.__class__.__name__


class home(Controller):
    'Home controller'
    
    def test(self):    
        return "test"
    

x = home();
x.me()
print x.test()
print x.__doc__


print "\n\n\n"

include('../prev_file.py')

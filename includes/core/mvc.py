# @package RADPY 1.0 Goodies
# @date    April 23, 2016
# @author  Ali Imran <me@aliiks.com>


class Controller:
    'Base controller of RADPY - aka "RED PIE"'

    get = {}
    post = {}

    def __init__(self):
        self.get  = {}
        self.post = {}
        
    def render(self,tpl='none',area='CONTENT',_DATA={}):
        print tpl, area, "\n"

    def me(self):
        return self.__class__.__name__

    def main(self, *args):
        return "Controller::main() called"

    def render_layout(self):
        return ">> todo - Layout rendering"

    def eval_template(self, template, _DATA={}):
        return ">> todo - Template evaluation"

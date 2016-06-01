#!C:/Python/python.exe -u 
# @package RADPY 1.0 BookLoader
# @date    April 23, 2016
# @author  Ali Imran <me@aliiks.com>

try:
    import sys
    import cgi
    import os
    import cgitb

    cgitb.enable()

    MY_ROOT_DIR = os.path.dirname(os.path.realpath(__file__));

    parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.sys.path.insert(0,parentdir) 

    def start_http():
        print "Content-Type: text/html"
        print

    _GET=_POST={}
    args=os.getenv("QUERY_STRING").split('&')

    for arg in args: 
        if "=" not in arg and len(arg)>0:
            _GET[arg]=True
        else:
            t = arg.split('=')
            if len(t)>1: 
                k,v=arg.split('=')
                _GET[k]=v

    
    args=sys.stdin.read().split('&')

    for arg in args: 
        t = arg.split('=')
        if len(t)>1: 
            k, v=arg.split('=') 
            _POST[k]=v

    ##################################################################################
    from includes.settings import *
    from includes.core.mvc import *

    start_http()
    ##################################################################################

    ARGUMENTS = _GET["_url"].split('/')
    ARGUMENTS.pop(0)
    ARGUMENTS = filter(None, ARGUMENTS)

    current_controller = DEFAULT_CONTROLLER
    __controller = {}

    #set selected controller
    if ARGUMENTS.__len__() > 0:
        current_controller = ARGUMENTS[0]
        ARGUMENTS.pop(0)

    c_filename = '../application/controllers/'+current_controller+'.py'
    if not os.path.isfile(c_filename):
        raise Exception("controller not found - "+current_controller)
        os._exit(1001)
        
    c_fp = open(c_filename, 'rb')
    c_ret = c_fp.read(1000000)
    c_fp.close()
    exec(c_ret);


    c_ret = "__controller = "+current_controller+"()"
    exec(c_ret);

    __controller.get = _GET
    __controller.post = _POST

    current_method = DEFAULT_METHOD
    #set selected method
    if ARGUMENTS.__len__() > 0:
        current_method = ARGUMENTS[0]
        ARGUMENTS.pop(0) 
        if not current_method in dir(__controller):
            raise Exception("method not found - "+current_controller+"::"+current_method)
            os._exit(1002) 
            
    __func_result = ''    
    if len(ARGUMENTS) > 0:
        exec('__func_result = __controller.'+current_method+'(*ARGUMENTS)')    
    else:
        exec('__func_result = __controller.'+current_method+'()')    


    ##################################################################################
    __func_result = __func_result if 'ajax' in _GET else __controller.render_layout()

    if 'ajax' in _GET:
        import json
        print json.dumps(__func_result)
    else:
        print __func_result
            
    ##################################################################################

except:
    e = sys.exc_info()[0]
    print "Unexpected error:", e
    raise


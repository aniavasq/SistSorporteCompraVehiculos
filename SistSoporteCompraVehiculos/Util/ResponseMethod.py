'''
Created on 27/08/2014

@author: anibal
'''

class ResponseMethod(object):
    '''
    classdocs
    '''

    def __init__(self, model):
        '''
        Constructor
        '''
        self.model = model
        
    def do_on_post(self, request, post_action):
        return post_action(request)
    
    def do_on_get(self, request, get_action):
        return get_action(request)
    
    REQUEST_METHODS = {'POST': do_on_post,
                       'GET': do_on_get,
                       }
    
    def do_on_request(self, request, actions, do_on_method=REQUEST_METHODS):
        return do_on_method[request.method](self, request, actions[request.method])
        
        
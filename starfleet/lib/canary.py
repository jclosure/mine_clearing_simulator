
import sys, inspect

from itertools import *
import six

class Canary:

    def tweet(self):
        print "tweet"
    def eat(self, food):
        print "eating " + food

    def get_method_parameters(self, name):
        for varname in self.__class__.__dict__[name].__code__.co_varnames:
            print varname

    def find_method(self, name):
        
        for key,val in six.iteritems(self.__class__.__dict__):
            if key == name:
                return key,val


# module level functions
def is_mod_function(mod, func):
    return inspect.isfunction(func) and inspect.getmodule(func) == mod

def list_functions(mod):
    return [func.__name__ for func in mod.__dict__.itervalues() 
            if is_mod_function(mod, func)]


# print 'functions in current module:\n', list_functions(sys.modules[__name__])
# print 'functions in inspect module:\n', list_functions(inspect)

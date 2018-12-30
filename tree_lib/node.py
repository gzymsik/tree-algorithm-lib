'''
Created on 30 Dec 2018

@author: gbarabas
'''


class TreeNode(object):
    def __init__(self, node_element):
        self.element = node_element
        self.left = None
        self.right = None

    def __str__(self):
        return "TreeNode: %s" % self.element

    def __repr__(self):
        return self.__str__()

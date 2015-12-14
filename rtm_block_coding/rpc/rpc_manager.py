import os
from twisted.web import server, xmlrpc, resource
from twisted.web.xmlrpc import withRequest

class RpcManager(xmlrpc.XMLRPC):
    """
    An example object to be published.
    """
    isLeaf = True

    def __init__(self, directory=None):
        xmlrpc.XMLRPC.__init__(self, allowNone=True)
        if not directory:
            directory = os.getcwd()
        self.directory = directory
        if not os.path.isdir(directory):
            os.mkdir(directory)

        self.old_directory = os.getcwd()

    def pre_rpc(self):
        os.chdir(self.directory)

    def post_rpc(self):
        os.chdir(self.old_directory)
        
    def xmlrpc_echo(self, x):
        return [True, x]


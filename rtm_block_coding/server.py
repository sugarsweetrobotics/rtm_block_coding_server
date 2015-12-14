import sys

from nevow import appserver
from twisted.web import server
from twisted.internet import reactor

from site import resource
from rpc import manager

def main(argv):
    sys.stdout.write('--- RTM Block Coding Server\n')    
    self.parser.add_option('-d', '--directory', help='Set Static File Directory Tree Root', default=None, dest='directory')
    self.parser.add_option('-p', '--port', help='Set TCP Port number for web server', type='int', default=8080, dest='port')
    options, argv = self.parse_args(args[:])
    verbose = options.verbose_flag # This is default option
    directory = options.directory
        
    options, argv = self.parse_args(args[:])
    verbose = options.verbose_flag # This is default option
    port = options.port
    if directory is None:
        sys.stdout.write('--- Error. Set Directory for WWW service.\n')
        sys.stdout.write('--- Usage: rbc_server.py -d YOUR_HTML_DIRECTORY\n')
        return -1
    elif not os.path.isdir(directory):
        directory = os.path.join(os.getcwd(), directory)
        if not os.path.isdir(directory):
            raise wasanbon.InvalidArgumentException()
    
    res = resource.ResourceManager(directory)
    res.putChild('RPC', manager.RpcManager(directory=directory));
    site = appserver.NevowSite(res)
    reactor.listenTCP(port, site)
    reactor.run()
    return 0

    

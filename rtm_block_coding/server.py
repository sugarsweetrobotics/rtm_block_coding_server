import sys, optparse, os

from nevow import appserver
from twisted.web import server
from twisted.internet import reactor

from rtm_block_coding import resource, rpc_manager


def main(argv):
    sys.stdout.write('--- RTM Block Coding Server\n')    
    usage = 'rbc_server.py -d YOUR_HTML_DIRECTORY'
    parser = optparse.OptionParser(usage=usage)
    parser.add_option('-d', '--directory', help='Set Static File Directory Tree Root', default=None, dest='directory')
    parser.add_option('-p', '--port', help='Set TCP Port number for web server', type='int', default=8080, dest='port')
    options, argv = parser.parse_args(argv)
    #verbose = options.verbose_flag # This is default option
    directory = options.directory
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
    res.putChild('RPC', rpc_manager.RpcManager(directory=directory));
    site = appserver.NevowSite(res)
    reactor.listenTCP(port, site)
    reactor.run()
    return 0

    

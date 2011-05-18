#
# baselightWebService.py - A spectacular hack job. Simply provides an http
# interface to fl-cp
#
# Date: 15th April 2011
# Author: Andrew Bunday
# Support: requests@baseblack.com
#
#

__version__ = "1.0.0"

import os
import web

urls = 	(
		'/', 'Index',
		)

class Index( object ):
	def GET( self ):
		global pids
				
		i = web.input()
		
		inputpath = i.path.rstrip('/')
		localpath = os.path.dirname( inputpath.replace('/mnt/muxfs/', '/mnt/disk1/images1/' ) )
		
		cmd = 'fl-cp -sync %s %s' % (inputpath, localpath )
		yield "Running '%s'\n\n" % cmd
		
		os.system( '/bin/bash -c "setsid fl-cp -sync %s %s" &' %( inputpath, localpath ) )
		
		
app = web.application(urls, globals())

if __name__ == "__main__":
	app.run()
		
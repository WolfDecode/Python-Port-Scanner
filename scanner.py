#!/bin/python

import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv)==2:
    target=socket.gethostbyname(sys.argv[1])

else:
    print(&quot;Invalid amount of arguements&quot;)
    print(&quot;Syntax: python3 scanner.py &lt;ip&gt;&quot;)

#Add a pretty banner

print(&quot;-&quot;*50)
print(&quot;Scanning target&quot;+target)
print(&quot;Time started&quot;+str(datetime.now()))
print(&quot;-&quot;*50)

try:
    for port in range(50,85):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result=s.connect_ex((target,port))
        if result==0:
            print(&quot;Port {} is open&quot;.format(port))
        s.close()

except KeyboardInterrupt:
    print(&quot;\n Exiting Program&quot;)
    sys.exit()

except socket.gaierror:
    print(&quot;Hostname could not be resolved&quot;)

except socket.error:
    print(&quot;Couldnt connect to server&quot;)
    sys.exit()

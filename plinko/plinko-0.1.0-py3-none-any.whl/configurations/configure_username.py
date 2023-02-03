'''
Set CONNECT_USER Environment Variable.

Copyright (C) 2023 Nat Hawkins & Mike Chappelow

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License (version 3 of the License)
as published by the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''


# Imports
import os
from .configure_api_key import configure_api_key


def configure_username(connect_server = "https://rstudioconnect.analytics.kellogg.com",
                       api_route = "/__api__/v1/user"):
    '''
    Configure CONNECT_USER environment variable in $PATH for assessing
    server-level permissions when authenticating to Connect servers
    
    Parameters
    ----------
    connect_server : str (optional)
        URL for Connect server to authenticate to. Default: "https://rstudioconnect.analytics.kellogg.com"
    api_route : str (optional)
        API route to call in connect_server. Default = "/__api__/v1/user"
        
    Returns
    -------
    int
       1 if CONNECT_USER variable can be set to $PATH by querying connect_server's user API,
       else 0
    '''
    # Configure API key if not configured
    if os.getenv("CONNECT_API_KEY") is None: configure_api_key()
    
    # Call user API for user information
    curl = f'''curl -s -X GET {connect_server}{api_route} -H "Authorization: Key {os.getenv('CONNECT_API_KEY')}" -H "accept: */*"'''
    x    = os.popen(curl).read()
    if x == '' or x is None:
        print("Unable to establish user identification. Please verify CONNECT_API_KEY and try again.")
        return 1
    
    # Post process API return
    true  = True
    false = False
    x     = eval(x)
    
    # Check for valid response with username information
    if "username" in x.keys():
        os.environ["CONNECT_USER"] = x["username"]
        
        # By default, lock user access
        if "locked" in x.keys(): os.environ["CONNECT_USER_LOCKED"] = str(x["locked"])
        else: os.environ["CONNECT_USER_LOCKED"] = "True"
        return 0
    
    print("Unable to establish user identification. Please verify CONNECT_API_KEY and try again.")
    return 1
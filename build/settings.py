# settings. py

def init():
    # Instance KV Variables
    global instanceInfo
    instanceInfo = {}

    # Build Variables
    global otterBuildAll 
    global appServerBuild 
    global routerServerBuild
    global rtmpServerBuild
    global switchServerBuild

    otterBuildAll = False
    appServerBuild = False
    routerServerBuild = False
    rtmpServerBuild = False
    switchServerBuild = False

    '''build Order - the order which the build serveres needs to build
       It is impoortan to have prefix name in JSON which is used below
       It is not required to have all applications to be built. The order
       however will be followed for configurationn are dependent on the
       order of the build.
    '''
    global buildOrder
    buildOrder = ["rtmpserver", "switcherserver", "routerserver", "appserver"]

    ''' All the  scripts we need
        to call is built as a key-value pair
        in the build order. We do this to check
        if all the build requess are correct for
        we do not want to build anything till we make
        sure all requests are good
    '''
    global buildScript
    buildScript = {}

    # list of prebuilt images on existing google cloud
    global images
    images = []

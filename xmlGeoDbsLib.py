# $Header: /nfs/slac/g/glast/ground/cvs/GlastRelease-scons/xmlGeoDbs/xmlGeoDbsLib.py,v 1.1 2008/08/15 21:42:40 ecephas Exp $
def generate(env, **kw):
    #    if not kw.get('depsOnly', 0):
    #        env.Tool('addLibrary', library = 'xmlGeoDbs')
    return 1;

def exists(env):
    return 1;

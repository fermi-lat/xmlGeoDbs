# -*- python -*-
# $Header: /nfs/slac/g/glast/ground/cvs/GlastRelease-scons/xmlGeoDbs/SConscript,v 1.4 2009/01/23 00:07:54 ecephas Exp $ 
# Authors: Joanne Bogart <jrb@slac.stanford.edu>
# Version: xmlGeoDbs-01-47-05
import os
Import('baseEnv')
Import('listFiles')
Import('packages')
progEnv = baseEnv.Clone()

progEnv.Tool('registerTargets', package = 'xmlGeoDbs',
             xml=listFiles(files = ['xml/*'], recursive = True))





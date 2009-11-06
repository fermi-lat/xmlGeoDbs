# -*- python -*-
# $Header: /nfs/slac/g/glast/ground/cvs/GlastRelease-scons/xmlGeoDbs/SConscript,v 1.5 2009/08/07 01:11:09 jrb Exp $ 
# Authors: Joanne Bogart <jrb@slac.stanford.edu>
# Version: xmlGeoDbs-01-47-06
import os
Import('baseEnv')
Import('listFiles')
Import('packages')
progEnv = baseEnv.Clone()

progEnv.Tool('registerTargets', package = 'xmlGeoDbs',
             xml=listFiles(files = ['xml/*'], recursive = True))





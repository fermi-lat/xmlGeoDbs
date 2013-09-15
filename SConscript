# -*- python -*-
# $Header: /nfs/slac/g/glast/ground/cvs/xmlGeoDbs/SConscript,v 1.7 2010/07/19 20:47:05 lsrea Exp $ 
# Authors: Joanne Bogart <jrb@slac.stanford.edu>
# Version: xmlGeoDbs-01-48-01
import os
Import('baseEnv')
Import('listFiles')
Import('packages')
progEnv = baseEnv.Clone()

progEnv.Tool('registerTargets', package = 'xmlGeoDbs',
             xml=listFiles(files = ['xml/*'], recursive = True))





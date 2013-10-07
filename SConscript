# -*- python -*-
# $Header: /nfs/slac/g/glast/ground/cvs/xmlGeoDbs/SConscript,v 1.9 2013/09/18 19:56:14 lsrea Exp $ 
# Authors: Joanne Bogart <jrb@slac.stanford.edu>
# Version: xmlGeoDbs-01-48-03
import os
Import('baseEnv')
Import('listFiles')
Import('packages')
progEnv = baseEnv.Clone()

progEnv.Tool('registerTargets', package = 'xmlGeoDbs',
             xml=listFiles(files = ['xml/*'], recursive = True))





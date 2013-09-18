# -*- python -*-
# $Header: /nfs/slac/g/glast/ground/cvs/xmlGeoDbs/SConscript,v 1.8 2013/09/15 00:10:01 lsrea Exp $ 
# Authors: Joanne Bogart <jrb@slac.stanford.edu>
# Version: xmlGeoDbs-01-48-02
import os
Import('baseEnv')
Import('listFiles')
Import('packages')
progEnv = baseEnv.Clone()

progEnv.Tool('registerTargets', package = 'xmlGeoDbs',
             xml=listFiles(files = ['xml/*'], recursive = True))





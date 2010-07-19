# -*- python -*-
# $Header: /nfs/slac/g/glast/ground/cvs/xmlGeoDbs/SConscript,v 1.6 2009/11/06 01:58:53 jrb Exp $ 
# Authors: Joanne Bogart <jrb@slac.stanford.edu>
# Version: xmlGeoDbs-01-48-00
import os
Import('baseEnv')
Import('listFiles')
Import('packages')
progEnv = baseEnv.Clone()

progEnv.Tool('registerTargets', package = 'xmlGeoDbs',
             xml=listFiles(files = ['xml/*'], recursive = True))





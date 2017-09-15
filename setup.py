'''------------------------------------------------------------------------------------------------
Program:    setup.py
Version:    0.1.0
Py Ver:     2.7
Purpose:    Setup packager for: s3dcolors

Dependents: os
            site
            distutils
            setuptools

Comments:
            Installation:
            > cd /path/to/package_x.x.x
            > pip install . --no-deps

---------------------------------------------------------------------------------------------------
UPDATE LOG:
Date        Programmer      Version     Update
22.03.17    J. Berendt      0.0.1       Written
15.09.17    J. Berendt      0.0.2       Minor formatting updates
                                        Using import _version instead of exec() function.
27.09.17    J. Berendt      0.1.0       Restructured layout for setup to make new setups easier.
-------------------------------------------------------------------------------------------------'''

import os
import site
from distutils.core import setup
from setuptools import find_packages
from s3dcolors._version import __version__


#IGNORE LONG LINES (KEEP FOR READABILITY)
#pylint: disable=line-too-long

#-------------------------------------------------------------------------
#USER PARAMETERS -- FILL ME IN!
PACKAGE     = 's3dcolors'
PLATFORM    = 'Python 2.7'
DESC        = 'A small centralised class libary for S3DEV colourmaps.'
NAME        = 'J. Berendt'
EMAIL       = 'support@73rdstreetdevelopment.co.uk'
URL         = 'n/a'
LICENSE     = 'MIT'

#DEFINE ROOT TO INSTALL DATA_FILES
INST_ROOT = os.path.join(os.path.realpath(site.getsitepackages()[1]), PACKAGE)

#DEFINE PARAMETERS (EDIT THESE)
#LIST ALL PROGRAM DEPENDENCIES IN INSTALL_REQUIRES
#LIST ALL RESOURCE FILES IN DATA_FILES [(DESTINATION, [SOURCE_FILE_1, SOURCE_FILE_2])]
PARAMS = dict(prog              = PACKAGE,
              version           = __version__,
              platforms         = PLATFORM,
              description       = DESC,
              name              = NAME,
              email             = EMAIL,
              url               = URL,
              license_          = LICENSE,
              packages          = find_packages(),
              install_requires  = ['utils'],
              data_files        = [(INST_ROOT, ['README.html'])])

#SETUP PARAMETERS (DO NOT EDIT THESE)
setup(name              = PARAMS['prog'],
      version           = PARAMS['version'],
      platforms         = PARAMS['platforms'],
      description       = PARAMS['description'],
      author            = PARAMS['name'],
      author_email      = PARAMS['email'],
      maintainer        = PARAMS['name'],
      maintainer_email  = PARAMS['email'],
      url               = PARAMS['url'],
      license           = PARAMS['license_'],
      packages          = PARAMS['packages'],
      install_requires  = PARAMS['install_requires'],
      data_files        = PARAMS['data_files'])

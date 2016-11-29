
from setuptools import setup

#GET THE VERSION FILE
exec(open('coloursS3D/_version.py').read())


#DEFINE PARAMETERS (EDIT THESE)
params = dict(prog='coloursS3D',
              version=__version__,
              platforms='Python 2.7',
              description='Package for standardised S3DEV colourmaps.',
              name='J. Berendt',
              email='support@73rdstreetdevelopment.co.uk',
              url='73rdstreetdevelopment.wordpress.com',
              license='MIT',
              packages=['coloursS3D'],
              install_requires=[]
              )


#SETUP PARAMETERS (DO NOT EDIT THESE)
setup(name=params['prog'],
      version=params['version'],
      platforms=params['platforms'],
      description=params['description'],
      author=params['name'],
      author_email=params['email'],
      maintainer=params['name'],
      maintainer_email=params['email'],
      url=params['url'],
      license=params['license'],
      packages=params['packages'],
      install_requires=params['install_requires']
      )
from distutils.core import setup

setup(name='misty_client',
      version='1.0',
      description='REST API client for Misty',
      author='Hunter Thompson',
      license='MIT',
      url='https://github.com/SLIM-Misty/misty-client',
      author_email='hunterthompson261@u.boisestate.edu',
      packages=['misty_client'],
      install_requires=['requests']
)

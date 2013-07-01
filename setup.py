from setuptools import setup
    
setup(name='neocities_client',
      version='0.1',
      description='Simple python client for neocities websites',
      url='http://github.com/skrubly/neocities-client',
      author='Skrubly',
      packages=['neocities_client'],
      install_requires=[
        'requests',
        'beautifulsoup4',
      ],
      zip_safe=False)

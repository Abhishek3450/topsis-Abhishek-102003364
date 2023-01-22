from distutils.core import setup
setup(
  name = 'Topsis-Abhishek-102003364',        
  packages = ['Topsis-Abhishek-102003364'],   
  version = '0.1',      
  license='MIT',        
  description = 'This package can be used for implementation of Multiple criteria decision making using Topsis Algorithm. This is a python library for dealing with Multi-Criteria Decision Making (MCDM) problems by using techniques for order of preference by similarity to ideal solution (TOPSIS).',   # Give a short description about your library
  author = 'Abhishek Gandhi',                 
  author_email = 'abhishekgandhi989@gmail.com',     
  url = 'https://github.com/Abhishek3450/topsis-package',   
  download_url = 'https://github.com/Abhishek3450/topsis-package/archive/refs/tags/py.tar.gz',   
  keywords = ['topsis', 'multiple criteria decision'],   
  install_requires=[        
          'tabulate',
          'os',
          'pandas',
          'math',
          'sys'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3'
      ],
)

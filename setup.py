from distutils.core import setup
setup(
  name = 'Topsis-Abhishek-102003364',         # How you named your package folder (MyLib)
  packages = ['Topsis-Abhishek-102003364'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'This package can be used for implementation of Multiple criteria decision making using Topsis Algorithm. This is a python library for dealing with Multi-Criteria Decision Making (MCDM) problems by using techniques for order of preference by similarity to ideal solution (TOPSIS).',   # Give a short description about your library
  author = 'Abhishek Gandhi',                   # Type in your name
  author_email = 'abhishekgandhi989@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/user/reponame',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['topsis', 'multiple criteria decision'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
      ],
)

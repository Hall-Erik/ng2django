from distutils.core import setup

setup(
  name = 'ng2django',
  scripts = ['ng2django'],
  version = '0.1.1',
  license='MIT',
  description = 'Convert your Angular built index.html file to Django Template syntax',
  author = 'Erik Hall',
  author_email = 'hall.erik@gmail.com',
  url = 'https://github.com/Hall-Erik/ng2django',
  download_url = 'https://github.com/Hall-Erik/ng2django/archive/v_01_1.tar.gz',
  keywords = ['Django', 'Angular'],
  install_requires=[            # I get to this in a second
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)
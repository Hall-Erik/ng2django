import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
  name = 'ng2django',
  version = '22.09.27',
  author = 'Erik Hall',
  author_email = 'hall.erik@gmail.com',
  description = 'Convert your Angular built index.html file to Django Template syntax',
  long_description=long_description,
  long_description_content_type="text/markdown",
  url = 'https://github.com/Hall-Erik/ng2django',
  packages=setuptools.find_packages(),
  entry_points = {
    'console_scripts': [
      'ng2django=ng2django:main',
    ],
  },
  install_requires=[            # I get to this in a second
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',    
  ],
  python_requires='>=3.6',
)
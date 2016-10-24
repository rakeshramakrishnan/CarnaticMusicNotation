#TODO: How to add developer dependencies separately in python? Like 'nose' for tests
from setuptools import setup

def long_description():
    with open('README.rst', 'r') as f:
        return f.read()

setup(name='carnaticMusicNotation',
      version='0.1',
      description='Read MIDI or text notes and generate Latex file of song notation and MIDI, for carnatic music',
      long_description=long_description(),
      url='http://github.com/rakeshramakrishnan/CarnaticMusicNotation',
      author='Rakesh Ramakrishnan',
      author_email='rakeshramakrishnan92@gmail.com',
      classifiers=[
        'Development Status :: 1 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Music :: Carnatic',
      ],
      keywords='Carnatic Music Notation MIDI',
      license='MIT',
      packages=['carnaticMusicNotation'],
      install_requires=['python-midi'],
      dependency_links=['https://github.com/vishnubob/python-midi/tarball/master'],
      include_package_data=True,
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'])

#!/usr/bin/env python3

from setuptools import setup

setup(name='ly2video',
      version='0.5.0',
      description='Converts Lilypond files to videos',
      license='GPLv3',
      author='Adam Spiers',
      author_email='github@adamspiers.org',
      url='https://github.com/aspiers/ly2video',
      packages=['ly2video'],
      install_requires=[
        "mido==1.3.3",
        "packaging==26.3",
        "pexpect==4.9.0",
        "pillow==12.3.0",
        "ptyprocess==0.7.0"
      ],
      entry_points={
          'console_scripts': [
              'ly2video = ly2video.cli:main'
          ]
      },
      scripts=[
          'scripts/midi-rubato',
          'scripts/xsc2beatmap'
      ],
)

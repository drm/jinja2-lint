from distutils.core import setup
setup(name='jinja2-lint',
      version='1.0',
      install_requires=['jinja2'],
      entry_points={
        'console_scripts': [
            'j2lint = j2lint:main',
        ],
        },
      )

from distutils.core import setup
setup(name='jinja2-lint',
      version='2.0.0',
      py_modules=['j2lint'],
      install_requires=['jinja2'],
      entry_points={
        'console_scripts': [
            'j2lint = j2lint:main',
        ],
        },
      )

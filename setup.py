from setuptools import setup, Extension

bitweb_yespower_module = Extension('bitweb_yespower',
                            sources = ['yespower-module.c',
                                       'yespower.c',
                                       'yespower-opt.c',
                                       'sha256.c'
                                       ],
                            extra_compile_args=['-O2', '-funroll-loops', '-fomit-frame-pointer'],
                            include_dirs=['.'])

setup (name = 'bitweb_yespower',
       version = '1.0.4',
       author_email = 'mraksoll4@gmail.com',
       author = 'mraksoll',
       url = 'https://github.com/bitweb-project/bitweb_yespower_python3',
       description = 'Bindings for yespower-1.0 proof of work used by bitweb',
       ext_modules = [bitweb_yespower_module])

from setuptools import setup

test_requirements = [
    'mock',
    'nose',
]

classifiers=[
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 5 - Production/Stable',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',

    # License
    "License :: Public Domain",

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
]

setup(
    name='chipmunk',
    version='1.0',
    description='A very small and simple usage mechanism for Python threadlocals.',
    url='https://github.com/Rigdon/chipmunk',
    download_url='https://github.com/Rigdon/chipmunk/tarball/1.0',
    tests_require=test_requirements,
    test_suite="nose.collector",
    author='Rigdon',
    author_email='mr.rigdon@gmail.com',
    license='The Unlicense',
    packages=['chipmunk'],
    keywords=['utilities', 'locals', 'threading'],
    classifiers=[]
)

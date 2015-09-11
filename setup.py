from setuptools import setup

test_requirements = [
    'mock',
    'nose',
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
    keywords=['utilities', 'locals'],
    classifiers=[]
)

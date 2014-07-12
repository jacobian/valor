from setuptools import setup

setup(
    name = "valor",
    description = "Python HTTP clients for APIs represented by JSON Schema.",
    version = "0.1",
    author = "Jacob Kaplan-Moss",
    author_email = "jacob@jacobian.org",
    url = "http://github.com/jacobian/valor",
    py_modules = ['valor'],
    install_requires = ['requests>=2.3', 'jsonpointer>=1.4', 'six>=1.7.3'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP'
    ]
)

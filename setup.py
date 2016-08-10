"""
A permission flask extension inspired by Django.
"""

from setuptools import setup


setup(
    name='Flask-Perm',
    version='0.1.0',
    url='https://github.com/xiewenlongs/flask_perm_2',
    license='MIT',
    author='Ju Lin',
    author_email='soasme@gmail.com',
    description='Flask Authentication Contrib',
    long_description=__doc__,
    packages=['flask_perm'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'Flask-SQLAlchemy',
    ],
    classifiers=[
        'Framework :: Flask',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)

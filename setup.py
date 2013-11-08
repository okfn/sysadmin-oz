from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='optzone',
    version=version,
    description="DNS Zone Optimiser",
    long_description="""\
DNS Zone Optimiser

Rearrange A and CNAME records for sanity.
""",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    keywords="dns",
    author='William Waites',
    author_email='ww@eris.okfn.org',
    url="http://eris.okfn.org/ww/optzone/",
    license='GPLv3',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
	"dnspython",
        "setuptools",
    ],
    entry_points="""
        # -*- Entry points: -*-
        [console_scripts]
        oz=oz.cmd:_cli
    """,
)

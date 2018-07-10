from setuptools import setup, find_packages

setup(
    name='rmi',
    version='0.0.1',
    author='Intel SSDG',
    description='Resource Mesos integrator',
    classifiers = [
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6',
        'Topic :: System :: Distributed Computing',
    ],
    install_requires=[
          'ruamel.yaml==0.15.37',
          'colorlog==3.1.4',
          'logging-tree==1.7',
          'dataclasses==0.6',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
          'pytest',
          'pytest-cov',
          'flake8'
    ],
    packages=find_packages(),
    python_requires=">=3.6",
    scripts=['bin/rmi']
)

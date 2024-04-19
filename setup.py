from setuptools import setup, find_packages

setup(
    name='gitGraber',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'requests==2.31.0',
        'argcomplete==3.2.1',
        'python_crontab==2.3.9',
        'termcolor==1.1.0'
        # Add any other dependencies your project requires
    ],
    entry_points={
        'console_scripts': [
            'gitGraber = gitGraber.gitGraber:main'
        ]
    },
    author='ThreatCode',
    author_email='infosulaiman@gmail.com',
    description='Description of your project',
    long_description='Long description of your project',
    url='https://github.com/threatcode/gitGraber',
    license='MIT',  # Changed to MIT license
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Updated license classifier
        'Operating System :: OS Independent',
    ],
)

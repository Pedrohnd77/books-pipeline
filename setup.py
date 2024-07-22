from setuptools import setup, find_packages

setup(
    name='web_scraper_project',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'selenium',
        'boto3',
        'webdriver-manager',
    ],
    entry_points={
        'console_scripts': [
            'run-scraper=src.main:main',
        ],
    },
)

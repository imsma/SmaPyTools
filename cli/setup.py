from setuptools import setup, find_packages

setup(
    name='cli',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'click>=8.0'  # This package is required for image processing
    ],
    author='Shoket Mahmood Ahmed',
    author_email='hello@sma.im',
    description='A simple image to Base64 converter',
    keywords='image base64 converter',
    url='https://github.com/imsma/SmaPyTools'  # URL to your project's repository
)

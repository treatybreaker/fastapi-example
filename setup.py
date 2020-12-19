from setuptools import setup, find_packages

setup(
    name='fastapi-example',
    version='0.0.1',
    packages=find_packages(),
    url='',
    license='BSD-3',
    author='Price Hiller',
    author_email='philler3138@gmail.com',
    description='A simple fastapi app capable of serving webpages with routers support',
    install_requires=[
        'uvicorn',
        'setuptools',
        'fastapi',
        'aiofiles'
    ]
)

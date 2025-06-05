from setuptools import setup, find_packages

setup(
    name='sampah',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    author='Amirul Sadikin',
    author_email='ai.amirul.sadikin@gmail.com',
    description='SAMPAH – Smart Annotation Management Platform for Adaptive Handling',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/yourrepo',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.12',
)

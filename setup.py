from setuptools import setup, find_packages


with open('README.rst', 'r') as fp:
    long_description = fp.read()

setup(
    name='webclient-helper',
    version='0.0.4',
    description='Helpful WebClient class to interact with APIs on the web',
    long_description=long_description,
    author='Ken',
    author_email='kenjyco@gmail.com',
    license='MIT',
    url='https://github.com/kenjyco/webclient-helper',
    download_url='https://github.com/kenjyco/webclient-helper/tarball/v0.0.4',
    packages=find_packages(),
    install_requires=[
        'fs-helper',
        'input-helper',
        'requests',
        'urllib3',
        'xmljson',
    ],
    extras_require={
        'bs4': ['beautifulsoup4', 'lxml'],
    },
    include_package_data=True,
    package_dir={'': '.'},
    package_data={
        '': ['*.ini'],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries',
        'Intended Audience :: Developers',
    ],
    keywords=['webclient', 'requests', 'soup', 'beautifulsoup', 'lxml', 'helper']
)

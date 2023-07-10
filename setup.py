from setuptools import setup, find_packages


with open('README.rst', 'r') as fp:
    long_description = fp.read()

with open('requirements.txt', 'r') as fp:
    requirements = fp.read().splitlines()

with open('requirements-bs4.txt', 'r') as fp:
    requirements_bs4 = fp.read().splitlines()

setup(
    name='webclient-helper',
    version='0.0.6',
    description='Helpful WebClient class to interact with APIs on the web',
    long_description=long_description,
    author='Ken',
    author_email='kenjyco@gmail.com',
    license='MIT',
    url='https://github.com/kenjyco/webclient-helper',
    download_url='https://github.com/kenjyco/webclient-helper/tarball/v0.0.6',
    packages=find_packages(),
    install_requires=requirements,
    extras_require={
        'bs4': requirements_bs4,
    },
    include_package_data=True,
    package_dir={'': '.'},
    package_data={
        '': ['*.ini'],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Topic :: Text Processing :: Markup :: HTML',
        'Topic :: Text Processing :: Markup :: XML',
        'Topic :: Utilities',
    ],
    keywords=['webclient', 'api', 'requests', 'soup', 'beautifulsoup', 'lxml', 'http', 'rest', 'helper', 'kenjyco']
)

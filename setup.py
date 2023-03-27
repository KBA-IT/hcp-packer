from setuptools import setup, find_packages

setup(
    name='HCP-Packer',
    version='0.0.3',
    license='MIT',
    author="Billy Austin",
    author_email="billy@kba-it.com",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url="https://github.com/KBA-IT/hcp-packer",
    keywords="Hashicorp Packer",
    install_requires=[],
)

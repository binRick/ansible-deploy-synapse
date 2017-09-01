#!/bin/sh
virtualenv -p python2.7 /opt/synapse
source /opt/synapse/bin/activate
pip install --upgrade pip
pip install --upgrade setuptools
pip install https://github.com/matrix-org/synapse/tarball/master

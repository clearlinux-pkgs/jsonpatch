#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jsonpatch
Version  : 1.11
Release  : 14
URL      : https://pypi.python.org/packages/source/j/jsonpatch/jsonpatch-1.11.tar.gz
Source0  : https://pypi.python.org/packages/source/j/jsonpatch/jsonpatch-1.11.tar.gz
Summary  : Apply JSON-Patches (RFC 6902)
Group    : Development/Tools
License  : BSD-3-Clause
Requires: jsonpatch-bin
Requires: jsonpatch-python
BuildRequires : jsonpointer
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
python-json-patch [![Build Status](https://secure.travis-ci.org/stefankoegl/python-json-patch.png?branch=master)](https://travis-ci.org/stefankoegl/python-json-patch) [![Coverage Status](https://coveralls.io/repos/stefankoegl/python-json-patch/badge.png?branch=master)](https://coveralls.io/r/stefankoegl/python-json-patch?branch=master) ![Downloads](https://pypip.in/d/jsonpatch/badge.png) ![Version](https://pypip.in/v/jsonpatch/badge.png)
=================
Applying JSON Patches in Python
-------------------------------

%package bin
Summary: bin components for the jsonpatch package.
Group: Binaries

%description bin
bin components for the jsonpatch package.


%package python
Summary: python components for the jsonpatch package.
Group: Default

%description python
python components for the jsonpatch package.


%prep
%setup -q -n jsonpatch-1.11

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python tests.py
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jsondiff
/usr/bin/jsonpatch

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*

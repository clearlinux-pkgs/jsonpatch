#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jsonpatch
Version  : 1.15
Release  : 28
URL      : http://pypi.debian.net/jsonpatch/jsonpatch-1.15.tar.gz
Source0  : http://pypi.debian.net/jsonpatch/jsonpatch-1.15.tar.gz
Summary  : Apply JSON-Patches (RFC 6902)
Group    : Development/Tools
License  : BSD-3-Clause
Requires: jsonpatch-bin
Requires: jsonpatch-python
Requires: jsonpointer
BuildRequires : jsonpointer
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
========================================================================
        
        Applying JSON Patches in Python
        -------------------------------
        
        Library to apply JSON Patches according to `RFC

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
%setup -q -n jsonpatch-1.15

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1503094051
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python tests.py
%install
export SOURCE_DATE_EPOCH=1503094051
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jsondiff
/usr/bin/jsonpatch

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*

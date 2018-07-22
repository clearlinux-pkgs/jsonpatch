#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jsonpatch
Version  : 1.23
Release  : 31
URL      : https://files.pythonhosted.org/packages/9a/7d/bcf203d81939420e1aaf7478a3efce1efb8ccb4d047a33cb85d7f96d775e/jsonpatch-1.23.tar.gz
Source0  : https://files.pythonhosted.org/packages/9a/7d/bcf203d81939420e1aaf7478a3efce1efb8ccb4d047a33cb85d7f96d775e/jsonpatch-1.23.tar.gz
Summary  : Apply JSON-Patches (RFC 6902)
Group    : Development/Tools
License  : BSD-3-Clause
Requires: jsonpatch-bin
Requires: jsonpatch-python3
Requires: jsonpatch-license
Requires: jsonpatch-python
Requires: jsonpointer
BuildRequires : buildreq-distutils3
BuildRequires : jsonpointer
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

%description
=================
        
        |PyPI version| |Supported Python versions| |Build Status| |Coverage
        Status|
        
        Applying JSON Patches in Python
        -------------------------------
        
        Library to apply JSON Patches according to `RFC

%package bin
Summary: bin components for the jsonpatch package.
Group: Binaries
Requires: jsonpatch-license

%description bin
bin components for the jsonpatch package.


%package license
Summary: license components for the jsonpatch package.
Group: Default

%description license
license components for the jsonpatch package.


%package python
Summary: python components for the jsonpatch package.
Group: Default
Requires: jsonpatch-python3

%description python
python components for the jsonpatch package.


%package python3
Summary: python3 components for the jsonpatch package.
Group: Default
Requires: python3-core

%description python3
python3 components for the jsonpatch package.


%prep
%setup -q -n jsonpatch-1.23

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532243352
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python tests.py
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/jsonpatch
cp COPYING %{buildroot}/usr/share/doc/jsonpatch/COPYING
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jsondiff
/usr/bin/jsonpatch

%files license
%defattr(-,root,root,-)
/usr/share/doc/jsonpatch/COPYING

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

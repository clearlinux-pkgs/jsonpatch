#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jsonpatch
Version  : 1.25
Release  : 41
URL      : https://files.pythonhosted.org/packages/70/9f/6f0bfbb4cc1401ce994d336bcb4ed2aa924f395e7fd1926511c04a52eee1/jsonpatch-1.25.tar.gz
Source0  : https://files.pythonhosted.org/packages/70/9f/6f0bfbb4cc1401ce994d336bcb4ed2aa924f395e7fd1926511c04a52eee1/jsonpatch-1.25.tar.gz
Summary  : Apply JSON-Patches (RFC 6902)
Group    : Development/Tools
License  : BSD-3-Clause
Requires: jsonpatch-bin = %{version}-%{release}
Requires: jsonpatch-license = %{version}-%{release}
Requires: jsonpatch-python = %{version}-%{release}
Requires: jsonpatch-python3 = %{version}-%{release}
Requires: jsonpointer
BuildRequires : buildreq-distutils3
BuildRequires : jsonpointer

%description
python-json-patch
=================
[![PyPI version](https://img.shields.io/pypi/v/jsonpatch.svg)](https://pypi.python.org/pypi/jsonpatch/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/jsonpatch.svg)](https://pypi.python.org/pypi/jsonpatch/)
[![Build Status](https://travis-ci.org/stefankoegl/python-json-patch.png?branch=master)](https://travis-ci.org/stefankoegl/python-json-patch)
[![Coverage Status](https://coveralls.io/repos/stefankoegl/python-json-patch/badge.png?branch=master)](https://coveralls.io/r/stefankoegl/python-json-patch?branch=master)

%package bin
Summary: bin components for the jsonpatch package.
Group: Binaries
Requires: jsonpatch-license = %{version}-%{release}

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
Requires: jsonpatch-python3 = %{version}-%{release}

%description python
python components for the jsonpatch package.


%package python3
Summary: python3 components for the jsonpatch package.
Group: Default
Requires: python3-core
Provides: pypi(jsonpatch)

%description python3
python3 components for the jsonpatch package.


%prep
%setup -q -n jsonpatch-1.25
cd %{_builddir}/jsonpatch-1.25

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583161777
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python tests.py
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/jsonpatch
cp %{_builddir}/jsonpatch-1.25/COPYING %{buildroot}/usr/share/package-licenses/jsonpatch/0305317c0f694ba11e8f059938fd0c880356e7bc
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## Remove excluded files
rm -f %{buildroot}/usr/bin/jsondiff

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jsonpatch

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/jsonpatch/0305317c0f694ba11e8f059938fd0c880356e7bc

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

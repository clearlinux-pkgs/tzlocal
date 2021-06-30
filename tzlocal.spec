#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tzlocal
Version  : 2.1
Release  : 34
URL      : https://files.pythonhosted.org/packages/ce/73/99e4cc30db6b21cba6c3b3b80cffc472cc5a0feaf79c290f01f1ac460710/tzlocal-2.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/ce/73/99e4cc30db6b21cba6c3b3b80cffc472cc5a0feaf79c290f01f1ac460710/tzlocal-2.1.tar.gz
Summary  : tzinfo object for the local timezone
Group    : Development/Tools
License  : MIT
Requires: tzlocal-license = %{version}-%{release}
Requires: tzlocal-python = %{version}-%{release}
Requires: tzlocal-python3 = %{version}-%{release}
Requires: pytz
BuildRequires : buildreq-distutils3
BuildRequires : python-mock
BuildRequires : pytz

%description
=======
        
        This Python module returns a ``tzinfo`` object with the local timezone information under Unix and Win-32.
        It requires ``pytz``, and returns ``pytz`` ``tzinfo`` objects.
        
        This module attempts to fix a glaring hole in ``pytz``, that there is no way to
        get the local timezone information, unless you know the zoneinfo name, and
        under several Linux distros that's hard or impossible to figure out.
        
        Also, with Windows different timezone system using pytz isn't of much use
        unless you separately configure the zoneinfo timezone name.
        
        With ``tzlocal`` you only need to call ``get_localzone()`` and you will get a
        ``tzinfo`` object with the local time zone info. On some Unices you will still
        not get to know what the timezone name is, but you don't need that when you
        have the tzinfo file. However, if the timezone name is readily available it
        will be used.
        
        
        Supported systems
        -----------------

%package license
Summary: license components for the tzlocal package.
Group: Default

%description license
license components for the tzlocal package.


%package python
Summary: python components for the tzlocal package.
Group: Default
Requires: tzlocal-python3 = %{version}-%{release}

%description python
python components for the tzlocal package.


%package python3
Summary: python3 components for the tzlocal package.
Group: Default
Requires: python3-core
Provides: pypi(tzlocal)
Requires: pypi(pytz)

%description python3
python3 components for the tzlocal package.


%prep
%setup -q -n tzlocal-2.1
cd %{_builddir}/tzlocal-2.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1625012607
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/tzlocal
cp %{_builddir}/tzlocal-2.1/LICENSE.txt %{buildroot}/usr/share/package-licenses/tzlocal/d0e0745ad05aba07ac3481313b59665d4a36017c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tzlocal/d0e0745ad05aba07ac3481313b59665d4a36017c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

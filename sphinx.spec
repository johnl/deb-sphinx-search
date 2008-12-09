Summary: Sphinx full-text search engine
Name: sphinx
Version: 0.9.8.1
Release: r1533
License: GPL
Group: Development
BuildRoot: /tmp/sphinx-%{version}
Source: http://sphinxsearch.com/downloads/sphinx-%{version}.tar.gz
URL: http://sphinxsearch.com/
BuildRequires: mysql-devel
Requires: mysql


%description 
Sphinx is a free, open-source full-text search engine,
designed with indexing database content in mind.


%prep
%setup -n sphinx-%{version}


%build
CPPFLAGS="-D_FILE_OFFSET_BITS=64"
export CPPFLAGS
%configure
make


%install
mkdir -p $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/sphinx
cp -R -p api $RPM_BUILD_ROOT/%{_libdir}/sphinx


%files
/usr/bin/*
%{_libdir}/sphinx
%config /etc/*
%doc INSTALL doc/sphinx.*


%clean
rm -rf $RPM_BUILD_ROOT

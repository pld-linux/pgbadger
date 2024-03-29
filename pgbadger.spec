Summary:	a fast PostgreSQL log analyzer
Name:		pgbadger
Version:	12.1
Release:	1
License:	BSD
Group:		Applications/Databases
Source0:	https://github.com/darold/pgbadger/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	a602077e7f5d5bfe19ade2bf85dc4610
URL:		https://pgbadger.darold.net/
Patch0:		%{name}-perl_path.patch
BuildRequires:	perl-devel >= 1:5.6
BuildRequires:	perl-ExtUtils-MakeMaker
Requires:	perl-base >= 1:5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
pgBadger is a PostgreSQL log analyzer build for speed with fully
detailed reports from your PostgreSQL log file. It's a single and
small Perl script that aims to replace and outperform the old php
script pgFouine.

pgBadger is written in pure Perl language. It uses a javascript
library to draw graphs so that you don't need additional Perl modules
or any other package to install. Furthermore, this library gives us
more features such as zooming.

pgBadger is able to autodetect your log file format (syslog, stderr or
csvlog). It is designed to parse huge log files as well as gzip
compressed file.

%prep
%setup -q
%patch0

%build
%{__perl} Makefile.PL \
		INSTALLDIRS=vendor

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


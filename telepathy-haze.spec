Summary:	A Telepathy connection manager using libpurple
Summary(pl.UTF-8):	Zarządca połączeń Telepathy używający biblioteki libpurple
Name:		telepathy-haze
Version:	0.8.1
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	https://telepathy.freedesktop.org/releases/telepathy-haze/%{name}-%{version}.tar.gz
# Source0-md5:	bdc5c30762ddebf24c4da05e023c9072
URL:		https://telepathy.freedesktop.org/components/telepathy-haze
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-glib-devel >= 0.73
BuildRequires:	glib2-devel >= 1:2.22
BuildRequires:	libpurple-devel >= 2.10.12
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3.2
BuildRequires:	sed >= 4.0
BuildRequires:	telepathy-glib-devel >= 0.15.1
Requires:	dbus-glib >= 0.73
Requires:	glib2 >= 1:2.22
Requires:	libpurple >= 2.10.12
Requires:	telepathy-glib >= 0.15.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A connection manager to connect Telepathy to any of the protocols
supported by pidgin's libpurple.

%description -l pl.UTF-8
Zarządca połączeń pozwalający połączyć się Telepathy z każdym
protokołem wspieranym przez bibliotekę libpurple.

%prep
%setup -q

%{__sed} -i -e '1s,/usr/bin/python$,%{__python3},' tools/*.py

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	PYTHON="%{__python3}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_libdir}/telepathy-haze
%{_mandir}/man8/telepathy-haze.8*
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.haze.service

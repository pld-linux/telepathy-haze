Summary:	A Telepathy connection manager using libpurple
Summary(pl.UTF-8):	Zarządca połączeń Telepathy używający biblioteki libpurple
Name:		telepathy-haze
Version:	0.3.4
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://telepathy.freedesktop.org/releases/telepathy-haze/%{name}-%{version}.tar.gz
# Source0-md5:	100b022f14165c2097f530139a02693b
URL:		http://telepathy.freedesktop.org/wiki/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-glib-devel >= 0.73
BuildRequires:	libpurple-devel >= 2.1.1
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRequires:	telepathy-glib-devel >= 0.7.36
Requires:	telepathy-glib >= 0.7.36
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A connection manager to connect Telepathy to any of the protocols
supported by pidgin's libpurple.

%description -l pl.UTF-8
Zarządca połączeń pozwalający połączyć się Telepathy z każdym
protokołem wspieranym przez bibliotekę libpurple.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
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
%{_mandir}/man8/*
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.haze.service
%{_datadir}/telepathy/managers/haze.manager

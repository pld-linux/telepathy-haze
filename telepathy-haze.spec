Summary:	A Telepathy connection manager using libpurple
Name:		telepathy-haze
Version:	0.2.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://telepathy.freedesktop.org/releases/telepathy-haze/%{name}-%{version}.tar.gz
# Source0-md5:	63bb7d0f9c45be27d5cec478f9f61846
URL:		http://telepathy.freedesktop.org/wiki/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.8
BuildRequires:	dbus-glib-devel >= 0.61
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	pidgin-devel
BuildRequires:	pkgconfig
BuildRequires:	telepathy-glib-devel >= 0.5.13-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A connection manager to connect Telepathy to any of the protocols
supported by pidgin's libpurple.

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
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/telepathy-haze
%{_mandir}/man8/*
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.haze.service
%{_datadir}/telepathy/managers/haze.manager

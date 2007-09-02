Summary:	OpenSync Evolution plugin
Summary(pl.UTF-8):	Wtyczka Evolution do OpenSync
Name:		libopensync-plugin-evolution
Version:	0.22
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.opensync.org/attachment/wiki/download/%{name}2-%{version}.tar.bz2?format=raw
# Source0-md5:	c4419dd2451bd1595fe42fcf96a9ba45
URL:		http://www.opensync.org/
BuildRequires:	evolution-data-server-devel >= 1.2
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libopensync-devel >= %{version}
BuildRequires:	pkgconfig
Obsoletes:	multisync-evolution
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenSync is a synchronization framework that is platform and distribution
independent.

It consists of several plugins that can be used to connect to devices,
a powerful sync-engine and the framework itself.

This package contains Evolution plugin for OpenSync framework.

%description -l pl.UTF-8
OpenSync to niezależny od platformy i dystrybucji szkielet do
synchronizacji danych.

Składa się z różnych wtyczek, których można używać do łączenia z
urządzeniami, potężnego silnika synchronizacji oraz samego szkieletu.

Ten pakiet zawiera wtyczkę Evolution dla szkieletu OpenSync.

%prep
%setup -q -n %{name}2-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/opensync/plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/opensync/plugins/evo2_sync.so
%{_datadir}/opensync/defaults/evo2-sync

# devel
#%{_includedir}/opensync-1.0/opensync/evo2_sync.h

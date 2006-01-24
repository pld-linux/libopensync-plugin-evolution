Summary:	OpenSync Evolution plugin
Summary(pl):	Wtyczka Evolution do OpenSync
Name:		libopensync-plugin-evolution
Version:	0.18
Release:	0.1
License:	LGPL
Group:		Libraries
Source0:	http://www.opensync.org/attachment/wiki/download/%{name}2-%{version}.tar.gz?format=raw
# Source0-md5:	64f182fa37483419ca09721dec2d6f1e
URL:		http://www.opensync.org/
BuildRequires:	evolution-devel
BuildRequires:	libopensync-devel
Obsoletes:	multisync-evolution
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenSync is a synchronization framework that is platform and distribution
independent.

It consists of several plugins that can be used to connect to devices,
a powerful sync-engine and the framework itself.

This package contains Evolution plugin for OpenSync framework.

%description -l pl
OpenSync to niezale¿ny od platformy i dystrybucji szkielet do
synchronizacji danych.

Sk³ada siê z ró¿nych wtyczek, których mo¿na u¿ywaæ do ³±czenia z
urz±dzeniami, potê¿nego silnika synchronizacji oraz samego szkieletu.

Ten pakiet zawiera wtyczkê Evolution dla szkieletu OpenSync.

%prep
%setup -q -n %{name}2-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/opensync/plugins/*.so
%{_libdir}/opensync/plugins/*.la
%{_datadir}/opensync/defaults/*

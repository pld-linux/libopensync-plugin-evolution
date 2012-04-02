Summary:	OpenSync Evolution plugin
Summary(pl.UTF-8):	Wtyczka Evolution do OpenSync
Name:		libopensync-plugin-evolution
Version:	0.39
Release:	4
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.opensync.org/download/releases/%{version}/%{name}2-%{version}.tar.bz2
# Source0-md5:	54d2fc3c80c29f3ac5feb609b082c99d
URL:		http://www.opensync.org/
BuildRequires:	cmake
BuildRequires:	evolution-data-server-devel >= 1.2
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libopensync-devel >= 1:%{version}
BuildRequires:	pkgconfig
Obsoletes:	multisync-evolution
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenSync is a synchronization framework that is platform and
distribution independent.

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
mkdir build
cd build
%cmake .. \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" != "lib"
	-DLIB_SUFFIX=64
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/opensync/plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/libopensync1/formats/evo2-format.so
%attr(755,root,root) %{_libdir}/libopensync1/plugins/evo2-sync.so
%{_datadir}/libopensync1/defaults/evo2-sync

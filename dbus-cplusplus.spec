Name:		dbus-cplusplus
Summary:	C++ Interface for DBus - with Google Chromiumos and Napatech patches
Version:	0.10.0
Release:        %{?buildnum}%{!?buildnum:0}%{?dist}
URL:		https://github.com/napatech/%{name}/
License:	LGPL
Source: 	https://github.com/napatech/%{name}/releases/%{version}.tar.gz
Group:		Libraries
BuildRequires:  nt-ctemplate-devel
Requires:       nt-ctemplate
Conflicts:      dbus-c++

%description

Ability to reflect dbus methods and signals into a more natural C++ object system.

%package devel
Requires:	%{name} = %{version} nt-ctemplate
Group:		Development/Libraries
Summary:	Header files for dbus-cplusplus

%description devel
Header files for dbus-cplusplus

%prep
%setup -q

%build
scl enable devtoolset-7 "./autogen.sh \
--prefix=%{_prefix} \
--exec-prefix=%{_exec_prefix} \
--bindir=%{_bindir} \
--sbindir=%{_sbindir} \
--sysconfdir=%{_sysconfdir} \
--datadir=%{_datadir} \
--includedir=%{_includedir} \
--libdir=%{_libdir} \
--libexecdir=%{_libexecdir} \
--localstatedir=%{_localstatedir} \
--sharedstatedir=%{_sharedstatedir} \
--mandir=%{_mandir} \
--infodir=%{_infodir} \
--enable-glib \
CPPFLAGS=-I%{_includedir} \
LDFLAGS=-L%{_libdir}"
scl enable devtoolset-7 make

%install
rm -rf $RPM_BUILD_ROOT
scl enable devtoolset-7 "make DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p' install"

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(755,root,root)
%{_libdir}/libdbus-c*.so*

%files devel
%defattr(-,root,root)
%{_bindir}/dbusxx-xml2cpp
%{_bindir}/dbusxx-introspect
%{_libdir}/libdbus-c*.a
%{_libdir}/libdbus-c*.la
%{_libdir}/pkgconfig/*.pc
%{_includedir}/dbus-c++-1
%{_prefix}/share/libdbus-c++/*.tpl

%changelog
* Thu Feb 8 2007 Ben Martin
- initial spec file

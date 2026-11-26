Summary:	Portable implementation of the kqueue() and kevent() system calls
Summary(pl.UTF-8):	Przenośna implementacja wywołań systemowych kqueue() i kevent()
Name:		libkqueue
Version:	2.7.0
Release:	2
License:	BSD (header), ISC (implementation)
Group:		Libraries
#Source0Download: https://github.com/mheily/libkqueue/releases
Source0:	https://github.com/mheily/libkqueue/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	f08b6a3dede0576e4e40e325ed98249f
Patch0:		%{name}-format.patch
URL:		https://github.com/mheily/libkqueue
BuildRequires:	cmake >= 3.0
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libkqueue is a portable userspace implementation of the kqueue(2)
kernel event notification mechanism found in FreeBSD and other
BSD-based operating systems. The library translates between the kevent
structure and the native kernel facilities of the host machine.

%description -l pl.UTF-8
libkqueue to przenośna implementacja w przestrzeni użytkownika
mechanizmu powiadomień o zdarzeniach kqueue(2) obecnego w jądrach
FreeBSD i innych systemach operacyjnych opartych na BSD. Biblioteka
dokonuje tłumaczenia między strukturą kevent a natywnymi mechanizmami
jądra systemu, na którym działa.

%package devel
Summary:	Header files for libkqueue library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libkqueue
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libkqueue library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libkqueue.

%package static
Summary:	Static libkqueue library
Summary(pl.UTF-8):	Statyczna biblioteka libkqueue
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libkqueue library.

%description static -l pl.UTF-8
Statyczna biblioteka libkqueue.

%prep
%setup -q
%patch -P0 -p1

%build
# 2.7.0 tarball still hardcodes PROJECT_VERSION 2.6.3 (ends up in libkqueue.pc)
%cmake -B build \
	-DVERSION_OVERRIDE=%{version} \
	-DENABLE_SHARED=ON \
	-DENABLE_STATIC=ON

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE
%attr(755,root,root) %{_libdir}/libkqueue.so.0

%files devel
%defattr(644,root,root,755)
%{_libdir}/libkqueue.so
%{_includedir}/kqueue
%{_pkgconfigdir}/libkqueue.pc
%{_mandir}/man2/kqueue.2*

%files static
%defattr(644,root,root,755)
%{_libdir}/libkqueue.a

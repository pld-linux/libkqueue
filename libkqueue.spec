Summary:	Portable implementation of the kqueue() and kevent() system calls
Summary(pl.UTF-8):	Przenośna implementacja wywołań systemowych kqueue() i kevent()
Name:		libkqueue
Version:	2.0.1
Release:	1
License:	BSD (header), MIT-like (implementation)
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libkqueue/%{name}-%{version}.tar.gz
# Source0-md5:	3d939aa5fa83a870aee71f2181b22994
URL:		http://sourceforge.net/projects/libkqueue/
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

%build
# NOTE: not autoconf configure
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
CPPFLAGS="%{rpmcppflags}" \
LDFLAGS="%{rpmldflags}" \
./configure \
	--build=%{_target_platform} \
	--prefix=%{_prefix} \
	--libdir=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install libkqueue.a $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE
%attr(755,root,root) %{_libdir}/libkqueue.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libkqueue.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkqueue.so
%{_includedir}/kqueue
%{_pkgconfigdir}/libkqueue.pc
%{_mandir}/man2/kevent.2*
%{_mandir}/man2/kqueue.2*

%files static
%defattr(644,root,root,755)
%{_libdir}/libkqueue.a

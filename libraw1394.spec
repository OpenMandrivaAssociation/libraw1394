%define	name	libraw1394
%define	version	1.2.2
%define svn	172
%if %svn
%define	release	%mkrel 0.%svn.2
%else
%define release	%mkrel 1
%endif

%define	major		8
%define	libname		%mklibname raw1394_ %{major}
%define	develname	%mklibname raw1394 -d
%define staticname	%mklibname raw1394 -d -s

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	LGPLv2+
Group:		System/Libraries
%if %svn
Source0:	%{name}-%{svn}.tar.bz2
%else
Source0:	http://download.sourceforge.net/libraw1394/%{name}-%{version}.tar.bz2
%endif
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://www.linux1394.org/
Summary:	FireWire interface
Requires(post): coreutils

%description
libraw1394 is the only supported interface to the kernel side raw1394 of
the Linux IEEE-1394 subsystem, which provides direct access to the connected
1394 buses to user space.  Through libraw1394/raw1394, applications can
directly send to and receive from other nodes without requiring a kernel driver
for the protocol in question.

The reason for making a library the interface to the kernel is to avoid
a program dependency on the kernel version, which would hinder development and
optimization of raw1394.  If development changed the protocol and made it
incompatible with previous versions only the libraw1394 has to be upgraded to
match the kernel version (instead of all applications).

%package -n	%{name}-utils
Group:		Communications
Summary:	Some small Firewire utilities

%description -n	%{name}-utils
This package contains a few utilities to send and receive raw data over
Firewire (ieee1394).

%package -n	%{libname}
Group:		System/Libraries
Summary:	FireWire interface shared library

%description -n %{libname}
libraw1394 is the only supported interface to the kernel side raw1394 of
the Linux IEEE-1394 subsystem, which provides direct access to the connected
1394 buses to user space.  Through libraw1394/raw1394, applications can
directly send to and receive from other nodes without requiring a kernel driver
for the protocol in question.

The reason for making a library the interface to the kernel is to avoid
a program dependency on the kernel version, which would hinder development and
optimization of raw1394.  If development changed the protocol and made it
incompatible with previous versions only the libraw1394 has to be upgraded to
match the kernel version (instead of all applications).

This package contains the shared library to run applications linked
with %{name}.

%package -n	%{develname}
Summary:	Development and include files for libraw1394
Summary(pt_BR):	Arquivos de desenvolvimento e cabe?alhos para o libraw1394
Summary(es):	Development and include files for libraw1394
Group:		Development/C
Group(pt_BR):	Desenvolvimento
Group(es):	Desarrollo
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname raw1394_8 -d}

%description -n	%{develname}
libraw1394 is the only supported interface to the kernel side raw1394 of
the Linux IEEE-1394 subsystem, which provides direct access to the connected
1394 buses to user space.  Through libraw1394/raw1394, applications can
directly send to and receive from other nodes without requiring a kernel driver
for the protocol in question.

This archive contains the header-files for libraw1394 development.


%package -n	%{staticname}
Summary:	Development components for libraw1394
Summary(pt_BR):	Componentes est?ticos de desenvolvimento para o libraw1394
Summary(es):	Development components for libraw1394
Group:		Development/C
Group(pt_BR):	Desenvolvimento
Group(es):	Desarrollo
Requires:	%{develname} = %{version}-%{release}
Obsoletes:	%{mklibname raw1394_8 -d -s}

%description -n	%{staticname}
libraw1394 is the only supported interface to the kernel side raw1394 of
the Linux IEEE-1394 subsystem, which provides direct access to the connected
1394 buses to user space.  Through libraw1394/raw1394, applications can
directly send to and receive from other nodes without requiring a kernel driver
for the protocol in question.

This archive contains the static libraries (.a) 


%prep
%setup -q -n %name

%build
%if %svn
./autogen.sh
%endif
%configure2_5x
%make

%install
rm -rf %{buildroot}
%{makeinstall_std}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files -n %name-utils
%defattr(-,root,root)
%doc README AUTHORS
%{_bindir}/*
%{_mandir}/man*/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libraw1394.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc README NEWS AUTHORS
%{_includedir}/libraw1394
%{_libdir}/libraw1394.so
%{_libdir}/libraw1394.la
%{_libdir}/pkgconfig/%{name}.pc

%files -n %{staticname}
%defattr(-,root,root)
%{_libdir}/libraw1394.a
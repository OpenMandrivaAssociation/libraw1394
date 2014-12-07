%define	major	11
%define	libname	%mklibname raw1394_ %{major}
%define	devname	%mklibname raw1394 -d

Summary:	FireWire interface
Name:		libraw1394
Version:	2.1.0
Release:	12
License:	LGPLv2+
Group:		System/Libraries
Url:		http://sourceforge.net/projects/libraw1394/
Source0:	http://www.kernel.org/pub/linux/libs/ieee1394/%{name}-%{version}.tar.xz
Requires(post):	coreutils

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

%package -n	%{devname}
Summary:	Development and include files for libraw1394
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname raw1394 -d -s} < 2.0.8

%description -n	%{devname}
This archive contains the header-files for libraw1394 development.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files -n %{name}-utils
%doc README AUTHORS
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*

%files -n %{libname}
%{_libdir}/libraw1394.so.%{major}*

%files -n %{devname}
%doc README NEWS AUTHORS
%{_includedir}/libraw1394
%{_libdir}/libraw1394.so
%{_libdir}/pkgconfig/%{name}.pc


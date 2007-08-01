%define	name	libraw1394
%define	version	1.2.1
%define	release	%mkrel 1

%define	major	8
%define	libname	%mklibname raw1394_ %{major}
%define	libnamedev %{libname}-devel

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Libraries
Source0:	http://download.sourceforge.net/libraw1394/%{name}-%{version}-svn160.tar.bz2
# required for freebob support (austin)
Patch0:		libraw1394-svn160-freebob_iso_again.patch.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://www.linux1394.org/
Summary:	FireWire interface
Summary(pt_BR):	FireWire interface
Summary(es):	FireWire interface
Requires(post): coreutils
Requires(post): ldconfig
Requires(postun): ldconfig

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

%package -n	%{libnamedev}
Summary:	Development and include files for libraw1394
Summary(pt_BR):	Arquivos de desenvolvimento e cabe?alhos para o libraw1394
Summary(es):	Development and include files for libraw1394
Group:		Development/C
Group(pt_BR):	Desenvolvimento
Group(es):	Desarrollo
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{libnamedev}
libraw1394 is the only supported interface to the kernel side raw1394 of
the Linux IEEE-1394 subsystem, which provides direct access to the connected
1394 buses to user space.  Through libraw1394/raw1394, applications can
directly send to and receive from other nodes without requiring a kernel driver
for the protocol in question.

This archive contains the header-files for libraw1394 development.


%package -n	%{libname}-static-devel
Summary:	Development components for libraw1394
Summary(pt_BR):	Componentes est?ticos de desenvolvimento para o libraw1394
Summary(es):	Development components for libraw1394
Group:		Development/C
Group(pt_BR):	Desenvolvimento
Group(es):	Desarrollo
Requires:	%{libname}-devel = %{version}-%{release}

%description -n	%{libname}-static-devel
libraw1394 is the only supported interface to the kernel side raw1394 of
the Linux IEEE-1394 subsystem, which provides direct access to the connected
1394 buses to user space.  Through libraw1394/raw1394, applications can
directly send to and receive from other nodes without requiring a kernel driver
for the protocol in question.

This archive contains the static libraries (.a) 


%prep
%setup -q -n %name
%patch0

%build
./autogen.sh
%configure2_5x
%make

%install
rm -rf %{buildroot}
%{makeinstall_std}

%post -n %libname
/sbin/ldconfig
if [ $1 -eq 1 -a ! -e /dev/raw1394 ] 
then 
mknod -m 600 /dev/raw1394 c 171 0
chown root.root /dev/raw1394
echo
echo "/dev/raw1394 created"
echo "It is owned by root with permissions 600.  You may want to fix"
echo "the group/permission to something appropriate for you."
echo "Note however that anyone who can open raw1394 can access all"
echo "devices on all connected 1394 buses unrestricted, including"
echo "harddisks and other probably sensitive devices."
echo
fi


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
%{_libdir}/libraw1394.so.%{major}.*
%{_libdir}/libraw1394.so.%{major}

%files -n %{libnamedev}
%defattr(-,root,root)
%doc README NEWS INSTALL COPYING.LIB AUTHORS
%{_includedir}/libraw1394
%{_libdir}/libraw1394.so
%{_libdir}/libraw1394.la
%{_libdir}/pkgconfig/%{name}.pc

%files -n %{libname}-static-devel
%defattr(-,root,root)
%{_libdir}/libraw1394.a

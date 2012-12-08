%define	major		11
%define	libname		%mklibname raw1394_ %{major}
%define	develname	%mklibname raw1394 -d

Name:		libraw1394
Version:	2.0.8
Release:	2
Summary:	FireWire interface
License:	LGPLv2+
Group:		System/Libraries
URL:		http://sourceforge.net/projects/libraw1394/
Source0:	http://dfn.dl.sourceforge.net/project/libraw1394/libraw1394/%{name}-%{version}.tar.xz
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

%package -n	%{develname}
Summary:	Development and include files for libraw1394
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Conflicts:	%{mklibname raw1394_8 -d}
Obsoletes:	%{mklibname raw1394 -d -s} < 2.0.8

%description -n	%{develname}
libraw1394 is the only supported interface to the kernel side raw1394 of
the Linux IEEE-1394 subsystem, which provides direct access to the connected
1394 buses to user space.  Through libraw1394/raw1394, applications can
directly send to and receive from other nodes without requiring a kernel driver
for the protocol in question.

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
%{_mandir}/man*/*

%files -n %{libname}
%{_libdir}/libraw1394.so.%{major}*

%files -n %{develname}
%doc README NEWS AUTHORS
%{_includedir}/libraw1394
%{_libdir}/libraw1394.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Wed Mar 07 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.0.8-1
+ Revision: 782762
- version update 2.0.8

* Mon Feb 20 2012 Götz Waschk <waschk@mandriva.org> 2.0.6-4
+ Revision: 778234
- rebuild

* Sat Dec 31 2011 Frank Kober <emuse@mandriva.org> 2.0.6-3
+ Revision: 748490
- Rebuild removing static lib and libtool archive

* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 2.0.6-2
+ Revision: 660278
- mass rebuild

* Tue Nov 02 2010 Thomas Backlund <tmb@mandriva.org> 2.0.6-1mdv2011.0
+ Revision: 591909
- update to 2.0.6

* Fri Jan 15 2010 Emmanuel Andry <eandry@mandriva.org> 2.0.5-1mdv2010.1
+ Revision: 491783
- New version 2.0.5

* Sun Nov 15 2009 Funda Wang <fwang@mandriva.org> 2.0.4-1mdv2010.1
+ Revision: 466185
- new version 2.0.4

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.0.2-2mdv2010.0
+ Revision: 425693
- rebuild

* Fri Feb 13 2009 Emmanuel Andry <eandry@mandriva.org> 2.0.2-1mdv2009.1
+ Revision: 340123
- New version 2.0.2

* Mon Jan 26 2009 Emmanuel Andry <eandry@mandriva.org> 2.0.1-1mdv2009.1
+ Revision: 333808
- New version 2.0.1

* Tue Jan 06 2009 Götz Waschk <waschk@mandriva.org> 2.0.0-2mdv2009.1
+ Revision: 325307
- don't obsolete old devel packages

* Sun Dec 28 2008 Emmanuel Andry <eandry@mandriva.org> 2.0.0-1mdv2009.1
+ Revision: 320339
- New version
- New major

* Mon Jun 09 2008 Pixel <pixel@mandriva.com> 1.3.0-2mdv2009.0
+ Revision: 217191
- do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Nov 14 2007 Funda Wang <fwang@mandriva.org> 1.3.0-2mdv2008.1
+ Revision: 108815
- rebuild

* Sun Oct 28 2007 Funda Wang <fwang@mandriva.org> 1.3.0-1mdv2008.1
+ Revision: 102726
- New version 1.3.0

* Thu Sep 06 2007 Adam Williamson <awilliamson@mandriva.org> 1.2.2-0.172.2mdv2008.0
+ Revision: 80742
- correct license to LGPLv2+

  + Thierry Vignaud <tv@mandriva.org>
    - kill ldconfig require as requested by pixel

* Wed Aug 01 2007 Adam Williamson <awilliamson@mandriva.org> 1.2.2-0.172.1mdv2008.0
+ Revision: 57360
- rebuild for 2008
- no need to package COPYING and INSTALL
- don't create /dev node manually (udev handles it)
- correct license to LGPLv2.1
- new devel policy
- drop patch0 (merged upstream)
- spec clean
- switch to a proper version scheme (was previously using svn, but undeclared)
- update to svn snapshot 172
- Import libraw1394


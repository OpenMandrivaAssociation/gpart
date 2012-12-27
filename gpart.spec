Summary:	Hard disk primary partition table reconstruction
Name:		gpart
Version:	0.1h
Release:	17
License:	GPLv2+
Source0:	%{name}-%{version}.tar.bz2
Group:		System/Kernel and hardware
URL:		http://home.pages.de/~michab/gpart/
Patch0:		gpart-0.1h-mdkconf.patch
Patch1:		gpart-errno.patch
Patch2:		gpart-0.1h-fixes.patch
Patch3:		gpart-0.1h-optflags.patch
Patch4:		gpart-0.1h-open-mode.patch
# Fedora patches
Patch100:	gpart-0.1h-cflags.patch
Patch101:	gpart-0.1h-errno.patch
Patch102:	gpart-0.1h-largefile.patch
Patch103:	gpart-0.1h-makefile.patch
Patch104:	gpart-0.1h-syscall.patch
Patch105:	gpart-0.1h-varname.patch

%description
A tool which tries to guess the primary partition table of a PC-type hard disk
in case the primary partition table in sector 0 is damaged, incorrect or
deleted. The guessed table can be written to a file or device. Supported
(guessable) filesystem or partition types: DOS/Windows FAT, Linux ext2 and
swap, OS/2 HPFS, Windows NTFS, FreeBSD and Solaris/x86 disklabels, Minix FS,
QNX 4 FS, Reiser FS, LVM physical volumes, BeOS FS, SGI XFS.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1 -b .fixes~
%patch100 -p1 -b .varname~
%patch101 -p1 -b .cflags~
%patch102 -p1 -b .errno~
%patch103 -p1 -b .syscall~
%patch104 -p1 -b .largefile~
%patch105 -p1 -b .makefile~
%patch3 -p1 -b .optflags~
%patch4 -p1 -b openmode~

%build
%make OPTFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
install -m755 src/%{name} -D %{buildroot}%{_bindir}/%{name}
install -m755 man/%{name}.8 -D %{buildroot}%{_mandir}/man8/%{name}.8

%files
%doc Changes README
%{_bindir}/%{name}
%{_mandir}/man8/*

%changelog
* Thu Dec 27 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.1h-17
- specify missing mode to open(2) as required (P4)
- compile with %%optflags & link with %%ldflags (P3)
- cleanups

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1h-15mdv2011.0
+ Revision: 664918
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1h-14mdv2011.0
+ Revision: 605493
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1h-13mdv2010.1
+ Revision: 522744
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.1h-12mdv2010.0
+ Revision: 425020
- rebuild

* Thu Apr 09 2009 Funda Wang <fwang@mandriva.org> 0.1h-11mdv2009.1
+ Revision: 365301
- rediff syscall patch

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.1h-11mdv2009.0
+ Revision: 221098
- rebuild

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 0.1h-10mdv2008.1
+ Revision: 150229
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Sep 20 2007 Adam Williamson <awilliamson@mandriva.org> 0.1h-9mdv2008.0
+ Revision: 91493
- sync patches with fedora (various useful fixes, including one to fix build)
- rebuild for 2008
- don't package COPYING
- new license policy


* Fri Mar 16 2007 Oden Eriksson <oeriksson@mandriva.com> 0.1h-7mdv2007.1
+ Revision: 145247
- Import gpart

* Fri Mar 16 2007 Oden Eriksson <oeriksson@mandriva.com> 0.1h-7mdv2007.1
- use the %%mrel macro
- bunzip patches

* Wed Feb 02 2005 Lenny Cartier <lenny@mandrakesoft.com> 0.1h-6mdk
- rebuild


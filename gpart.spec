%bcond_without	uclibc

Summary:	Hard disk primary partition table reconstruction
Name:		gpart
Version:	0.1h
Release:	26
License:	GPLv2+
Group:		System/Kernel and hardware
Url:		http://home.pages.de/~michab/gpart/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		gpart-0.1h-mdkconf.patch
Patch1:		gpart-errno.patch
Patch2:		gpart-0.1h-fixes.patch
Patch3:		gpart-0.1h-optflags.patch
Patch4:		gpart-0.1h-open-mode.patch
Patch5:		gpart-0.1h-ntfs-winxp.patch
Patch6:		gpart-0.1h-imagefile.patch
Patch7:		gpart-0.1h-reiserfs.patch
Patch8:		gpart-0.1h-whole-program.patch
# Fedora patches
Patch100:	gpart-0.1h-cflags.patch
Patch101:	gpart-0.1h-errno.patch
Patch102:	gpart-0.1h-largefile.patch
Patch103:	gpart-0.1h-makefile.patch
Patch104:	gpart-0.1h-syscall.patch
Patch105:	gpart-0.1h-varname.patch
%if %{with uclibc}
BuildRequires:	uClibc-devel
%endif

%description
A tool which tries to guess the primary partition table of a PC-type hard disk
in case the primary partition table in sector 0 is damaged, incorrect or
deleted. The guessed table can be written to a file or device. Supported
(guessable) filesystem or partition types: DOS/Windows FAT, Linux ext2 and
swap, OS/2 HPFS, Windows NTFS, FreeBSD and Solaris/x86 disklabels, Minix FS,
QNX 4 FS, Reiser FS, LVM physical volumes, BeOS FS, SGI XFS.

%package -n	uclibc-%{name}
Summary:	Hard disk primary partition table reconstruction (uClibc build)
Group:		System/Kernel and hardware

%description -n	uclibc-%{name}
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
%patch4 -p1 -b .openmode~
%patch5 -p1 -b .ntfs_winxp~
%patch6 -p1 -b .imagefile~
%patch7 -p1 -b .gpart~
%patch8 -p1 -b .wholeprogram~

%if %{with uclibc}
mkdir .uclibc
cp -a * .uclibc
%endif

%build
%if %{with uclibc}
%make -C .uclibc CC="%{uclibc_cc}" OPTFLAGS="%{uclibc_cflags}" LDFLAGS="%{ldflags}" WHOLE_PROGRAM=1
%endif

%make OPTFLAGS="%{optflags}" LDFLAGS="%{ldflags}" WHOLE_PROGRAM=1

%install
%if %{with uclibc}
install -m755 .uclibc/src/%{name} -D %{buildroot}%{uclibc_root}%{_bindir}/%{name}
%endif

install -m755 src/%{name} -D %{buildroot}%{_bindir}/%{name}
install -m644 man/%{name}.8 -D %{buildroot}%{_mandir}/man8/%{name}.8

%files
%doc Changes README
%{_bindir}/%{name}
%{_mandir}/man8/*

%if %{with uclibc}
%files -n uclibc-%{name}
%{uclibc_root}%{_bindir}/%{name}
%endif


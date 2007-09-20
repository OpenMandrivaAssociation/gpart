Summary:	Hard disk primary partition table reconstruction
Name:		gpart
Version:	0.1h
Release:	%mkrel 8
License:	GPLv2+
Source0:	%{name}-%{version}.tar.bz2
Group:		System/Kernel and hardware
URL:		http://home.pages.de/~michab/gpart/
Patch0:		gpart-0.1h-mdkconf.patch
Patch1:		gpart-errno.patch
Patch2:		gpart-0.1h-fixes.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot

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
%patch2 -p1 -b .fixes

%build
%make 

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man8

install -m0755 src/%{name} %{buildroot}%{_bindir}/
install -m0755 man/%{name}.8 %{buildroot}%{_mandir}/man8

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_bindir}/%{name}
%{_mandir}/man8/*


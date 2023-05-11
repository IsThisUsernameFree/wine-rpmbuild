%define name wine
%define release 1
%define buildroot %{_tmppath}/%{name}-%{version}-%{release}-root

Name: %{name}
Version: %{version}
Release: %{release}
Summary: Wine is a compatibility layer for running Windows applications
Group: Applications/Emulators
License: LGPLv2+
URL: http://www.winehq.org/

Source0: wine.tar.xz

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libX11-devel
BuildRequires: libXau-devel
BuildRequires: libxcb-devel
BuildRequires: libXcursor-devel
BuildRequires: libXext-devel
BuildRequires: libXi-devel
BuildRequires: libxml2-devel
BuildRequires: libXrandr-devel
BuildRequires: libxslt-devel
BuildRequires: mesa-libGL-devel
BuildRequires: ncurses-devel
BuildRequires: openssl-devel
BuildRequires: perl
BuildRequires: pkgconfig
BuildRequires: pulseaudio-libs-devel
BuildRequires: zlib-devel
BuildRequires: freetype-devel

%description
Wine is a compatibility layer for running Windows applications on Unix.
Wine does not require Microsoft Windows, as it is a completely free
alternative implementation of the Windows API consisting of 100% non-Microsoft
code, however Wine can optionally use native Windows DLLs if they are
available. Wine provides both a development toolkit (Winelib) for porting
Windows sources to Unix and a program loader, allowing many unmodified
Windows binaries to run on x86-based Unixes, including Linux, FreeBSD,
Mac OS X, and Solaris.

%prep
%setup -q

%build
./configure --enable-win64 --prefix=/usr --libdir=/usr/lib64
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%files
%defattr(-,root,root,-)
/usr/bin/*
/usr/lib64/wine
/usr/include/wine/
/usr/share/man
/usr/share/wine
/usr/share/applications

%changelog

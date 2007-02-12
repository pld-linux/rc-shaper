Summary:	Shaper super-script
Summary(pl.UTF-8):   Shaper super-script - skrypt do konfiguracji ograniczania pasma
Name:		rc-shaper
Version:	1.10
Release:	0.1
License:	GPL script with binaries under unknown license
Group:		Networking/Admin
Source0:	http://dl.sourceforge.net/rc-shaper/%{name}-%{version}.tar.gz
# Source0-md5:	840926444558967b8498eb84bf829bd4
Patch0:		%{name}-conf.patch
URL:		http://rc-shaper.sourceforge.net/
Requires:	iproute2
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Shaper Super-Script is a bash script that uses iproute2 and shapecfg
(shaper.o) to limit incoming and outgoing traffic on a Linux router.
It also has an option for supporting more than 100 shapers via a
kernel patch.

%description -l pl.UTF-8
Shaper Super-Script to skrypt basha używający narzędzi iproute2 i
shapecfg (shaper.o) do ograniczania ruchu przychodzącego i
wychodzącego na linuksowym routerze. Ma także możliwość obsługi więcej
niż 100 shaperów poprzez łatę jądra.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},/etc/rc-shaper,/etc/rc.d/init.d}

install shapecfg-libc6	$RPM_BUILD_ROOT%{_sbindir}
install shapecfg-uClib	$RPM_BUILD_ROOT%{_sbindir}

install rc.shape	$RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}
install shape.conf	$RPM_BUILD_ROOT%{_sysconfdir}/%{name}/shape.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%attr(755,root,root) %{_sbindir}/*
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/shape.conf

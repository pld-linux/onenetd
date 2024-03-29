Summary:	onenetd - a single-server inetd
Summary(pl.UTF-8):	onenetd - inetd dla jednego serwera
Name:		onenetd
Version:	1.11
Release:	1
License:	MIT
Group:		Networking/Admin
Source0:	http://offog.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	da1b1365f0df1a84aea67569f154db62
URL:		http://offog.org/code/onenetd.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
onenetd is a single-server inetd, similar to Dan Bernstein's tcpserver
or courier-tcpd from Courier-IMAP. It is small, has been shown to work
happily on Linux and Solaris, and supports limiting the number of
concurrent connections and refusing further connections with a
configurable message (useful for limiting connections to busy FTP
servers, for instance). See the included manual page for all the
options.

%description -l pl.UTF-8
onenetd to inetd dla pojedynczego serwera, podobny do tcpservera Dana
Bernsteina czy courier-tcpd z Courier-IMAP-a. Jest mały i w praktyce
działa na Linuksie i Solarisie, obsługuje ograniczanie liczby
jednoczesnych połączeń i odrzucanie dalszych z konfigurowalnym
komunikatem (przydatne do ograniczania połączeń na przykład do
obciążonych serwerów FTP). Wszystkie opcje można znaleźć w załączonej
stronie manuala.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

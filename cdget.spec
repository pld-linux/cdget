Summary:	Client for mp3 file sharing on the Internet
Summary(pl):	Klient pozwalaj�cy na udost�pnianie plik�w mp3 w Internecie
Name:		cdget
Version:	0.2.3
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://trasdocka.hemmet.chalmers.se/cdget/%{name}-%{version}.tar.bz2
URL:		http://trasdocka.hemmet.chalmers.se/cdget/index.shtml
BuildRequires:	id3lib
BuildRequires:	qt-devel >= 3.1
Requires:	dctc
Requires:	id3lib
Requires:	qt >= 3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CdGet is not just another client for mp3 file sharing on the Internet.
CdGet is meant to do the work for you. In traditional file
sharing/downloading clients you often end up having to watch and
attend to the download in many steps. This process is usually
mechanical, repetitive and boring, a perfect candidate for
automatization! CdGet is meant to do exactly this, and eliminate the
need for manual control over the download process.

%description -l pl
CdGet nie jest kolejnym klientem s�u��cym do wymiany plik�w mp3
poprzez Internet. CdGet zosta� stworzony by zrobi� wszystko za ciebie.
W tradycyjnym kliencie udost�pniania/�ci�gania plik�w cz�sto zachodzi
potrzeba obserwowania i ingerowania w proces �ci�gania. Proces ten
jest zazwyczaj mechaniczny, powtarzaj�cy si� i nudny, idealny do
zautomatyzowania. CdGet ma robi� w�a�nie to, wyeliminowa� potrzeb�
r�cznej kontroli nad procesem �ci�gania.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/*

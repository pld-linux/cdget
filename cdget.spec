Summary:	Client for MP3 file sharing on the Internet
Summary(pl):	Klient pozwalaj±cy na udostêpnianie plików MP3 w Internecie
Name:		cdget
Version:	0.2.3
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.dtek.chalmers.se/~d00freed/cdget/download/%{name}-%{version}.tar.bz2
# Source0-md5:	47a325319d41e819507079598373fe41
Patch0:		%{name}-am18.patch
URL:		http://www.dtek.chalmers.se/~d00freed/cdget/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	id3lib
BuildRequires:	qt-devel >= 3.1.1
Requires:	dctc >= 0.84.1
Requires:	id3lib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CdGet is not just another client for MP3 file sharing on the Internet.
CdGet is meant to do the work for you. In traditional file
sharing/downloading clients you often end up having to watch and
attend to the download in many steps. This process is usually
mechanical, repetitive and boring, a perfect candidate for
automatization! CdGet is meant to do exactly this, and eliminate the
need for manual control over the download process.

%description -l pl
CdGet nie jest kolejnym klientem s³u¿±cym do wymiany plików MP3
poprzez Internet. CdGet zosta³ stworzony by zrobiæ wszystko za ciebie.
W tradycyjnym kliencie udostêpniania/¶ci±gania plików czêsto zachodzi
potrzeba obserwowania i ingerowania w proces ¶ci±gania. Proces ten
jest zazwyczaj mechaniczny, powtarzaj±cy siê i nudny, idealny do
zautomatyzowania. CdGet ma robiæ w³a¶nie to, wyeliminowaæ potrzebê
rêcznej kontroli nad procesem ¶ci±gania.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
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
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/*

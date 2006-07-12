#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	POE
%define		pnam	Component-Jabber
Summary:	POE::Component::Jabber - POE component for accessing Jabber servers
Summary(pl):	POE::Component::Jabber - komponent POE do dost�pu do serwer�w Jabbera
Name:		perl-POE-Component-Jabber
Version:	1.21
Release:	1.1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	75196e23db297a2b07b1d58a866b03d7
Patch0:		%{name}-const.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-Module-Build
%if %{with tests}
BuildRequires:	perl-Digest-SHA1 >= 1.03
BuildRequires:	perl-Jabber-Connection >= 0.02
BuildRequires:	perl-POE
BuildRequires:	perl-POE-Filter-XML >= 0.02
BuildRequires:	perl-XML-Parser >= 2.29
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
POE::Component::Jabber is heavily based on POE::Component::IRC and
uses much the same event model. Authentication routines are inspired
by Jabber::Connection.

POE::Filter::Jabber is provided which requires XML::Parser and
sends and receives data as Jabber::NodeFactory::Node objects.

POE::Component::Jabber::Auth implements authentication with the
Jabber server. This would be a good module to look at as it
does it in much the way an application would interface with
POE::Component::Jabber by registering for the IQ event.

%description -l pl
POE::Component::Jabber jest w du�ej cz�ci oparty na
POE::Component::IRC i u�ywa w wi�kszo�ci tego samego modelu. Funkcje
uwierzytelniania s� inspirowane Jabber::Connection.

Do��czony jest POE::Filter::Jabber, wymagaj�cy XML::Parser, kt�ry
wysy�a i odbiera dane jako obiekty Jabber::NodeFactory::Node.

POE::Component::Jabber::Auth zawiera implementacj� uwierzytelniania
wzgl�dem serwera Jabbera. To jest dobry modu� do ogl�dania, jako �e
robi to podobnie jak aplikacja, kt�ra wsp�pracowa�aby z
POE::Component::Jabber poprzez rejestracj� dla zdarzenia IQ.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

# rpmowy system wykrywani zaleznosci nie radzi sobie
# rpm dep lookup system dont work properly when
# package Foo::Bar; is declared in some files
# but other use it via use const .. then use FB::something
# there are 2 solutions, first one, 
# disable autodeps for this package, and add manually
# another way, patch perl modules to avoid use const
# i prefer second way

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	destdir=$RPM_BUILD_ROOT

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT 
install -d $RPM_BUILD_ROOT%{_examplesdir}
cp -r examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*/*.pm
%{perl_vendorlib}/%{pdir}/Component/Jabber
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*

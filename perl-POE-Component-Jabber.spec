#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	POE
%define	pnam	Component-Jabber
Summary:	POE::Component::Jabber - POE component for accessing Jabber servers
Summary(pl):	POE::Component::Jabber - komponent POE do dost�pu do serwer�w Jabbera
Name:		perl-POE-Component-Jabber
Version:	1.0
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4e0a60020511c19403b53d6fc993a3dd
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
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
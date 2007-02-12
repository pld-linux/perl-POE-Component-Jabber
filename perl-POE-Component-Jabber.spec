#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	POE
%define		pnam	Component-Jabber
Summary:	POE::Component::Jabber - POE component for accessing Jabber servers
Summary(pl.UTF-8):   POE::Component::Jabber - komponent POE do dostępu do serwerów Jabbera
Name:		perl-POE-Component-Jabber
Version:	1.21
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	75196e23db297a2b07b1d58a866b03d7
Patch0:		%{name}-const.patch
Patch1:		%{name}-examples.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-Module-Build
%if %{with tests}
BuildRequires:	perl-Digest-SHA1 >= 2.11
BuildRequires:	perl-Jabber-Connection >= 0.02
BuildRequires:	perl-POE >= 1:0.3401
BuildRequires:	perl-POE-Filter-XML >= 0.29
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

%description -l pl.UTF-8
POE::Component::Jabber jest w dużej części oparty na
POE::Component::IRC i używa w większości tego samego modelu. Funkcje
uwierzytelniania są inspirowane Jabber::Connection.

Dołączony jest POE::Filter::Jabber, wymagający XML::Parser, który
wysyła i odbiera dane jako obiekty Jabber::NodeFactory::Node.

POE::Component::Jabber::Auth zawiera implementację uwierzytelniania
względem serwera Jabbera. To jest dobry moduł do oglądania, jako że
robi to podobnie jak aplikacja, która współpracowałaby z
POE::Component::Jabber poprzez rejestrację dla zdarzenia IQ.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
# rpm problems fixed by following patch
%patch0 -p1
# this one allows to run examples on current poe (no POE::Preprocessor)
%patch1 -p1

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

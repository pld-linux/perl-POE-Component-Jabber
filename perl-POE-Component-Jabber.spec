#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	POE
%define	pnam	Component-Jabber
Summary:	POE::Component::Jabber - POE component for accessing Jabber servers
#Summary(pl):	
Name:		perl-POE-Component-Jabber
Version:	0.2
Release:	1
License:	?
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4da1e6b4f7c02c1267d9613c10289a40
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{!?_without_tests:1}0
BuildRequires:	perl(Jabber::Connection) >= 0.02
BuildRequires:	perl-Digest-SHA1 >= 1.03
BuildRequires:	perl-POE
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
jabber server. This would be a good module to look at as it
does it in much the way an application would interface with
POE::Component::Jabber by registering for the IQ event.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

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
%doc ChangeLog
%{perl_vendorlib}/%{pdir}/*/*.pm
%{perl_vendorlib}/%{pdir}/Component/Jabber
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*

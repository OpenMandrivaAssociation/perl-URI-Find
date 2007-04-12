%define realname URI-Find
%define name perl-%{realname}
%define version 0.16
%define release %mkrel 2

Summary:	Find URIs in arbitrary text
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}/
Source:		/%{realname}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:  perl(URI)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-root

%description
This module does one thing: Finds URIs and URLs in plain text.
It finds them quickly and it finds them all (or what URI::URL
considers a URI to be.) It only finds URIs which include a scheme
(http:// or the like), for something a bit less strict have
a look at URI::Find::Schemeless.

%prep
%setup -q -n %{realname}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/URI/*
%{_mandir}/*/*

%clean
rm -rf $RPM_BUILD_ROOT


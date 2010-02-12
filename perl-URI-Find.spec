%define upstream_name    URI-Find
%define upstream_version 20100211

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	Find URIs in arbitrary text
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source:     http://search.cpan.org/CPAN/authors/id/M/MS/MSCHWERN/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl(URI)
BuildRequires:  perl(Test::More) > 0.82
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module does one thing: Finds URIs and URLs in plain text.
It finds them quickly and it finds them all (or what URI::URL
considers a URI to be.) It only finds URIs which include a scheme
(http:// or the like), for something a bit less strict have
a look at URI::Find::Schemeless.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Build.PL installdirs=vendor destdir=%{buildroot}
./Build

%check
./Build test

%install
rm -rf $RPM_BUILD_ROOT
./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/URI/*
%{_mandir}/*/*


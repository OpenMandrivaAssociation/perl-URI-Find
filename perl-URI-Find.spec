%define upstream_name    URI-Find
%define upstream_version 20100505

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Find URIs in arbitrary text
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source:		http://search.cpan.org/CPAN/authors/id/M/MS/MSCHWERN/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(URI)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Test::More) > 0.82
BuildArch:	noarch

%description
This module does one thing: Finds URIs and URLs in plain text.
It finds them quickly and it finds them all (or what URI::URL
considers a URI to be.) It only finds URIs which include a scheme
(http:// or the like), for something a bit less strict have
a look at URI::Find::Schemeless.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL installdirs=vendor destdir=%{buildroot}
./Build

%check
./Build test

%install
./Build install

%files
%doc Changes
%{perl_vendorlib}/URI/*
%{_bindir}/urifind
%{_mandir}/*/*

%changelog
* Mon Jul 12 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 20100505.0.0-1mdv2011.0
+ Revision: 551202
- update to 20100505

* Fri Feb 12 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 20100211.0.0-1mdv2010.1
+ Revision: 504493
- update to 20100211

* Sun Jul 12 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 20090319.0.0-1mdv2010.0
+ Revision: 395186
- adding missing buildrequires:
- update to 20090319
- using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.16-5mdv2009.0
+ Revision: 242140
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 0.16-3mdv2008.0
+ Revision: 23624
- rebuild


* Wed Apr 19 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.16-2mdk
- Add BuildRequires

* Sat Apr 08 2006 Arnaud de Lorbeau <devel@mandriva.com> 0.16-1mdk
- Initial MDV RPM


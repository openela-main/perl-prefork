Name: 		perl-prefork
Version: 	1.04
Release: 	26%{?dist}
Summary: 	Optimized module loading for forking or non-forking processes
License: 	GPL+ or Artistic
Group: 		Development/Libraries
URL: 		http://search.cpan.org/dist/prefork/
Source0: 	http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/prefork-%{version}.tar.gz

Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildArch: noarch

BuildRequires: coreutils
BuildRequires: %{__perl}
BuildRequires: %{__make}
BuildRequires: perl-generators
BuildRequires: perl(inc::Module::Install::DSL) >= 0.91
# Run-time:
BuildRequires: perl(Carp)
BuildRequires: perl(Config)
BuildRequires: perl(List::Util) >= 0.18
BuildRequires: perl(Scalar::Util) >= 1.18
BuildRequires: perl(strict)  
BuildRequires: perl(vars)  
# Tests:
BuildRequires: perl(File::Spec) >= 0.80
BuildRequires: perl(overload)
BuildRequires: perl(Test::More) >= 0.47


%description
Optimized module loading for forking or non-forking processes

prefork.pm is intended to serve as a central and optional marshalling
point for state detection (are we running in compile-time or run-time
mode) and to act as a relatively light-weight module loader.

%prep
%setup -q -n prefork-%{version}
rm -r inc/

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%{__make} %{?_smp_mflags}

%install
%{__make} pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
unset AUTOMATED_TESTING RELEASE_TESTING
%{__make} test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/prefork*
%{_mandir}/man3/*

%changelog
* Wed Jul 04 2018 Petr Pisar <ppisar@redhat.com> - 1.04-26
- Disable extra tests and specify all dependencies

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.04-23
- Perl 5.26 rebuild

* Thu May 18 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.04-22
- Eliminate inc. BR: perl(inc::Module::Install) (RHBZ#1452129).
- Modernize spec.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.04-20
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.04-18
- Remove %%defattr.
- Add %%license.
- Modernize spec.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.04-16
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.04-15
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 31 2013 Petr Pisar <ppisar@redhat.com> - 1.04-12
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 22 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.04-10
- Remove RHEL spec file compatibility.
- Fix FTBFS (BZ 878829).

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Petr Pisar <ppisar@redhat.com> - 1.04-8
- Perl 5.16 rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.04-6
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.04-4
- 661697 rebuild for fixing problems with vendorach/lib

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.04-3
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.04-2
- rebuild against perl 5.10.1

* Wed Jul 29 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.04-1
- Upstream update.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 18 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.03-1
- Upstream update.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Mar  4 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.02-2
- rebuild for new perl

* Sun Nov 25 2007 Ralf Corsépius <rc040203@freenet.de> - 1.02-1
- Upstream update.
- Add BR: perl(Test::MinimumVersion).

* Fri Aug 17 2007 Ralf Corsépius <rc040203@freenet.de> - 1.01-3
- Update license tag.

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 1.01-2
- Mass rebuild.

* Mon Aug 07 2006 Ralf Corsépius <rc040203@freenet.de> - 1.01-1
- Upstream update.

* Wed Mar 01 2006 Ralf Corsépius <rc040203@freenet.de> - 1.00-3
- Rebuild for perl-5.8.8.

* Tue Sep 13 2005 Ralf Corsepius <rc040203@freenet.de> - 1.00-2
- Spec file cleanup.

* Sat Sep 10 2005 Ralf Corsepius <rc040203@freenet.de> - 1.00-1
- FE submission.

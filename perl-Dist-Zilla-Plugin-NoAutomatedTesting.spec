%define upstream_name    Dist-Zilla-Plugin-NoAutomatedTesting
%define upstream_version 0.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Avoid running under CPAN Testers
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Dist::Zilla)
BuildArch:	noarch

%description
CPAN Testers are great and do a worthy and thankless job, testing all the
distributions uploaded to CPAN. But sometimes we don't want a distribution
to be tested by these gallant individuals.

Dist::Zilla::Plugin::NoAutomatedTesting is a the Dist::Zilla manpage plugin
that mungles 'Makefile.PL' to detect that it is being run by a CPAN Tester
and 'exit 0' if it is.

As this plugin mungles the 'Makefile.PL' it is imperative that it is
specified in 'dist.ini' AFTER '[MakeMaker]'.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.yml LICENSE README META.json Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*



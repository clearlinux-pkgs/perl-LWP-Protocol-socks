#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-LWP-Protocol-socks
Version  : 1.7
Release  : 17
URL      : https://cpan.metacpan.org/authors/id/S/SC/SCR/LWP-Protocol-socks-1.7.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SC/SCR/LWP-Protocol-socks-1.7.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libl/liblwp-protocol-socks-perl/liblwp-protocol-socks-perl_1.7-1.debian.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-LWP-Protocol-socks-license = %{version}-%{release}
Requires: perl-LWP-Protocol-socks-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(HTTP::Status)
BuildRequires : perl(IO::Socket::SSL)
BuildRequires : perl(IO::Socket::Socks)
BuildRequires : perl(LWP)
BuildRequires : perl(LWP::Protocol::https)
BuildRequires : perl(Net::HTTP)
BuildRequires : perl(Net::SSLeay)
BuildRequires : perl(Try::Tiny)
BuildRequires : perl(URI)

%description
LWP-Protocol-socks
===============================
FYI, files are checked into git@github.com:scr/cpan.git

%package dev
Summary: dev components for the perl-LWP-Protocol-socks package.
Group: Development
Provides: perl-LWP-Protocol-socks-devel = %{version}-%{release}
Requires: perl-LWP-Protocol-socks = %{version}-%{release}

%description dev
dev components for the perl-LWP-Protocol-socks package.


%package license
Summary: license components for the perl-LWP-Protocol-socks package.
Group: Default

%description license
license components for the perl-LWP-Protocol-socks package.


%package perl
Summary: perl components for the perl-LWP-Protocol-socks package.
Group: Default
Requires: perl-LWP-Protocol-socks = %{version}-%{release}

%description perl
perl components for the perl-LWP-Protocol-socks package.


%prep
%setup -q -n LWP-Protocol-socks-1.7
cd %{_builddir}
tar xf %{_sourcedir}/liblwp-protocol-socks-perl_1.7-1.debian.tar.xz
cd %{_builddir}/LWP-Protocol-socks-1.7
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/LWP-Protocol-socks-1.7/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-LWP-Protocol-socks
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-LWP-Protocol-socks/ac1acdbbe5dec9a636be62a2461d194f34d2cbab
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/LWP::Protocol::socks.3
/usr/share/man/man3/LWP::Protocol::socks4.3
/usr/share/man/man3/URI::socks.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-LWP-Protocol-socks/ac1acdbbe5dec9a636be62a2461d194f34d2cbab

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.32.1/LWP/Protocol/socks.pm
/usr/lib/perl5/vendor_perl/5.32.1/LWP/Protocol/socks4.pm
/usr/lib/perl5/vendor_perl/5.32.1/URI/socks.pm
/usr/lib/perl5/vendor_perl/5.32.1/URI/socks4.pm

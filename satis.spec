
%define		rel		0.4
%define		githash	48191ff
# $ git rev-list 1.0.0-alpha1..%{githash} --count
%define		commits	152
%define		subver	alpha1
%define		php_min_version 5.3.4
%include	/usr/lib/rpm/macros.php
Summary:	Package Repository Generator
Name:		satis
Version:	1.0.0
Release:	1.%{subver}%{?commits:.%{commits}}%{?githash:.g%{githash}}.%{rel}
License:	MIT
Group:		Development/Languages/PHP
#Source0:	https://github.com/composer/satis/archive/%{version}-%{subver}/%{name}-%{version}%{subver}.tar.gz
Source0:	https://github.com/composer/satis/archive/%{githash}/%{name}-%{version}-%{subver}-%{commits}-g%{githash}.tar.gz
# Source0-md5:	adee07882bc8c526b6bd3489812bc194
Patch0:		versionparser.patch
URL:		https://github.com/composer/satis
BuildRequires:	composer
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.461
BuildRequires:	sed >= 4.0
Requires:	php(core) >= %{php_min_version}
Requires:	php(ctype)
Requires:	php(filter)
Requires:	php(hash)
Requires:	php(json)
Requires:	php(phar)
Requires:	php(spl)
Suggests:	php(openssl)
Suggests:	php(zip)
Suggests:	php(zlib)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_datadir}/%{name}

%description
Simple static Composer repository generator.

It uses any composer.json file as input and dumps all the required
(according to their version constraints) packages to a Composer
Repository file.

%prep
%setup -qc -n %{name}-%{version}-%{release}
mv %{name}-*/* .

%{__sed} -i -e '1s,^#!.*env php,#!/usr/bin/php,' bin/*
%{__rm} composer.lock

%build
composer install --prefer-dist --no-dev -v

%patch0 -p7 -d vendor/composer/semver/src

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_appdir}}
cp -a bin src vendor views $RPM_BUILD_ROOT%{_appdir}
ln -s %{_appdir}/bin/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%{__rm} -r $RPM_BUILD_ROOT%{_appdir}/vendor/twig/twig/test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%attr(755,root,root) %{_bindir}/satis
%dir %{_appdir}
%dir %{_appdir}/bin
%attr(755,root,root) %{_appdir}/bin/*
%{_appdir}/src
%{_appdir}/vendor
%{_appdir}/views

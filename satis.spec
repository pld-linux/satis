
%define		php_min_version 5.4.0
%include	/usr/lib/rpm/macros.php
Summary:	Package Repository Generator
Name:		satis
Version:	1.0.0
Release:	2
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/composer/satis/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	884bf6850503c0cf5eff693b841b3f1b
Source1:	autoload.php
Patch0:		autoload.patch
URL:		https://github.com/composer/satis
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.461
BuildRequires:	sed >= 4.0
Requires:	composer >= 1.0.0-18
Requires:	php(core) >= %{php_min_version}
Requires:	php(hash)
Requires:	php(json)
Requires:	php(pcre)
Requires:	php-composer-semver >= 1.2.0-2
Requires:	php-twig-Twig >= 1.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_datadir}/%{name}

%description
Simple static Composer repository generator.

It uses any composer.json file as input and dumps all the required
(according to their version constraints) packages to a Composer
Repository file.

%prep
%setup -q
%patch0 -p1

%{__sed} -i -e '1s,^#!.*env php,#!/usr/bin/php,' bin/*

cp -p %{SOURCE1} src/autoload.php

# move to Source dir, eases packaging
mv res views src

# not needed runtime
mv bin/docker* bin/*.bat .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{php_data_dir}/Composer/Satis}
cp -a src/* $RPM_BUILD_ROOT%{php_data_dir}/Composer/Satis
install -p bin/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%attr(755,root,root) %{_bindir}/satis
%{php_data_dir}/Composer/Satis

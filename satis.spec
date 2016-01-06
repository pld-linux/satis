
%define		rel		0.12
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
Source1:	autoload.php
Patch0:		autoload.patch
URL:		https://github.com/composer/satis
BuildRequires:	composer
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.461
BuildRequires:	sed >= 4.0
Requires:	composer >= 1.0.0-16.alpha11
Requires:	php(core) >= %{php_min_version}
Requires:	php(hash)
Requires:	php(json)
Requires:	php(pcre)
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
%setup -qc -n %{name}-%{version}-%{release}
mv %{name}-*/* .
%patch0 -p1

%{__sed} -i -e '1s,^#!.*env php,#!/usr/bin/php,' bin/*

cp -p %{SOURCE1} src/Composer/Satis/autoload.php

# move to Source dir, eases packaging
mv res views src/Composer/Satis

# not needed runtime
mv bin/compile .
mv src/Composer/Satis/Compiler.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{php_data_dir}/Composer}
cp -a src/Composer $RPM_BUILD_ROOT%{php_data_dir}
install -p bin/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%attr(755,root,root) %{_bindir}/satis
%{php_data_dir}/Composer/Satis

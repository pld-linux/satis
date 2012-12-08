%define		php_min_version 5.3.4
%include	/usr/lib/rpm/macros.php
Summary:	Package Repository Generator
Name:		satis
Version:	1.0.0
Release:	0.1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/composer/satis/archive/master.tar.gz
# Source0-md5:	a149bce7151e35dc23acc53522eefea5
URL:		https://github.com/composer/satis
BuildRequires:	composer-php
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php(core) >= %{php_min_version}
Requires:	php(phar)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple static Composer repository generator.

It uses any composer.json file as input and dumps all the required
(according to their version constraints) packages to a Composer
Repository file.

%prep
%setup -qc
mv %{name}-*/* .

%build
composer install -v

%{__php} -d phar.readonly=0 -d memory_limit=512M ./bin/compile

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
cp -p %{name}.phar $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%attr(755,root,root) %{_bindir}/satis

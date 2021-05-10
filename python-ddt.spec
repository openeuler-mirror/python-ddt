%global _empty_manifest_terminate_build 0
Name:		python-ddt
Version:	1.1.3
Release:	1
Summary:	Data-Driven/Decorated Tests
License:	MIT License
URL:		https://github.com/txels/ddt
Source0:	https://files.pythonhosted.org/packages/50/4e/5a85c13e77af8246b86fb1f341d79ba32d03d8fd5353efa4fa1caa5b7886/ddt-1.1.3.tar.gz
BuildArch:	noarch
%description
A library to multiply test cases

%package -n python2-ddt
Summary:	Data-Driven/Decorated Tests
Provides:	python-ddt
BuildRequires:	python2-devel
BuildRequires:	python2-setuptools
%description -n python2-ddt
A library to multiply test cases

%package help
Summary:	Development documents and examples for ddt
Provides:	python2-ddt-doc
%description help
A library to multiply test cases

%prep
%autosetup -n ddt-1.1.3

%build
%py2_build

%install
%py2_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
	find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
	find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
	find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
	find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
	find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%files -n python2-ddt -f filelist.lst
%{python2_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Mon May 10 2021 openstack-sig <openstack@openeuler.org>
- Package Spec generated

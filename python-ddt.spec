%global _empty_manifest_terminate_build 0
Name:		python-ddt
Version:	1.4.1
Release:	1
Summary:	Data-Driven/Decorated Tests
License:	MIT License
URL:		https://github.com/datadriventests/ddt
Source0:	https://files.pythonhosted.org/packages/1b/e3/499cfd630d217a4fa536f03465f879fb68492e2672851214c6eb024f1716/ddt-1.4.1.tar.gz
BuildArch:	noarch

Requires:	python3-enum34

%description
A library to multiply test cases




%package -n python3-ddt
Summary:	Data-Driven/Decorated Tests
Provides:	python-ddt
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
%description -n python3-ddt
A library to multiply test cases




%package help
Summary:	Development documents and examples for ddt
Provides:	python3-ddt-doc
%description help
A library to multiply test cases




%prep
%autosetup -n ddt-1.4.1

%build
%py3_build

%install
%py3_install
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

%files -n python3-ddt -f filelist.lst
%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Thu Nov 19 2020 Python_Bot <Python_Bot@openeuler.org>
- Package Spec generated

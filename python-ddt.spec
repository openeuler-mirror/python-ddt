%global _empty_manifest_terminate_build 0
Name:           python-ddt
Version:        1.6.0
Release:        1
Summary:        Data-Driven/Decorated Tests
License:        MIT
URL:            https://github.com/datadriventests/ddt
Source0:        https://files.pythonhosted.org/packages/c2/b2/20cfe16303e0bef0b2fb54024118ff97fa752414763ab626486794dab072/ddt-1.6.0.tar.gz
BuildArch:      noarch
%description
A library to multiply test cases

%package -n python3-ddt
Summary:        Data-Driven/Decorated Tests
Provides:       python-ddt
# Base build requires
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
BuildRequires:  python3-pytest
BuildRequires:  python3-six
BuildRequires:  python3-PyYAML
# General requires
BuildRequires:  python3-enum34
# General requires
Requires:       python3-enum34
%description -n python3-ddt
A library to multiply test cases

%package help
Summary:        Data-Driven/Decorated Tests
Provides:       python3-ddt-doc
%description help
A library to multiply test cases

%prep
%autosetup -n ddt-%{version}

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

%check
%{__python3} setup.py test

%files -n python3-ddt -f filelist.lst
%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Wed Aug 31 2022 hkgy <kaguyahatu@outlook.com> - 1.6.0-1
- Update to 1.6.0

* Thu May 19 2022 renliang16 <renliang@uniontech.com> - 1.4.4-1
- Upgrade package python3-ddt to version 1.4.4

* Thu Nov 19 2020 Python_Bot <Python_Bot@openeuler.org>
- Package Spec generated

%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name requirements-parser

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        0.2.0
Release:        2%{?dist}
Summary:        Parses Pip requirement files

License:        BSD
URL:            https://github.com/davidfischer/requirements-parser
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_install
%{?scl:EOF}


%files -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%license LICENSE.rst
%doc README.rst
%{python3_sitelib}/requirements
%{python3_sitelib}/requirements_parser-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Sep 06 2021 Evgeni Golov - 0.2.0-2
- Build against Python 3.8

* Thu Nov 05 2020 Evgeni Golov - 0.2.0-1
- Initial package.

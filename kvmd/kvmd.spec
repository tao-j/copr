%global srcname kvmd

Name:           python-%{srcname}
Version:        3.156
Release:        1%{?dist}
Summary:        The main PiKVM daemon

License:        GPL
URL:            https://github.com/pikvm/kvmd
Source0:        https://github.com/pikvm/kvmd/archive/refs/tags/v3.156.tar.gz

BuildArch:      noarch

%description
"The main PiKVM daemon. With a nginx server conf."


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        The main PiKVM daemon
BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description -n python%{python3_pkgversion}-%{srcname}
"The main PiKVM daemon. With a nginx server conf."


%generate_buildrequires
%pyproject_buildrequires -r

%prep
%autosetup -p1 -n kvmd-3.156

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files kvmd


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md
/usr/bin/kvmd*

%changelog
* Sat Oct 22 2022 Tao Jin <tao-j@outlook.com> - 3.156-1
- Initial RPM spec

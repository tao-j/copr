Name: kvmd
Version: 3.50
Release: 1%{?dist}
Summary: The main Pi-KVM daemon
License: GPLv3+
URL: https://github.com/pikvm/kvmd
Source: https://github.com/pikvm/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0: kvmd-otgnet-fix-paths.patch
BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: python3-rpm
BuildRequires: systemd-rpm-macros
BuildRequires: python3dist(pyyaml)
BuildRequires: python3dist(aiohttp) >= 3.7.4
BuildRequires: python3dist(aiofiles)
BuildRequires: python3dist(passlib)
BuildRequires: python3dist(python-periphery)
BuildRequires: python3dist(pyserial)
BuildRequires: python3dist(setproctitle)
BuildRequires: python3dist(spidev)
BuildRequires: python3dist(psutil)
BuildRequires: python3dist(netifaces)
BuildRequires: python3dist(systemd-python)
BuildRequires: python3dist(dbus-python)
BuildRequires: python3dist(pygments)
BuildRequires: python3dist(pyghmi)
BuildRequires: python3dist(python-pam)
BuildRequires: python3dist(pillow) >= 8.3.1
BuildRequires: python3dist(python-xlib)
BuildRequires: python3dist(hidapi)
BuildRequires: python3-libgpiod
Requires: python3-%{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: group(gpio)
Requires: gpio-udev-rules
Requires(pre): %{_bindir}/getent
Requires(pre): %{_sbindir}/useradd

%description
The main Pi-KVM daemon.


%package -n python3-%{name}
Summary: The main Pi-KVM daemon
BuildArch: noarch
Requires: python3dist(pyyaml)
Requires: python3dist(aiohttp) >= 3.7.4
Requires: python3dist(aiofiles)
Requires: python3dist(passlib)
Requires: python3dist(python-periphery)
Requires: python3dist(pyserial)
Requires: python3dist(setproctitle)
Requires: python3dist(spidev)
Requires: python3dist(psutil)
Requires: python3dist(netifaces)
Requires: python3dist(systemd-python)
Requires: python3dist(dbus-python)
Requires: python3dist(pygments)
Requires: python3dist(pyghmi)
Requires: python3dist(python-pam)
Requires: python3dist(pillow) >= 8.3.1
Requires: python3dist(python-xlib)
Requires: python3dist(hidapi)
Requires: python3-libgpiod
Requires: v4l-utils
Requires: ustreamer >= 4.4
Requires: iptables
Requires: iproute
Requires: dnsmasq
Requires: ipmitool
Requires: dhclient
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n python3-%{name}
The main Pi-KVM daemon.


%package web
Summary: Web assets for Pi-KVM
BuildArch: noarch
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description web
Web assets for Pi-KVM.


%package defconfig
Summary: Default configuration files for Pi-KVM
BuildArch: noarch
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description defconfig
Default configuration files for Pi-KVM.


%package nginx
Summary: Nginx configuration for Pi-KVM
BuildArch: noarch
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{name}-web = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: nginx

%description nginx
Nginx configuration for Pi-KVM.


%prep
%setup -q
%patch0 -p1

%build
CFLAGS="%{optflags}" %{__python3} setup.py build

%install
%{__python3} setup.py install -O1 --prefix=%{_prefix} --root %{buildroot}
%{__install} -Dm644 -t %{buildroot}%{_unitdir} configs/os/services/*.service
%{__rm} -f %{buildroot}%{_unitdir}/kvmd-bootconfig.service
%{__sed} -i 's|/usr/bin/nginx|/usr/sbin/nginx|' %{buildroot}%{_unitdir}/kvmd-nginx.service
%{__install} -DTm644 configs/os/sysusers.conf %{buildroot}%{_sysusersdir}/kvmd.conf
%{__sed} -i \
    -e 's/^m kvmd uucp$/m kvmd dialout/' \
    -e '/^m kvmd dialout$/a m kvmd video' \
    %{buildroot}%{_sysusersdir}/kvmd.conf
%{__install} -DTm644 configs/os/tmpfiles.conf %{buildroot}%{_tmpfilesdir}/kvmd.conf
%{__mkdir_p} %{buildroot}%{_datadir}/kvmd
%{__cp} -r hid web extras contrib/keymaps %{buildroot}%{_datadir}/kvmd
find %{buildroot}%{_datadir}/kvmd/web -name '*.pug' -exec rm -f '{}' \;
%{__mkdir_p} %{buildroot}%{_datadir}/kvmd/configs.default
%{__cp} -r configs/* %{buildroot}%{_datadir}/kvmd/configs.default
find %{buildroot}%{_datadir}/kvmd -name .gitignore -delete
%{__mkdir_p} %{buildroot}/etc/kvmd/nginx/ssl
%{__chmod} 750 %{buildroot}/etc/kvmd/nginx/ssl
%{__install} -Dm444 -t %{buildroot}/etc/kvmd/nginx configs/nginx/*.conf
%{__chmod} 644 %{buildroot}/etc/kvmd/nginx/nginx.conf
%{__sed} -i -e 's/^#PROD//' %{buildroot}/etc/kvmd/nginx/nginx.conf
%{__install} -Dm644 -t %{buildroot}%{_sysconfdir}/kvmd configs/kvmd/*.yaml configs/kvmd/*passwd
%{__mkdir_p} %{buildroot}%{_sharedstatedir}/kvmd/msd

%check
%{__python3} -m unittest discover -v

%pre
%{_bindir}/getent passwd kvmd >/dev/null || \
%{_sbindir}/useradd -r -U -G gpio,dialout,video,systemd-journal \
                    -d %{_datadir}/kvmd -s %{_sbindir}/nologin \
                    -c 'Pi-KVM - The main daemon' kvmd

%{_bindir}/getent passwd kvmd-ipmi >/dev/null || \
%{_sbindir}/useradd -r -U -G kvmd \
                    -d %{_datadir}/kvmd -s %{_sbindir}/nologin \
                    -c 'Pi-KVM - IPMI to KVMD proxy' kvmd-ipmi

%{_bindir}/getent passwd kvmd-vnc >/dev/null || \
%{_sbindir}/useradd -r -U -G kvmd \
                    -d %{_datadir}/kvmd -s %{_sbindir}/nologin \
                    -c 'Pi-KVM - VNC to KVMD/Streamer proxy' kvmd-vnc

%files
%doc README.md
%license LICENSE
%dir %{_sysconfdir}/kvmd
%config %attr(0600,kvmd,kvmd) %{_sysconfdir}/kvmd/htpasswd
%config %attr(0600,kvmd-ipmi,kvmd-ipmi) %{_sysconfdir}/kvmd/ipmipasswd
%config %attr(0600,kvmd-vnc,kvmd-vnc) %{_sysconfdir}/kvmd/vncpasswd
%config %{_sysconfdir}/kvmd/*.yaml
%{_unitdir}/*.service
%exclude %{_unitdir}/kvmd-nginx.service
%{_sysusersdir}/kvmd.conf
%{_tmpfilesdir}/kvmd.conf
%{_datadir}/kvmd
%exclude %{_datadir}/kvmd/web
%exclude %{_datadir}/kvmd/configs.default
%dir %{_sharedstatedir}/kvmd
%attr(-,kvmd,root) %{_sharedstatedir}/kvmd/msd

%files -n python3-%{name}
%doc README.md
%license LICENSE
%{_bindir}/kvmd*
%{python3_sitelib}/*

%files web
%doc README.md
%license LICENSE
%{_datadir}/kvmd/web

%files defconfig
%doc README.md
%license LICENSE
%{_datadir}/kvmd/configs.default

%files nginx
%doc README.md
%license LICENSE
%dir %{_sysconfdir}/kvmd/nginx
%{_sysconfdir}/kvmd/nginx/*.conf
%dir %attr(0750,root,root) %{_sysconfdir}/kvmd/nginx/ssl
%{_unitdir}/kvmd-nginx.service

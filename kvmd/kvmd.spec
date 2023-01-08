Name: kvmd
Version: 3.191
Release: 2%{?dist}
Summary: The main kvmd daemon
License: GPL-3.0-or-later
URL: https://github.com/pikvm/kvmd
Source: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1: fedora.yaml
Source2: kvmd-systemd-override.conf
BuildArch: noarch
BuildRequires: systemd-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-libgpiod
BuildRequires: python3dist(pyyaml)
BuildRequires: python3dist(aiohttp) >= 3.7.4
BuildRequires: python3dist(aiofiles)
BuildRequires: python3dist(passlib)
BuildRequires: python3dist(pyserial)
BuildRequires: python3dist(setproctitle)
BuildRequires: python3dist(spidev)
BuildRequires: python3dist(psutil)
BuildRequires: python3dist(netifaces)
BuildRequires: python3dist(systemd-python)
BuildRequires: python3dist(dbus-python)
BuildRequires: python3dist(dbus-next)
BuildRequires: python3dist(zstandard)
BuildRequires: python3dist(pygments)
BuildRequires: python3dist(pyghmi)
BuildRequires: python3dist(python-pam)
BuildRequires: python3dist(pillow) >= 8.3.1
BuildRequires: python3dist(python-xlib)
BuildRequires: python3dist(hidapi)
#BuildRequires: python3dist(ustreamer)
Requires: python3-%{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: group(gpio)
Requires(pre): %{_bindir}/getent
Requires(pre): %{_sbindir}/useradd
Recommends: janus
Recommends: %{name}-nginx
Recommends: %{name}-config

%description
The kvmd daemon is used to make the server running this service capable of being as an out of band KVM(Keyboard, Video, Mouse) machine over the network. 

%package -n python3-%{name}
Summary: The main kvmd daemon
BuildArch: noarch
Requires: v4l-utils
Requires: ustreamer >= 4.4
Requires: iptables
Requires: iproute
Requires: dnsmasq
Requires: ipmitool
Requires: dhclient
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n python3-%{name}
The main kvmd daemon.

%package config
Summary: Default configuration files for kvmd
BuildArch: noarch
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
%description config
Default yaml configuration files for kvmd.

%package config-fedora
Summary: Default configuration files for kvmd
BuildArch: noarch
%description config-fedora
Default yaml configuration files for kvmd. Fedora generic sever support

%package web
Summary: Web assets for kvmd
BuildArch: noarch
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
%description web
Web assets for kvmd nginx server.

%package nginx
Summary: Nginx configuration for kvmd
BuildArch: noarch
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{name}-web = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: nginx
Requires: tesseract
Requires: tesseract-langpack-eng
%description nginx
Nginx configuration for kvmd.

%prep
%autosetup -p1 
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%{__install} -Dm755 -t %{buildroot}%{_bindir} scripts/kvmd-{bootconfig,gencert,certbot}
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
%{__mkdir_p} %{buildroot}%{_sysconfdir}/kvmd/{vnc,nginx}/ssl
%{__chmod} 750 %{buildroot}%{_sysconfdir}/kvmd/{vnc,nginx}/ssl
%{__install} -Dm444 -t %{buildroot}%{_sysconfdir}/kvmd/nginx configs/nginx/*.conf
%{__chmod} 644 %{buildroot}%{_sysconfdir}/kvmd/nginx/{nginx,redirect-to-https,ssl,listen-http{,s}}.conf
%{__sed} -i -e 's/^#PROD//' %{buildroot}%{_sysconfdir}/kvmd/nginx/nginx.conf
%{__mkdir_p} %{buildroot}%{_sysconfdir}/kvmd/janus
%{__chmod} 750 %{buildroot}%{_sysconfdir}/kvmd/janus
%{__install} -Dm444 -t %{buildroot}%{_sysconfdir}/kvmd/janus configs/janus/*.jcfg
%{__install} -Dm644 -t %{buildroot}%{_sysconfdir}/kvmd configs/kvmd/*.yaml configs/kvmd/web.css
%{__install} -Dm600 -t %{buildroot}%{_sysconfdir}/kvmd configs/kvmd/*passwd
%{__mkdir_p} %{buildroot}%{_sysconfdir}/kvmd/override.d
%{__mkdir_p} %{buildroot}%{_sharedstatedir}/kvmd/{msd,pst}
%{__install} -Dm644 -t %{buildroot}%{_sysconfdir}/kvmd/main.yaml %{SOURCE1}
%{__cp} -r testenv/fakes %{buildroot}%{_datadir}/kvmd
%{__install} -Dm644 -t ${buildroot}{_bindir}/kvmd-fake-vcgencmd testenv/fakes/vcgencmd
%{__mkdir_p} %{buildroot}%{_sysconfdir}/systemd/system/kvmd.service.d
%{__cp} %{SOURCE2} %{buildroot}%{_sysconfdir}/systemd/system/kvmd.service.d

#%check
#%{__python3} -m unittest discover -v

%pre
%{_bindir}/getent passwd kvmd >/dev/null || \
%{_sbindir}/useradd -r -U -G gpio,dialout,video,systemd-journal \
                    -d %{_datadir}/kvmd -s %{_sbindir}/nologin \
                    -c 'kvmd - The main daemon' kvmd

%{_bindir}/getent passwd kvmd-ipmi >/dev/null || \
%{_sbindir}/useradd -r -U -G kvmd \
                    -d %{_datadir}/kvmd -s %{_sbindir}/nologin \
                    -c 'kvmd - IPMI to KVMD proxy' kvmd-ipmi

%{_bindir}/getent passwd kvmd-vnc >/dev/null || \
%{_sbindir}/useradd -r -U -G kvmd \
                    -d %{_datadir}/kvmd -s %{_sbindir}/nologin \
                    -c 'kvmd - VNC to KVMD/Streamer proxy' kvmd-vnc

%post
%{_bindir}/kvmd-gencert --do-the-thing
%{_bindir}/kvmd-gencert --do-the-thing --vnc

%files
%doc README.md
%license LICENSE
%dir %{_sysconfdir}/kvmd
%config %attr(0600,kvmd,kvmd) %{_sysconfdir}/kvmd/htpasswd
%config %attr(0600,kvmd-ipmi,kvmd-ipmi) %{_sysconfdir}/kvmd/ipmipasswd
%config %attr(0600,kvmd-vnc,kvmd-vnc) %{_sysconfdir}/kvmd/vncpasswd
%config %{_sysconfdir}/kvmd/*.yaml
%config %{_sysconfdir}/kvmd/*.css
%config %{_sysconfdir}/kvmd/janus/*.jcfg
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
%{python3_sitelib}/kvmd*

%files web
%doc README.md
%license LICENSE
%{_datadir}/kvmd/web

%files config
%doc README.md
%license LICENSE
%{_datadir}/kvmd/configs.default

%files config-fedora
%doc README.md
%license LICENSE
%{_sysconfdir}/kvmd/main.yaml
%{_sysconfdir}/systemd/system/kvmd.service.d/*

%files nginx
%doc README.md
%license LICENSE
%dir %{_sysconfdir}/kvmd/nginx
%{_sysconfdir}/kvmd/nginx/*.conf
%dir %attr(0750,root,root) %{_sysconfdir}/kvmd/nginx/ssl
%{_unitdir}/kvmd-nginx.service

%changelog
* Sat Jan 07 2023 Tao Jin <tao-j@outlook.com> - 3.191-2
- Add fake script to be used in generic server
- Multiple clean-ups


* Sat Jan 07 2023 Tao Jin <tao-j@outlook.com> - 3.191-1
- Update to 3.191
- Refactor spec file to comply with Fedora guideline and submit for review

* Sun Oct 23 2022 Tao Jin <tao-j@outlook.com> - 3.156-1
- Update to 3.156, add patch to remove unsupported type annotation

* Sun Aug 28 2022 Oleg Girko <ol@infoserver.lv> - 3.50-1
- Update to 3.50

* Sun Jul 11 2021 Oleg Girko <ol@infoserver.lv> - 2.3-2
- Require gpio-udev-rules

* Fri Jul 09 2021 Oleg Girko <ol@infoserver.lv> - 2.3-1
- Update to 2.3
- Require getent and useradd utilities for preinstall script
- Require gpio group

* Wed Oct 21 2020 Oleg Girko <ol@infoserver.lv> - 2.2-2
- Add patch to fix paths of various system utilities

* Tue Oct 20 2020 Oleg Girko <ol@infoserver.lv> - 2.2-1
- Update to 2.2

* Sun Oct 11 2020 Oleg Girko <ol@infoserver.lv> - 2.1-1
- Update to 2.1

* Wed Oct 07 2020 Oleg Girko <ol@infoserver.lv> - 2.0-1
- Update to 2.0

* Wed Sep 23 2020 Oleg Girko <ol@infoserver.lv> - 1.102-2
- Enable unit tests (just to check syntax)
- Fix python3-libgpiod dependency

* Fri Sep 18 2020 Oleg Girko <ol@infoserver.lv> - 1.102-1
- Update to 1.102

* Mon Sep 14 2020 Oleg Girko <ol@infoserver.lv> - 1.100-1
- Update to 1.100

* Tue Sep 01 2020 Oleg Girko <ol@infoserver.lv> - 1.98-1
- Update to 1.98

* Mon Aug 31 2020 Oleg Girko <ol@infoserver.lv> - 1.97-1
- Update to 1.97

* Tue Aug 25 2020 Oleg Girko <ol@infoserver.lv> - 1.95-1
- Update to 1.95
- Make kvmd-nginx subpackage require nginx

* Fri Aug 21 2020 Oleg Girko <ol@infoserver.lv> - 1.92-2
- Split more correctly into more subpackages

* Thu Aug 20 2020 Oleg Girko <ol@infoserver.lv> - 1.92-1
- Update to 1.91
- Add subpackage with Nginx configs
- Fix Nginx binary path in service file
- Fix groups of kvmd user

* Wed Aug 19 2020 Oleg Girko <ol@infoserver.lv> - 1.91-1
- Update to 1.91
- Fix patch to remove all uses of assignment expressions

* Tue Aug 18 2020 Oleg Girko <ol@infoserver.lv> - 1.90-2
- Fix runtime dependency
- Drop unneeded build dependencies

* Mon Aug 17 2020 Oleg Girko <ol@infoserver.lv> - 1.90-1
- Initial import
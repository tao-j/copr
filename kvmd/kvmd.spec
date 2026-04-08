Name:           kvmd
Version:        4.163
Release:        3%{?dist}
Summary:        The main PiKVM daemon
License: GPL-3.0-or-later
URL:            https://github.com/pikvm/kvmd
Source0:        %{url}/archive/v%{version}.tar.gz
Source1:        generic.yaml

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-rpm
BuildRequires:  systemd-rpm-macros
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(aiofiles)
BuildRequires:  python3dist(async-lru)
BuildRequires:  python3dist(passlib)
BuildRequires:  python3dist(pyotp)
BuildRequires:  python3dist(qrcode)
BuildRequires:  python3dist(pyserial)
BuildRequires:  python3dist(pyserial-asyncio)
BuildRequires:  python3dist(setproctitle)
BuildRequires:  python3dist(spidev)
BuildRequires:  python3dist(psutil)
BuildRequires:  python3dist(netifaces)
BuildRequires:  python3dist(systemd-python)
BuildRequires:  python3dist(dbus-python)
BuildRequires:  python3dist(dbus-next)
BuildRequires:  python3dist(pygments)
BuildRequires:  python3dist(pyghmi)
BuildRequires:  python3dist(python-pam)
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(python-xlib)
BuildRequires:  python3dist(xkbcommon)
BuildRequires:  python3dist(hidapi)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(pyrad)
BuildRequires:  python3dist(python-ldap)
BuildRequires:  python3dist(zstandard)
BuildRequires:  python3dist(mako)
BuildRequires:  python3dist(pyusb)
BuildRequires:  python3dist(pyudev)
BuildRequires:  python3dist(gpiod) >= 2
BuildRequires:  python3dist(ustreamer)
Requires:       group(gpio)
%{?sysusers_requires_compat}
Requires(pre):  %{_bindir}/getent
Requires(pre):  %{_sbindir}/useradd
Requires:       python3dist(pyyaml)
Requires:       python3dist(aiohttp)
Requires:       python3dist(aiofiles)
Requires:       python3dist(async-lru)
Requires:       python3dist(passlib)
Requires:       python3dist(pyotp)
Requires:       python3dist(qrcode)
Requires:       python3dist(python-periphery)
Requires:       python3dist(pyserial)
Requires:       python3dist(pyserial-asyncio)
Requires:       python3dist(setproctitle)
Requires:       python3dist(spidev)
Requires:       python3dist(psutil)
Requires:       python3dist(netifaces)
Requires:       python3dist(systemd-python)
Requires:       python3dist(dbus-python)
Requires:       python3dist(dbus-next)
Requires:       python3dist(pygments)
Requires:       python3dist(pyghmi)
Requires:       python3dist(python-pam)
Requires:       python3dist(pillow)
Requires:       python3dist(python-xlib)
Requires:       python3dist(xkbcommon)
Requires:       python3dist(hidapi)
Requires:       python3dist(six)
Requires:       python3dist(pyrad)
Requires:       python3dist(python-ldap)
Requires:       python3dist(zstandard)
Requires:       python3dist(mako)
# Requires:       python3dist(luma-oled)
Requires:       python3dist(pyusb)
Requires:       python3dist(pyudev)
Requires:       python3dist(gpiod) >= 2
Requires:       python3dist(ustreamer)

Requires:       v4l-utils
Requires:       iptables
Requires:       iproute
Requires:       dnsmasq
Requires:       ipmitool
Requires:       certbot
Requires:       dhclient
Requires:       nginx >= 1.25.1
Requires:       openssl
Requires:       sudo

Recommends:     tesseract
Recommends:     tesseract-langpack-eng

%description
The main PiKVM daemon, packaged for generic generic devices and/or SBCs.

%prep
%autosetup -p1 
%generate_buildrequires
%pyproject_buildrequires


# Patch sysusers to remove OLED support (avoiding i2c dependency),
# remove arch specific uucp in favor of dialout, and add video
%{__sed} -i \
    -e '/kvmd-oled/d' \
    -e 's/^m kvmd uucp$/m kvmd dialout/' \
    -e 's/^m kvmd spi$/m kvmd video/' \
    configs/os/sysusers.conf


%build
%pyproject_wheel

%install
%pyproject_install

install -Dm755 -t %{buildroot}%{_bindir} scripts/kvmd-{bootconfig,gencert,certbot}
install -dm755 %{buildroot}%{_unitdir}
cp -rd configs/os/services/* %{buildroot}%{_unitdir}/

install -DTm644 configs/os/sysusers.conf %{buildroot}%{_sysusersdir}/kvmd.conf

install -DTm644 configs/os/tmpfiles.conf %{buildroot}%{_tmpfilesdir}/kvmd.conf

# Patch tmpfiles.d to securely bootstrap Nginx volatile directories across reboots
cat << 'EOF' >> %{buildroot}%{_tmpfilesdir}/kvmd.conf
d /tmp/kvmd-nginx 0755 kvmd-nginx kvmd-nginx -
d /tmp/kvmd-nginx/client_body_temp 0755 kvmd kvmd -
EOF

mkdir -p %{buildroot}%{_datadir}/kvmd
cp -r switch hid web extras contrib/keymaps %{buildroot}%{_datadir}/kvmd
find %{buildroot}%{_datadir}/kvmd/web -name '*.pug' -delete

cfg_default=%{buildroot}%{_datadir}/kvmd/configs.default
mkdir -p $cfg_default
cp -r configs/* $cfg_default

find %{buildroot} -name '.gitignore' -delete
find $cfg_default -type f -exec chmod 444 '{}' \;
chmod 400 $cfg_default/kvmd/*passwd
chmod 400 $cfg_default/kvmd/*.secret
chmod 750 $cfg_default/os/sudoers
chmod 400 $cfg_default/os/sudoers/*

mkdir -p %{buildroot}%{_sysconfdir}/kvmd/{nginx,vnc}/ssl
chmod 755 %{buildroot}%{_sysconfdir}/kvmd/{nginx,vnc}/ssl
install -Dm444 -t %{buildroot}%{_sysconfdir}/kvmd/nginx $cfg_default/nginx/*.conf*
chmod 644 %{buildroot}%{_sysconfdir}/kvmd/nginx/{nginx,ssl}.conf*

mkdir -p %{buildroot}%{_sysconfdir}/kvmd/janus
chmod 755 %{buildroot}%{_sysconfdir}/kvmd/janus
install -Dm444 -t %{buildroot}%{_sysconfdir}/kvmd/janus $cfg_default/janus/*.jcfg

install -Dm644 -t %{buildroot}%{_sysconfdir}/kvmd $cfg_default/kvmd/*.yaml
install -Dm600 -t %{buildroot}%{_sysconfdir}/kvmd $cfg_default/kvmd/*passwd
install -Dm600 -t %{buildroot}%{_sysconfdir}/kvmd $cfg_default/kvmd/*.secret
install -Dm644 -t %{buildroot}%{_sysconfdir}/kvmd $cfg_default/kvmd/web.css
mkdir -p %{buildroot}%{_sysconfdir}/kvmd/override.d

mkdir -p %{buildroot}%{_sharedstatedir}/kvmd/{msd,pst}
chmod 1775 %{buildroot}%{_sharedstatedir}/kvmd/pst

# Add specific Generic Platform overwrites from sources
install -Dm644 -T %{SOURCE1} %{buildroot}%{_sysconfdir}/kvmd/main.yaml

# Generate custom udev rule matching the missing gpio-udev package dependency
mkdir -p %{buildroot}%{_udevrulesdir}
echo 'SUBSYSTEM=="gpio", KERNEL=="gpiochip*", GROUP="gpio", MODE="0660"' > %{buildroot}%{_udevrulesdir}/99-kvmd-generic-gpio.rules

%pre
%sysusers_create_compat configs/os/sysusers.conf

%post
%systemd_post kvmd.service kvmd-nginx.service kvmd-vnc.service kvmd-ipmi.service kvmd-pst.service kvmd-otg.service kvmd-janus.service kvmd-watchdog.service

if [ ! -e %{_sysconfdir}/kvmd/nginx/ssl/server.crt ]; then
    kvmd-gencert --do-the-thing
fi
if [ ! -e %{_sysconfdir}/kvmd/vnc/ssl/server.crt ]; then
    kvmd-gencert --do-the-thing --vnc
fi
for target in nginx vnc; do
    chown root:root %{_sysconfdir}/kvmd/$target/ssl || true
    owner="root:kvmd-$target"
    path="%{_sysconfdir}/kvmd/$target/ssl/server.key"
    if [ ! -L "$path" ]; then
        chown "$owner" "$path" || true
        chmod 440 "$path" || true
    fi
    path="%{_sysconfdir}/kvmd/$target/ssl/server.crt"
    if [ ! -L "$path" ]; then
        chown "$owner" "$path" || true
        chmod 444 "$path" || true
    fi
done

%tmpfiles_create %{_tmpfilesdir}/kvmd.conf

%preun
%systemd_preun kvmd.service kvmd-nginx.service kvmd-vnc.service kvmd-ipmi.service kvmd-pst.service kvmd-otg.service kvmd-janus.service kvmd-watchdog.service

%postun
%systemd_postun_with_restart kvmd.service kvmd-nginx.service kvmd-vnc.service kvmd-ipmi.service kvmd-pst.service kvmd-otg.service kvmd-janus.service kvmd-watchdog.service

%files
%{python3_sitelib}/kvmd*
%{_bindir}/kvmd*
%{_unitdir}/*
%{_udevrulesdir}/*.rules
%{_sysusersdir}/kvmd.conf
%{_tmpfilesdir}/kvmd.conf
%dir %{_datadir}/kvmd
%{_datadir}/kvmd/configs.default
%{_datadir}/kvmd/extras
%{_datadir}/kvmd/hid
%{_datadir}/kvmd/keymaps
%{_datadir}/kvmd/switch
%{_datadir}/kvmd/web
%dir %{_sysconfdir}/kvmd
%dir %{_sysconfdir}/kvmd/janus
%dir %{_sysconfdir}/kvmd/nginx
%dir %{_sysconfdir}/kvmd/override.d
%dir %{_sysconfdir}/kvmd/vnc
%config(noreplace) %{_sysconfdir}/kvmd/*.yaml
%config(noreplace) %attr(0600,kvmd,kvmd) %{_sysconfdir}/kvmd/htpasswd
%config(noreplace) %attr(0600,kvmd-ipmi,kvmd-ipmi) %{_sysconfdir}/kvmd/ipmipasswd
%config(noreplace) %attr(0600,kvmd-vnc,kvmd-vnc) %{_sysconfdir}/kvmd/vncpasswd
%config(noreplace) %attr(0600,kvmd,kvmd) %{_sysconfdir}/kvmd/totp.secret
%config(noreplace) %{_sysconfdir}/kvmd/web.css
%config(noreplace) %{_sysconfdir}/kvmd/janus/*.jcfg
%config(noreplace) %{_sysconfdir}/kvmd/nginx/*.conf*
%dir %{_sharedstatedir}/kvmd
%attr(-,kvmd,root) %dir %{_sharedstatedir}/kvmd/msd
%attr(-,kvmd-pst,root) %dir %{_sharedstatedir}/kvmd/pst

%changelog
%autochangelog

%global rules_file 66-gpio.rules

Name: gpio-udev-rules
Version: 1.0.1
Release: 1%{?dist}
Summary: Rules for udev to give gpio group access to operate GPIO ports
License: GPLv3+
Source0: gpio-udev.rules
BuildArch: noarch
BuildRequires: systemd-rpm-macros
Requires: systemd-udev
Requires(pre): %{_sbindir}/groupadd
Provides: group(gpio)

%description
This package creates a gpio group and provides udev rules
that grant access to GPIO ports to this group.

%prep

%build

%install
%{__install} -D -p -m 644 %{SOURCE0} %{buildroot}%{_udevrulesdir}/%{rules_file}

%pre
%{_sbindir}/groupadd -f -r gpio

%post
%udev_rules_update

%postun
%udev_rules_update

%files
%{_udevrulesdir}/%{rules_file}

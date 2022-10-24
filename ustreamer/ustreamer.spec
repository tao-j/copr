Name: ustreamer
Version: 5.24
Release: 1%{?dist}
Summary: Lightweight and fast MJPG-HTTP streamer
License: GPLv3+
URL: https://github.com/pikvm/ustreamer
Source: https://github.com/pikvm/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(libevent)
BuildRequires: pkgconfig(libevent_pthreads)
BuildRequires: pkgconfig(libbsd)
BuildRequires: pkgconfig(libgpiod)
BuildRequires: pkgconfig(libsystemd)

%description
µStreamer is a lightweight and very quick server to stream MJPG video
from any V4L2 device to the net.

All new browsers have native support of this video format,
as well as most video players such as mplayer, VLC etc.

µStreamer is a part of the Pi-KVM project designed to stream VGA and HDMI
screencast hardware data with the highest resolution and FPS possible.


%prep
%setup -q

%build
%make_build \
    CFLAGS='%{?build_cflags}' \
    LDFLAGS='%{?build_ldflags}' \
    WITH_GPIO=1 \
    WITH_SYSTEMD=1

%install
%make_install 'PREFIX=%{_prefix}'

%files
%license LICENSE
%doc README.md
%{_bindir}/ustreamer
%{_bindir}/ustreamer-dump
%{_mandir}/man1/ustreamer.1*
%{_mandir}/man1/ustreamer-dump.1*

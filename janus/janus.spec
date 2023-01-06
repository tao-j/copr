Name:           janus
Version:        1.1.1
Release:        4%{?dist}
Summary:        An open source WebRTC server designed and developed by Meetecho

License:        GPLv3 AND MIT AND BSD-3-Clause
URL:            https://janus.conf.meetecho.com/
Source0:        https://github.com/meetecho/%{name}-gateway/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.service
Source2:        %{name}.sysusers

# web resources for docs and demos
Source3:        blueimp-md5-2.6.0.min.js
Source4:        bootbox-5.4.0.min.js
Source5:        bootstrap-3.4.1.min.js
Source6:        bootstrap-slider-10.6.2.min.js
Source7:        bootstrap-slider-10.6.2.css
Source8:        bootswatch-cerulean-3.4.0.min.css
Source9:        jquery.blockUI-2.70.min.js
Source10:       jquery-1.9.1.min.js
Source11:       selfie_segmentation-0.1.1671057942.js
Source12:       spin-2.3.2.min.js
Source13:       toastr-2.1.4.min.css
Source14:       toastr-2.1.4.min.js
Source15:       webrtc-adapter-8.2.0.min.js

patch0:         0001-janus-docs-make-web-resources-local.patch
patch1:         0002-janus-demos-make-web-resources-local.patch
patch2:         0003-janus-turntest-use_parentheses.patch

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  duktape-devel
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  graphviz
BuildRequires:  intltool
BuildRequires:  jansson-devel
BuildRequires:  libavcodec-free-devel
BuildRequires:  libavformat-free-devel
BuildRequires:  libavutil-free-devel
BuildRequires:  libconfig-devel
BuildRequires:  libcurl-devel
BuildRequires:  libmicrohttpd-devel
BuildRequires:  libnice-devel
BuildRequires:  libogg
BuildRequires:  libpcap-devel
BuildRequires:  librabbitmq-devel
BuildRequires:  libsrtp-devel
BuildRequires:  libtool
BuildRequires:  libwebsockets-devel
BuildRequires:  lua-devel
BuildRequires:  nanomsg-devel
BuildRequires:  openssl-devel
BuildRequires:  opus-devel
BuildRequires:  paho-c-devel
BuildRequires:  sofia-sip-devel
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  usrsctp-devel
BuildRequires:  web-assets-devel
BuildRequires:  zlib-devel

%description
Janus is an open source WebRTC server designed and developed by Meetecho.


%package demos
BuildArch:      noarch
Summary:        The HTML demos from the %{name} website
Requires:       %{name}%{?_isa} = %{version}-%{release}


Provides:       bundled(bootstrap-slider) = 10.6.2
Provides:       bundled(bootswatch-cerulean) = 3.4.0
Provides:       bundled(js-blueimp-md5) = 2.6.0
Provides:       bundled(js-bootbox) = 5.4.0
Provides:       bundled(js-bootstrap) = 3.4.1
Provides:       bundled(js-bootstrap-slider) = 10.6.2
Provides:       bundled(js-jquery) = 1.9.1
Provides:       bundled(js-jquery.blockUI) = 2.7.0
Provides:       bundled(js-selfie_segmentation) = 0.1.1671057942
Provides:       bundled(js-spin) = 2.3.2
Provides:       bundled(js-toastr) = 2.1.4
Provides:       bundled(js-webrtc-adapter) = 8.2.0
Provides:       bundled(toastr) = 2.1.4

%description demos
The HTML demos from the %{name} website.


%package devel
Summary:        The %{name} header files and test scripts

%description devel
Development package containing header files and what is required for %{name}
plugin development, as well as some test scripts.


%package doc
BuildArch:      noarch
Summary:        Documentation files for %{name}
Requires:       js-query

Provides:       bundled(bootswatch-cerulean) = 3.4.0
Provides:       bundled(js-bootstrap) = 3.4.1

%description doc
Documentation files for %{name}.


%package eventhandlers-gelf
Summary:        GELF event handler for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description eventhandlers-gelf
GELF event handler for %{name}


%package eventhandlers-mqtt
Summary:        MQTT event handler for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description eventhandlers-mqtt
MQTT event handler for %{name}


%package eventhandlers-nanomsg
Summary:        The nanomsg event handler for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description eventhandlers-nanomsg
nanomsg event handler for %{name}


%package eventhandlers-rabbitmq
Summary:        RabbitMQ event handler for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description eventhandlers-rabbitmq
RabbitMQ event handler for %{name}


%package eventhandlers-sample
Summary:        Sample event handler for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description eventhandlers-sample
Sample event handler for %{name}


%package eventhandlers-ws
Summary:        WebSocket event handler for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description eventhandlers-ws
WebSocket event handler for %{name}


%package loggers-json
Summary:        A logger plugin for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description loggers-json
This is a trivial logger plugin for %{name}


%package plugins-audiobridge
Summary:        Audio conference bridge for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description plugins-audiobridge
This is a plugin implementing an audio conference bridge for %{name}, specifically mixing Opus streams


%package plugins-duktape
Summary:        A simple bridge to JavaScript via Duktape for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description plugins-duktape
This is a plugin that implements a simple bridge to JavaScript via Duktape for %{name}


%package plugins-echotest
Summary:        EchoTest plugin for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description plugins-echotest
This is a trivial EchoTest plugin for %{name}, just used to showcase the plugin interface


%package plugins-lua
Summary:        Simple bridge to Lua scripts for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description plugins-lua
This is a plugin that implements a simple bridge to Lua scripts for %{name}


%package plugins-nosip
Summary:        Acts as an RTP bridge for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description plugins-nosip
This is quite a basic plugin, as it only takes care of acting as an RTP bridge for %{name}


%package plugins-recordplay
Summary:        Record and playback of WebRTC messages for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description plugins-recordplay
This is a simple application that implements two different features for %{name}: it allows you to record a message you send with
WebRTC and subsequently replay this recording (or other previously recorded) through WebRTC as well


%package plugins-sip
Summary:        Allows WebRTC peers to register at a SIP server
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description plugins-sip
This is a simple SIP plugin for Janus, allowing WebRTC peers to register at a SIP server (e.g., Asterisk) and call SIP user agents
through %{name}


%package plugins-streaming
Summary:        Streaming plugin for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description plugins-streaming
This is a streaming plugin for %{name}, allowing WebRTC peers to watch/listen to pre-recorded files or media generated by another tool


%package plugins-textroom
Summary:        A DataChannel only text room for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description plugins-textroom
This is a plugin implementing a DataChannel only text room for %{name}


%package plugins-videocall
Summary:        Allows two WebRTC peers to call each other through %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description plugins-videocall
This is a simple video call plugin for Janus, allowing two WebRTC peers to call each other through %{name}


%package plugins-videoroom
Summary:        Videoconferencing SFU for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description plugins-videoroom
This is a plugin implementing a videoconferencing SFU (Selective Forwarding Unit) for %{name}, that is an audio/video router


%package plugins-voicemail
Summary:        A very simple VoiceMail service for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description plugins-voicemail
This is a plugin implementing a very simple VoiceMail service for %{name}


%package tools
Summary:        The %{name}'s helper tools
Requires:       gstreamer1.0-plugins-good

%description tools
%{name} helper tools.


%package transports-http
Summary:        RESTs transport for the %{name} API
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description transports-http
This is an implementation of a RESTs transport for the %{name} API, using the libmicrohttpd library


%package transports-mqtt
Summary:        MQTT transport for the %{name} API
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description transports-mqtt
This is an implementation of a MQTT transport for the %{name} API, using the Eclipse Paho C Client library


%package transports-nanomsg
Summary:        Nanomsg transport for the %{name} API
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description transports-nanomsg
This is an implementation of a Nanomsg transport for the %{name} API


%package transports-pfunix
Summary:        Unix Sockets transport for the %{name} API
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description transports-pfunix
This is an implementation of a Unix Sockets transport for the %{name} API


%package transports-rabbitmq
Summary:        RabbitMQ transport for the %{name} API
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description transports-rabbitmq
This is an implementation of a RabbitMQ transport for the %{name} API


%package transports-websockets
Summary:        WebSockets transport for the %{name} API
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description transports-websockets
This is an implementation of a WebSockets transport for the %{name} API


%prep
%autosetup -p 1 -n %{name}-gateway-%{version}


%build
sh autogen.sh
%configure --enable-plugin-duktape --enable-plugin-lua --enable-post-processing --enable-docs --docdir=%{_docdir}/%{name} --enable-systemd-sockets --enable-json-logger
%make_build


%check
make check


%install
%make_install

# generate configuration files
make DESTDIR=%{buildroot} configs

# put sample files in doc directory
install -d -m 755 %{buildroot}%{_docdir}/%{name}/
mv %{buildroot}%{_sysconfdir}/%{name}/*.sample %{buildroot}%{_docdir}/%{name}/

# put html files in docs dir
mv %{buildroot}%{_docdir}/%{name}/%{name}-gateway-%{version}/html %{buildroot}%{_docdir}/%{name}/
rmdir %{buildroot}%{_docdir}/%{name}/%{name}-gateway-%{version}/

# add offline web resources
## docs
### bootswatch-cerulean
install -p -D -m 0644 %{SOURCE8} %{buildroot}%{_docdir}/%{name}/html/css/

### bootstrap
install -p -D -m 0644 %{SOURCE5} %{buildroot}%{_docdir}/%{name}/html/js/

## demos
### create required directories
install -d -m 755 %{buildroot}%{_datadir}/%{name}/demos/js/

### blueimp-md5
install -p -D -m 0644 %{SOURCE3} %{buildroot}%{_datadir}/%{name}/demos/js/

### bootbox
install -p -D -m 0644 %{SOURCE4} %{buildroot}%{_datadir}/%{name}/demos/js/

### bootstrap
install -p -D -m 0644 %{SOURCE5} %{buildroot}%{_datadir}/%{name}/demos/js/

### bootstrap-slider
install -p -D -m 0644 %{SOURCE6} %{buildroot}%{_datadir}/%{name}/demos/js/
install -p -D -m 0644 %{SOURCE7} %{buildroot}%{_datadir}/%{name}/demos/css/

### bootswatch-cerulean
install -p -D -m 0644 %{SOURCE8} %{buildroot}%{_datadir}/%{name}/demos/css/

### jquery.blockUI
install -p -D -m 0644 %{SOURCE9} %{buildroot}%{_datadir}/%{name}/demos/js/

### jquery
install -p -D -m 0644 %{SOURCE10} %{buildroot}%{_datadir}/%{name}/demos/js/

### selfie_segmentation
install -p -D -m 0644 %{SOURCE11} %{buildroot}%{_datadir}/%{name}/demos/js/

### spin
install -p -D -m 0644 %{SOURCE12} %{buildroot}%{_datadir}/%{name}/demos/js/

### toastr
install -p -D -m 0644 %{SOURCE13} %{buildroot}%{_datadir}/%{name}/demos/css/
install -p -D -m 0644 %{SOURCE14} %{buildroot}%{_datadir}/%{name}/demos/js/

### webrtc-adapter
install -p -D -m 0644 %{SOURCE15} %{buildroot}%{_datadir}/%{name}/demos/js/

# systemd
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -p -D -m 0644 %{SOURCE2} %{buildroot}%{_sysusersdir}/%{name}.conf

# cleanup
rm -fr %{buildroot}%{_docdir}/%{name}-gateway

## not required in the main package acording to upstream:
## https://groups.google.com/g/meetecho-janus/c/ESCW9mQJpYc/m/ylBv2-_hAgAJ
rm -fr %{buildroot}%{_datadir}/%{name}/javascript


%pre
%sysusers_create_compat %{SOURCE2}


%post
%systemd_post %{name}.service


%preun
%systemd_preun %{name}.service


%postun
%systemd_postun_with_restart %{name}.service


%files
# licenses and docs
%license COPYING
%doc README.md
%doc SECURITY.md
%doc CHANGELOG.md
%doc %{_docdir}/%{name}/%{name}.jcfg.sample

# binaries
%{_bindir}/janus
%{_bindir}/janus-cfgconv

# manuals
%{_mandir}/man1/janus-cfgconv.1.gz
%{_mandir}/man1/janus.1.gz

# configuration
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.jcfg

# systemd service unit
%{_unitdir}/%{name}.service

# systemd sysusers
%{_sysusersdir}/%{name}.conf

# lib filesystem
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/events
%dir %{_libdir}/%{name}/loggers
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/transports

# data filesystem
%dir %{_datadir}/%{name}


## event handlers
%files eventhandlers-gelf
%doc %{_docdir}/%{name}/janus.eventhandler.gelfevh.jcfg.sample
%{_libdir}/%{name}/events/libjanus_gelfevh.so.0
%{_libdir}/%{name}/events/libjanus_gelfevh.so.0.1.1
%config(noreplace) %{_sysconfdir}/%{name}/janus.eventhandler.gelfevh.jcfg


%files eventhandlers-mqtt
%doc %{_docdir}/%{name}/janus.eventhandler.mqttevh.jcfg.sample
%{_libdir}/%{name}/events/libjanus_mqttevh.so.0
%{_libdir}/%{name}/events/libjanus_mqttevh.so.0.1.1
%config(noreplace) %{_sysconfdir}/%{name}/janus.eventhandler.mqttevh.jcfg


%files eventhandlers-nanomsg
%doc %{_docdir}/%{name}/janus.eventhandler.nanomsgevh.jcfg.sample
%{_libdir}/%{name}/events/libjanus_nanomsgevh.so.0
%{_libdir}/%{name}/events/libjanus_nanomsgevh.so.0.1.1
%config(noreplace) %{_sysconfdir}/%{name}/janus.eventhandler.nanomsgevh.jcfg


%files eventhandlers-rabbitmq
%doc %{_docdir}/%{name}/janus.eventhandler.rabbitmqevh.jcfg.sample
%{_libdir}/%{name}/events/libjanus_rabbitmqevh.so.0
%{_libdir}/%{name}/events/libjanus_rabbitmqevh.so.0.1.1
%config(noreplace) %{_sysconfdir}/%{name}/janus.eventhandler.rabbitmqevh.jcfg


%files eventhandlers-sample
%doc %{_docdir}/%{name}/janus.eventhandler.sampleevh.jcfg.sample
%{_libdir}/%{name}/events/libjanus_sampleevh.so.0
%{_libdir}/%{name}/events/libjanus_sampleevh.so.0.1.1
%config(noreplace) %{_sysconfdir}/%{name}/janus.eventhandler.sampleevh.jcfg


%files eventhandlers-ws
%doc %{_docdir}/%{name}/janus.eventhandler.wsevh.jcfg.sample
%{_libdir}/%{name}/events/libjanus_wsevh.so.0
%{_libdir}/%{name}/events/libjanus_wsevh.so.0.1.1
%config(noreplace) %{_sysconfdir}/%{name}/janus.eventhandler.wsevh.jcfg


# loggers
%files loggers-json
%doc %{_docdir}/%{name}/janus.logger.jsonlog.jcfg.sample
%{_libdir}/%{name}/loggers/libjanus_jsonlog.so.0
%{_libdir}/%{name}/loggers/libjanus_jsonlog.so.0.1.1
%config(noreplace) %{_sysconfdir}/%{name}/janus.logger.jsonlog.jcfg


## plugins
%files plugins-audiobridge
%doc %{_docdir}/%{name}/janus.plugin.audiobridge.jcfg.sample
%{_libdir}/%{name}/plugins/libjanus_audiobridge.so.0
%{_libdir}/%{name}/plugins/libjanus_audiobridge.so.0.1.1
%config(noreplace) %{_sysconfdir}/%{name}/janus.plugin.audiobridge.jcfg


%files plugins-duktape
%doc %{_docdir}/%{name}/janus.plugin.duktape.jcfg.sample
%dir %{_datadir}/%{name}/duktape
%{_datadir}/%{name}/duktape/echotest.js
%{_datadir}/%{name}/duktape/janus-sdp.js
%{_libdir}/%{name}/plugins/libjanus_duktape.so.0
%{_libdir}/%{name}/plugins/libjanus_duktape.so.0.1.1
%config(noreplace) %{_sysconfdir}/%{name}/janus.plugin.duktape.jcfg


%files plugins-echotest
%doc %{_docdir}/%{name}/janus.plugin.echotest.jcfg.sample
%{_libdir}/%{name}/plugins/libjanus_echotest.so.0
%{_libdir}/%{name}/plugins/libjanus_echotest.so.0.1.1
%config(noreplace) %{_sysconfdir}/%{name}/janus.plugin.echotest.jcfg


%files plugins-lua
%doc %{_docdir}/%{name}/janus.plugin.lua.jcfg.sample
%dir %{_datadir}/%{name}/lua
%{_datadir}/%{name}/lua/echotest.lua
%{_datadir}/%{name}/lua/janus-logger.lua
%{_datadir}/%{name}/lua/janus-sdp.lua
%{_datadir}/%{name}/lua/videoroom.lua
%{_libdir}/%{name}/plugins/libjanus_lua.so.0
%{_libdir}/%{name}/plugins/libjanus_lua.so.0.1.1
%config(noreplace) %{_sysconfdir}/%{name}/janus.plugin.lua.jcfg


%files plugins-nosip
%doc %{_docdir}/%{name}/janus.plugin.nosip.jcfg.sample
%{_libdir}/%{name}/plugins/libjanus_nosip.so.0
%{_libdir}/%{name}/plugins/libjanus_nosip.so.0.1.1
%config(noreplace) %{_sysconfdir}/%{name}/janus.plugin.nosip.jcfg


%files plugins-recordplay
%doc %{_docdir}/%{name}/janus.plugin.recordplay.jcfg.sample
%dir %{_datadir}/%{name}/recordings
%{_datadir}/%{name}/recordings/1234.nfo
%{_datadir}/%{name}/recordings/rec-sample-audio.mjr
%{_datadir}/%{name}/recordings/rec-sample-video.mjr
%{_libdir}/%{name}/plugins/libjanus_recordplay.so.0
%{_libdir}/%{name}/plugins/libjanus_recordplay.so.0.1.1
%config(noreplace) %{_sysconfdir}/%{name}/janus.plugin.recordplay.jcfg


%files plugins-sip
%doc %{_docdir}/%{name}/janus.plugin.sip.jcfg.sample
%{_libdir}/%{name}/plugins/libjanus_sip.so.0
%{_libdir}/%{name}/plugins/libjanus_sip.so.0.1.1
%config(noreplace) %{_sysconfdir}/%{name}/janus.plugin.sip.jcfg


%files plugins-streaming
%doc %{_docdir}/%{name}/janus.plugin.streaming.jcfg.sample
%dir %{_datadir}/%{name}/streams
%{_datadir}/%{name}/streams/music.mulaw
%{_datadir}/%{name}/streams/radio.alaw
%{_datadir}/%{name}/streams/test_gstreamer.sh
%{_datadir}/%{name}/streams/test_gstreamer1.sh
%{_datadir}/%{name}/streams/test_gstreamer1_multistream.sh
%{_datadir}/%{name}/streams/test_gstreamer_multistream.sh
%{_libdir}/%{name}/plugins/libjanus_streaming.so.0
%{_libdir}/%{name}/plugins/libjanus_streaming.so.0.1.1
%config(noreplace) %{_sysconfdir}/%{name}/janus.plugin.streaming.jcfg


%files plugins-textroom
%doc %{_docdir}/%{name}/janus.plugin.textroom.jcfg.sample
%{_libdir}/%{name}/plugins/libjanus_textroom.so.0
%{_libdir}/%{name}/plugins/libjanus_textroom.so.0.1.1
%config(noreplace) %{_sysconfdir}/%{name}/janus.plugin.textroom.jcfg


%files plugins-videocall
%doc %{_docdir}/%{name}/janus.plugin.videocall.jcfg.sample
%{_libdir}/%{name}/plugins/libjanus_videocall.so.0
%{_libdir}/%{name}/plugins/libjanus_videocall.so.0.1.1
%config(noreplace) %{_sysconfdir}/%{name}/janus.plugin.videocall.jcfg


%files plugins-videoroom
%doc %{_docdir}/%{name}/janus.plugin.videoroom.jcfg.sample
%{_libdir}/%{name}/plugins/libjanus_videoroom.so.0
%{_libdir}/%{name}/plugins/libjanus_videoroom.so.0.1.1
%config(noreplace) %{_sysconfdir}/%{name}/janus.plugin.videoroom.jcfg


%files plugins-voicemail
%doc %{_docdir}/%{name}/janus.plugin.voicemail.jcfg.sample
%{_libdir}/%{name}/plugins/libjanus_voicemail.so.0
%{_libdir}/%{name}/plugins/libjanus_voicemail.so.0.1.1
%config(noreplace) %{_sysconfdir}/%{name}/janus.plugin.voicemail.jcfg


# transports
%files transports-http
%doc %{_docdir}/%{name}/janus.transport.http.jcfg.sample
%{_libdir}/%{name}/transports/libjanus_http.so.0
%{_libdir}/%{name}/transports/libjanus_http.so.0.1.1
%config(noreplace) %{_sysconfdir}/%{name}/janus.transport.http.jcfg


%files transports-mqtt
%doc %{_docdir}/%{name}/janus.transport.mqtt.jcfg.sample
%{_libdir}/%{name}/transports/libjanus_mqtt.so.0
%{_libdir}/%{name}/transports/libjanus_mqtt.so.0.1.1
%config(noreplace) %{_sysconfdir}/%{name}/janus.transport.mqtt.jcfg


%files transports-nanomsg
%doc %{_docdir}/%{name}/janus.transport.nanomsg.jcfg.sample
%{_libdir}/%{name}/transports/libjanus_nanomsg.so.0
%{_libdir}/%{name}/transports/libjanus_nanomsg.so.0.1.1
%config(noreplace) %{_sysconfdir}/%{name}/janus.transport.nanomsg.jcfg


%files transports-pfunix
%doc %{_docdir}/%{name}/janus.transport.pfunix.jcfg.sample
%{_libdir}/%{name}/transports/libjanus_pfunix.so.0
%{_libdir}/%{name}/transports/libjanus_pfunix.so.0.1.1
%config(noreplace) %{_sysconfdir}/%{name}/janus.transport.pfunix.jcfg


%files transports-rabbitmq
%doc %{_docdir}/%{name}/janus.transport.rabbitmq.jcfg.sample
%{_libdir}/%{name}/transports/libjanus_rabbitmq.so.0
%{_libdir}/%{name}/transports/libjanus_rabbitmq.so.0.1.1
%config(noreplace) %{_sysconfdir}/%{name}/janus.transport.rabbitmq.jcfg


%files transports-websockets
%doc %{_docdir}/%{name}/janus.transport.websockets.jcfg.sample
%{_libdir}/%{name}/transports/libjanus_websockets.so.0
%{_libdir}/%{name}/transports/libjanus_websockets.so.0.1.1
%config(noreplace) %{_sysconfdir}/%{name}/janus.transport.websockets.jcfg


%files demos
%dir %{_datadir}/%{name}/demos
%dir %{_datadir}/%{name}/demos/background
%dir %{_datadir}/%{name}/demos/css
%dir %{_datadir}/%{name}/demos/docs
%dir %{_datadir}/%{name}/demos/js
%dir %{_datadir}/%{name}/demos/surround
%{_datadir}/%{name}/demos/admin.html
%{_datadir}/%{name}/demos/admin.js
%{_datadir}/%{name}/demos/audiobridgetest.html
%{_datadir}/%{name}/demos/audiobridgetest.js
%{_datadir}/%{name}/demos/background/retro.webp
%{_datadir}/%{name}/demos/canvas.html
%{_datadir}/%{name}/demos/canvas.js
%{_datadir}/%{name}/demos/citeus.html
%{_datadir}/%{name}/demos/css/bootstrap-slider-10.6.2.css
%{_datadir}/%{name}/demos/css/bootswatch-cerulean-3.4.0.min.css
%{_datadir}/%{name}/demos/css/demo.css
%{_datadir}/%{name}/demos/css/toastr-2.1.4.min.css
%{_datadir}/%{name}/demos/demos.html
%{_datadir}/%{name}/demos/devicetest.html
%{_datadir}/%{name}/demos/devicetest.js
%{_datadir}/%{name}/demos/docs/index.html
%{_datadir}/%{name}/demos/e2etest.html
%{_datadir}/%{name}/demos/e2etest.js
%{_datadir}/%{name}/demos/echotest.html
%{_datadir}/%{name}/demos/echotest.js
%{_datadir}/%{name}/demos/favicon.ico
%{_datadir}/%{name}/demos/footer.html
%{_datadir}/%{name}/demos/index.html
%{_datadir}/%{name}/demos/janus-logo-small.png
%{_datadir}/%{name}/demos/janus-logo.png
%{_datadir}/%{name}/demos/janus.js
%{_datadir}/%{name}/demos/js/blueimp-md5-2.6.0.min.js
%{_datadir}/%{name}/demos/js/bootbox-5.4.0.min.js
%{_datadir}/%{name}/demos/js/bootstrap-3.4.1.min.js
%{_datadir}/%{name}/demos/js/bootstrap-slider-10.6.2.min.js
%{_datadir}/%{name}/demos/js/jquery-1.9.1.min.js
%{_datadir}/%{name}/demos/js/jquery.blockUI-2.70.min.js
%{_datadir}/%{name}/demos/js/selfie_segmentation-0.1.1671057942.js
%{_datadir}/%{name}/demos/js/spin-2.3.2.min.js
%{_datadir}/%{name}/demos/js/toastr-2.1.4.min.js
%{_datadir}/%{name}/demos/js/webrtc-adapter-8.2.0.min.js
%{_datadir}/%{name}/demos/meetecho-logo.png
%{_datadir}/%{name}/demos/multiopus.html
%{_datadir}/%{name}/demos/multiopus.js
%{_datadir}/%{name}/demos/mvideoroomtest.html
%{_datadir}/%{name}/demos/mvideoroomtest.js
%{_datadir}/%{name}/demos/navbar.html
%{_datadir}/%{name}/demos/nosiptest.html
%{_datadir}/%{name}/demos/nosiptest.js
%{_datadir}/%{name}/demos/recordplaytest.html
%{_datadir}/%{name}/demos/recordplaytest.js
%{_datadir}/%{name}/demos/screensharingtest.html
%{_datadir}/%{name}/demos/screensharingtest.js
%{_datadir}/%{name}/demos/settings.js
%{_datadir}/%{name}/demos/siptest.html
%{_datadir}/%{name}/demos/siptest.js
%{_datadir}/%{name}/demos/streamingtest.html
%{_datadir}/%{name}/demos/streamingtest.js
%{_datadir}/%{name}/demos/support.html
%{_datadir}/%{name}/demos/surround/ChID-BLITS-EBU.mp4
%{_datadir}/%{name}/demos/surround/ChID-BLITS-EBU.txt
%{_datadir}/%{name}/demos/textroomtest.html
%{_datadir}/%{name}/demos/textroomtest.js
%{_datadir}/%{name}/demos/up_arrow.png
%{_datadir}/%{name}/demos/videocalltest.html
%{_datadir}/%{name}/demos/videocalltest.js
%{_datadir}/%{name}/demos/videoroomtest.html
%{_datadir}/%{name}/demos/videoroomtest.js
%{_datadir}/%{name}/demos/virtualbg.html
%{_datadir}/%{name}/demos/virtualbg.js
%{_datadir}/%{name}/demos/voicemailtest.html
%{_datadir}/%{name}/demos/voicemailtest.js
%{_datadir}/%{name}/demos/vp9svctest.html
%{_datadir}/%{name}/demos/vp9svctest.js
%{_datadir}/%{name}/demos/webaudio.html
%{_datadir}/%{name}/demos/webaudio.js


%files devel
%dir %{_includedir}/%{name}
%dir %{_includedir}/%{name}/events
%dir %{_includedir}/%{name}/loggers
%dir %{_includedir}/%{name}/plugins
%dir %{_includedir}/%{name}/transports

# headers for plugin development
%{_includedir}/%{name}/apierror.h
%{_includedir}/%{name}/config.h
%{_includedir}/%{name}/debug.h
%{_includedir}/%{name}/events/eventhandler.h
%{_includedir}/%{name}/ip-utils.h
%{_includedir}/%{name}/log.h
%{_includedir}/%{name}/loggers/logger.h
%{_includedir}/%{name}/mutex.h
%{_includedir}/%{name}/plugins/plugin.h
%{_includedir}/%{name}/record.h
%{_includedir}/%{name}/refcount.h
%{_includedir}/%{name}/rtcp.h
%{_includedir}/%{name}/rtp.h
%{_includedir}/%{name}/rtpsrtp.h
%{_includedir}/%{name}/sdp-utils.h
%{_includedir}/%{name}/text2pcap.h
%{_includedir}/%{name}/transports/transport.h
%{_includedir}/%{name}/utils.h

# unversioned shared objects (plugins)
%{_libdir}/%{name}/events/libjanus_gelfevh.so
%{_libdir}/%{name}/events/libjanus_mqttevh.so
%{_libdir}/%{name}/events/libjanus_nanomsgevh.so
%{_libdir}/%{name}/events/libjanus_rabbitmqevh.so
%{_libdir}/%{name}/events/libjanus_sampleevh.so
%{_libdir}/%{name}/events/libjanus_wsevh.so
%{_libdir}/%{name}/loggers/libjanus_jsonlog.so
%{_libdir}/%{name}/plugins/libjanus_audiobridge.so
%{_libdir}/%{name}/plugins/libjanus_duktape.so
%{_libdir}/%{name}/plugins/libjanus_echotest.so
%{_libdir}/%{name}/plugins/libjanus_lua.so
%{_libdir}/%{name}/plugins/libjanus_nosip.so
%{_libdir}/%{name}/plugins/libjanus_recordplay.so
%{_libdir}/%{name}/plugins/libjanus_sip.so
%{_libdir}/%{name}/plugins/libjanus_streaming.so
%{_libdir}/%{name}/plugins/libjanus_textroom.so
%{_libdir}/%{name}/plugins/libjanus_videocall.so
%{_libdir}/%{name}/plugins/libjanus_videoroom.so
%{_libdir}/%{name}/plugins/libjanus_voicemail.so
%{_libdir}/%{name}/transports/libjanus_http.so
%{_libdir}/%{name}/transports/libjanus_mqtt.so
%{_libdir}/%{name}/transports/libjanus_nanomsg.so
%{_libdir}/%{name}/transports/libjanus_pfunix.so
%{_libdir}/%{name}/transports/libjanus_rabbitmq.so
%{_libdir}/%{name}/transports/libjanus_websockets.so


%files doc
%license %{_docdir}/%{name}/html/COPYING.html
%doc %{_docdir}/%{name}/CHANGELOG.md
%doc %{_docdir}/%{name}/README.md
%doc %{_docdir}/%{name}/SECURITY.md
%dir %{_docdir}/%{name}
%dir %{_docdir}/%{name}/html
%dir %{_docdir}/%{name}/html/css
%dir %{_docdir}/%{name}/html/js
%dir %{_docdir}/%{name}/html/search
%{_docdir}/%{name}/html/CHANGELOG.html
%{_docdir}/%{name}/html/CREDITS.html
%{_docdir}/%{name}/html/DEPS.html
%{_docdir}/%{name}/html/FAQ.html
%{_docdir}/%{name}/html/JS.html
%{_docdir}/%{name}/html/README.html
%{_docdir}/%{name}/html/admin.html
%{_docdir}/%{name}/html/annotated.html
%{_docdir}/%{name}/html/apierror_8c.html
%{_docdir}/%{name}/html/apierror_8c__incl.map
%{_docdir}/%{name}/html/apierror_8c__incl.md5
%{_docdir}/%{name}/html/apierror_8c__incl.png
%{_docdir}/%{name}/html/apierror_8h.html
%{_docdir}/%{name}/html/apierror_8h__dep__incl.map
%{_docdir}/%{name}/html/apierror_8h__dep__incl.md5
%{_docdir}/%{name}/html/apierror_8h__dep__incl.png
%{_docdir}/%{name}/html/apierror_8h_source.html
%{_docdir}/%{name}/html/audiobridge.html
%{_docdir}/%{name}/html/auth.html
%{_docdir}/%{name}/html/auth_8c.html
%{_docdir}/%{name}/html/auth_8c__incl.map
%{_docdir}/%{name}/html/auth_8c__incl.md5
%{_docdir}/%{name}/html/auth_8c__incl.png
%{_docdir}/%{name}/html/auth_8h.html
%{_docdir}/%{name}/html/auth_8h__dep__incl.map
%{_docdir}/%{name}/html/auth_8h__dep__incl.md5
%{_docdir}/%{name}/html/auth_8h__dep__incl.png
%{_docdir}/%{name}/html/auth_8h__incl.map
%{_docdir}/%{name}/html/auth_8h__incl.md5
%{_docdir}/%{name}/html/auth_8h__incl.png
%{_docdir}/%{name}/html/auth_8h_source.html
%{_docdir}/%{name}/html/bc_s.png
%{_docdir}/%{name}/html/bc_sd.png
%{_docdir}/%{name}/html/bdwn.png
%{_docdir}/%{name}/html/classes.html
%{_docdir}/%{name}/html/closed.png
%{_docdir}/%{name}/html/config_8c.html
%{_docdir}/%{name}/html/config_8c__incl.map
%{_docdir}/%{name}/html/config_8c__incl.md5
%{_docdir}/%{name}/html/config_8c__incl.png
%{_docdir}/%{name}/html/config_8h.html
%{_docdir}/%{name}/html/config_8h__dep__incl.map
%{_docdir}/%{name}/html/config_8h__dep__incl.md5
%{_docdir}/%{name}/html/config_8h__dep__incl.png
%{_docdir}/%{name}/html/config_8h__incl.map
%{_docdir}/%{name}/html/config_8h__incl.md5
%{_docdir}/%{name}/html/config_8h__incl.png
%{_docdir}/%{name}/html/config_8h_source.html
%{_docdir}/%{name}/html/css/bootswatch-cerulean-3.4.0.min.css
%{_docdir}/%{name}/html/css/demo.css
%{_docdir}/%{name}/html/debug.html
%{_docdir}/%{name}/html/debug_8h.html
%{_docdir}/%{name}/html/debug_8h__dep__incl.map
%{_docdir}/%{name}/html/debug_8h__dep__incl.md5
%{_docdir}/%{name}/html/debug_8h__dep__incl.png
%{_docdir}/%{name}/html/debug_8h__incl.map
%{_docdir}/%{name}/html/debug_8h__incl.md5
%{_docdir}/%{name}/html/debug_8h__incl.png
%{_docdir}/%{name}/html/debug_8h_source.html
%{_docdir}/%{name}/html/deploy.html
%{_docdir}/%{name}/html/dir_000004_000000.html
%{_docdir}/%{name}/html/dir_000004_000001.html
%{_docdir}/%{name}/html/dir_000004_000002.html
%{_docdir}/%{name}/html/dir_000004_000005.html
%{_docdir}/%{name}/html/dir_14e1e259e8275dc0c459acef3bbf05ae.html
%{_docdir}/%{name}/html/dir_14e1e259e8275dc0c459acef3bbf05ae_dep.map
%{_docdir}/%{name}/html/dir_14e1e259e8275dc0c459acef3bbf05ae_dep.md5
%{_docdir}/%{name}/html/dir_14e1e259e8275dc0c459acef3bbf05ae_dep.png
%{_docdir}/%{name}/html/dir_4ef9e1fab6db8f1c439d7edf0c56068f.html
%{_docdir}/%{name}/html/dir_4ef9e1fab6db8f1c439d7edf0c56068f_dep.map
%{_docdir}/%{name}/html/dir_4ef9e1fab6db8f1c439d7edf0c56068f_dep.md5
%{_docdir}/%{name}/html/dir_4ef9e1fab6db8f1c439d7edf0c56068f_dep.png
%{_docdir}/%{name}/html/dir_68267d1309a1af8e8297ef4c3efbcdba.html
%{_docdir}/%{name}/html/dir_68267d1309a1af8e8297ef4c3efbcdba_dep.map
%{_docdir}/%{name}/html/dir_68267d1309a1af8e8297ef4c3efbcdba_dep.md5
%{_docdir}/%{name}/html/dir_68267d1309a1af8e8297ef4c3efbcdba_dep.png
%{_docdir}/%{name}/html/dir_7020b8b7abcceffa3f9f7a2d24718f16.html
%{_docdir}/%{name}/html/dir_7020b8b7abcceffa3f9f7a2d24718f16_dep.map
%{_docdir}/%{name}/html/dir_7020b8b7abcceffa3f9f7a2d24718f16_dep.md5
%{_docdir}/%{name}/html/dir_7020b8b7abcceffa3f9f7a2d24718f16_dep.png
%{_docdir}/%{name}/html/dir_c9597c06ffdd5cc3c0a43db5afd620b2.html
%{_docdir}/%{name}/html/dir_c9597c06ffdd5cc3c0a43db5afd620b2_dep.map
%{_docdir}/%{name}/html/dir_c9597c06ffdd5cc3c0a43db5afd620b2_dep.md5
%{_docdir}/%{name}/html/dir_c9597c06ffdd5cc3c0a43db5afd620b2_dep.png
%{_docdir}/%{name}/html/dir_e272343b3e18644714a39f7f10eded81.html
%{_docdir}/%{name}/html/dir_e272343b3e18644714a39f7f10eded81_dep.map
%{_docdir}/%{name}/html/dir_e272343b3e18644714a39f7f10eded81_dep.md5
%{_docdir}/%{name}/html/dir_e272343b3e18644714a39f7f10eded81_dep.png
%{_docdir}/%{name}/html/doc.png
%{_docdir}/%{name}/html/docd.png
%{_docdir}/%{name}/html/doxy-boot.js
%{_docdir}/%{name}/html/doxygen.css
%{_docdir}/%{name}/html/doxygen.svg
%{_docdir}/%{name}/html/dtls-bio_8c.html
%{_docdir}/%{name}/html/dtls-bio_8c__incl.map
%{_docdir}/%{name}/html/dtls-bio_8c__incl.md5
%{_docdir}/%{name}/html/dtls-bio_8c__incl.png
%{_docdir}/%{name}/html/dtls-bio_8h.html
%{_docdir}/%{name}/html/dtls-bio_8h__dep__incl.map
%{_docdir}/%{name}/html/dtls-bio_8h__dep__incl.md5
%{_docdir}/%{name}/html/dtls-bio_8h__dep__incl.png
%{_docdir}/%{name}/html/dtls-bio_8h__incl.map
%{_docdir}/%{name}/html/dtls-bio_8h__incl.md5
%{_docdir}/%{name}/html/dtls-bio_8h__incl.png
%{_docdir}/%{name}/html/dtls-bio_8h_source.html
%{_docdir}/%{name}/html/dtls_8c.html
%{_docdir}/%{name}/html/dtls_8c__incl.map
%{_docdir}/%{name}/html/dtls_8c__incl.md5
%{_docdir}/%{name}/html/dtls_8c__incl.png
%{_docdir}/%{name}/html/dtls_8h.html
%{_docdir}/%{name}/html/dtls_8h__dep__incl.map
%{_docdir}/%{name}/html/dtls_8h__dep__incl.md5
%{_docdir}/%{name}/html/dtls_8h__dep__incl.png
%{_docdir}/%{name}/html/dtls_8h__incl.map
%{_docdir}/%{name}/html/dtls_8h__incl.md5
%{_docdir}/%{name}/html/dtls_8h__incl.png
%{_docdir}/%{name}/html/dtls_8h_source.html
%{_docdir}/%{name}/html/duktape.html
%{_docdir}/%{name}/html/dynsections.js
%{_docdir}/%{name}/html/echotest.html
%{_docdir}/%{name}/html/eventhandler_8h.html
%{_docdir}/%{name}/html/eventhandler_8h__dep__incl.map
%{_docdir}/%{name}/html/eventhandler_8h__dep__incl.md5
%{_docdir}/%{name}/html/eventhandler_8h__dep__incl.png
%{_docdir}/%{name}/html/eventhandler_8h__incl.map
%{_docdir}/%{name}/html/eventhandler_8h__incl.md5
%{_docdir}/%{name}/html/eventhandler_8h__incl.png
%{_docdir}/%{name}/html/eventhandler_8h_source.html
%{_docdir}/%{name}/html/eventhandlers.html
%{_docdir}/%{name}/html/events_8c.html
%{_docdir}/%{name}/html/events_8c__incl.map
%{_docdir}/%{name}/html/events_8c__incl.md5
%{_docdir}/%{name}/html/events_8c__incl.png
%{_docdir}/%{name}/html/events_8h.html
%{_docdir}/%{name}/html/events_8h__dep__incl.map
%{_docdir}/%{name}/html/events_8h__dep__incl.md5
%{_docdir}/%{name}/html/events_8h__dep__incl.png
%{_docdir}/%{name}/html/events_8h__incl.map
%{_docdir}/%{name}/html/events_8h__incl.md5
%{_docdir}/%{name}/html/events_8h__incl.png
%{_docdir}/%{name}/html/events_8h_source.html
%{_docdir}/%{name}/html/favicon.ico
%{_docdir}/%{name}/html/files.html
%{_docdir}/%{name}/html/folderclosed.png
%{_docdir}/%{name}/html/folderopen.png
%{_docdir}/%{name}/html/functions.html
%{_docdir}/%{name}/html/functions_b.html
%{_docdir}/%{name}/html/functions_c.html
%{_docdir}/%{name}/html/functions_d.html
%{_docdir}/%{name}/html/functions_e.html
%{_docdir}/%{name}/html/functions_f.html
%{_docdir}/%{name}/html/functions_g.html
%{_docdir}/%{name}/html/functions_h.html
%{_docdir}/%{name}/html/functions_i.html
%{_docdir}/%{name}/html/functions_j.html
%{_docdir}/%{name}/html/functions_k.html
%{_docdir}/%{name}/html/functions_l.html
%{_docdir}/%{name}/html/functions_m.html
%{_docdir}/%{name}/html/functions_n.html
%{_docdir}/%{name}/html/functions_o.html
%{_docdir}/%{name}/html/functions_p.html
%{_docdir}/%{name}/html/functions_q.html
%{_docdir}/%{name}/html/functions_r.html
%{_docdir}/%{name}/html/functions_s.html
%{_docdir}/%{name}/html/functions_t.html
%{_docdir}/%{name}/html/functions_u.html
%{_docdir}/%{name}/html/functions_v.html
%{_docdir}/%{name}/html/functions_vars.html
%{_docdir}/%{name}/html/functions_vars_b.html
%{_docdir}/%{name}/html/functions_vars_c.html
%{_docdir}/%{name}/html/functions_vars_d.html
%{_docdir}/%{name}/html/functions_vars_e.html
%{_docdir}/%{name}/html/functions_vars_f.html
%{_docdir}/%{name}/html/functions_vars_g.html
%{_docdir}/%{name}/html/functions_vars_h.html
%{_docdir}/%{name}/html/functions_vars_i.html
%{_docdir}/%{name}/html/functions_vars_j.html
%{_docdir}/%{name}/html/functions_vars_k.html
%{_docdir}/%{name}/html/functions_vars_l.html
%{_docdir}/%{name}/html/functions_vars_m.html
%{_docdir}/%{name}/html/functions_vars_n.html
%{_docdir}/%{name}/html/functions_vars_o.html
%{_docdir}/%{name}/html/functions_vars_p.html
%{_docdir}/%{name}/html/functions_vars_q.html
%{_docdir}/%{name}/html/functions_vars_r.html
%{_docdir}/%{name}/html/functions_vars_s.html
%{_docdir}/%{name}/html/functions_vars_t.html
%{_docdir}/%{name}/html/functions_vars_u.html
%{_docdir}/%{name}/html/functions_vars_v.html
%{_docdir}/%{name}/html/functions_vars_w.html
%{_docdir}/%{name}/html/functions_w.html
%{_docdir}/%{name}/html/globals.html
%{_docdir}/%{name}/html/globals_b.html
%{_docdir}/%{name}/html/globals_c.html
%{_docdir}/%{name}/html/globals_d.html
%{_docdir}/%{name}/html/globals_defs.html
%{_docdir}/%{name}/html/globals_defs_b.html
%{_docdir}/%{name}/html/globals_defs_c.html
%{_docdir}/%{name}/html/globals_defs_d.html
%{_docdir}/%{name}/html/globals_defs_g.html
%{_docdir}/%{name}/html/globals_defs_h.html
%{_docdir}/%{name}/html/globals_defs_i.html
%{_docdir}/%{name}/html/globals_defs_j.html
%{_docdir}/%{name}/html/globals_defs_l.html
%{_docdir}/%{name}/html/globals_defs_m.html
%{_docdir}/%{name}/html/globals_defs_n.html
%{_docdir}/%{name}/html/globals_defs_o.html
%{_docdir}/%{name}/html/globals_defs_p.html
%{_docdir}/%{name}/html/globals_defs_r.html
%{_docdir}/%{name}/html/globals_defs_s.html
%{_docdir}/%{name}/html/globals_defs_t.html
%{_docdir}/%{name}/html/globals_defs_u.html
%{_docdir}/%{name}/html/globals_defs_v.html
%{_docdir}/%{name}/html/globals_defs_w.html
%{_docdir}/%{name}/html/globals_e.html
%{_docdir}/%{name}/html/globals_enum.html
%{_docdir}/%{name}/html/globals_eval.html
%{_docdir}/%{name}/html/globals_func.html
%{_docdir}/%{name}/html/globals_func_c.html
%{_docdir}/%{name}/html/globals_func_j.html
%{_docdir}/%{name}/html/globals_func_l.html
%{_docdir}/%{name}/html/globals_func_m.html
%{_docdir}/%{name}/html/globals_func_o.html
%{_docdir}/%{name}/html/globals_g.html
%{_docdir}/%{name}/html/globals_h.html
%{_docdir}/%{name}/html/globals_i.html
%{_docdir}/%{name}/html/globals_j.html
%{_docdir}/%{name}/html/globals_l.html
%{_docdir}/%{name}/html/globals_m.html
%{_docdir}/%{name}/html/globals_n.html
%{_docdir}/%{name}/html/globals_o.html
%{_docdir}/%{name}/html/globals_p.html
%{_docdir}/%{name}/html/globals_q.html
%{_docdir}/%{name}/html/globals_r.html
%{_docdir}/%{name}/html/globals_s.html
%{_docdir}/%{name}/html/globals_t.html
%{_docdir}/%{name}/html/globals_type.html
%{_docdir}/%{name}/html/globals_type_e.html
%{_docdir}/%{name}/html/globals_type_j.html
%{_docdir}/%{name}/html/globals_type_m.html
%{_docdir}/%{name}/html/globals_type_p.html
%{_docdir}/%{name}/html/globals_type_r.html
%{_docdir}/%{name}/html/globals_type_s.html
%{_docdir}/%{name}/html/globals_type_w.html
%{_docdir}/%{name}/html/globals_u.html
%{_docdir}/%{name}/html/globals_v.html
%{_docdir}/%{name}/html/globals_vars.html
%{_docdir}/%{name}/html/globals_w.html
%{_docdir}/%{name}/html/graph_legend.html
%{_docdir}/%{name}/html/graph_legend.md5
%{_docdir}/%{name}/html/graph_legend.png
%{_docdir}/%{name}/html/group__core.html
%{_docdir}/%{name}/html/group__core.map
%{_docdir}/%{name}/html/group__core.md5
%{_docdir}/%{name}/html/group__core.png
%{_docdir}/%{name}/html/group__eventhandlerapi.html
%{_docdir}/%{name}/html/group__eventhandlerapi.map
%{_docdir}/%{name}/html/group__eventhandlerapi.md5
%{_docdir}/%{name}/html/group__eventhandlerapi.png
%{_docdir}/%{name}/html/group__eventhandlers.html
%{_docdir}/%{name}/html/group__eventhandlers.map
%{_docdir}/%{name}/html/group__eventhandlers.md5
%{_docdir}/%{name}/html/group__eventhandlers.png
%{_docdir}/%{name}/html/group__jspapi.html
%{_docdir}/%{name}/html/group__jspapi.map
%{_docdir}/%{name}/html/group__jspapi.md5
%{_docdir}/%{name}/html/group__jspapi.png
%{_docdir}/%{name}/html/group__loggerapi.html
%{_docdir}/%{name}/html/group__loggerapi.map
%{_docdir}/%{name}/html/group__loggerapi.md5
%{_docdir}/%{name}/html/group__loggerapi.png
%{_docdir}/%{name}/html/group__loggers.html
%{_docdir}/%{name}/html/group__loggers.map
%{_docdir}/%{name}/html/group__loggers.md5
%{_docdir}/%{name}/html/group__loggers.png
%{_docdir}/%{name}/html/group__luapapi.html
%{_docdir}/%{name}/html/group__luapapi.map
%{_docdir}/%{name}/html/group__luapapi.md5
%{_docdir}/%{name}/html/group__luapapi.png
%{_docdir}/%{name}/html/group__pluginapi.html
%{_docdir}/%{name}/html/group__pluginapi.map
%{_docdir}/%{name}/html/group__pluginapi.md5
%{_docdir}/%{name}/html/group__pluginapi.png
%{_docdir}/%{name}/html/group__plugins.html
%{_docdir}/%{name}/html/group__plugins.map
%{_docdir}/%{name}/html/group__plugins.md5
%{_docdir}/%{name}/html/group__plugins.png
%{_docdir}/%{name}/html/group__postprocessing.html
%{_docdir}/%{name}/html/group__postprocessing.map
%{_docdir}/%{name}/html/group__postprocessing.md5
%{_docdir}/%{name}/html/group__postprocessing.png
%{_docdir}/%{name}/html/group__protocols.html
%{_docdir}/%{name}/html/group__protocols.map
%{_docdir}/%{name}/html/group__protocols.md5
%{_docdir}/%{name}/html/group__protocols.png
%{_docdir}/%{name}/html/group__tools.html
%{_docdir}/%{name}/html/group__tools.map
%{_docdir}/%{name}/html/group__tools.md5
%{_docdir}/%{name}/html/group__tools.png
%{_docdir}/%{name}/html/group__transportapi.html
%{_docdir}/%{name}/html/group__transportapi.map
%{_docdir}/%{name}/html/group__transportapi.md5
%{_docdir}/%{name}/html/group__transportapi.png
%{_docdir}/%{name}/html/group__transports.html
%{_docdir}/%{name}/html/group__transports.map
%{_docdir}/%{name}/html/group__transports.md5
%{_docdir}/%{name}/html/group__transports.png
%{_docdir}/%{name}/html/ice_8c.html
%{_docdir}/%{name}/html/ice_8c__incl.map
%{_docdir}/%{name}/html/ice_8c__incl.md5
%{_docdir}/%{name}/html/ice_8c__incl.png
%{_docdir}/%{name}/html/ice_8h.html
%{_docdir}/%{name}/html/ice_8h__dep__incl.map
%{_docdir}/%{name}/html/ice_8h__dep__incl.md5
%{_docdir}/%{name}/html/ice_8h__dep__incl.png
%{_docdir}/%{name}/html/ice_8h__incl.map
%{_docdir}/%{name}/html/ice_8h__incl.md5
%{_docdir}/%{name}/html/ice_8h__incl.png
%{_docdir}/%{name}/html/ice_8h_source.html
%{_docdir}/%{name}/html/ide.html
%{_docdir}/%{name}/html/index.html
%{_docdir}/%{name}/html/ip-utils_8c.html
%{_docdir}/%{name}/html/ip-utils_8c__incl.map
%{_docdir}/%{name}/html/ip-utils_8c__incl.md5
%{_docdir}/%{name}/html/ip-utils_8c__incl.png
%{_docdir}/%{name}/html/ip-utils_8h.html
%{_docdir}/%{name}/html/ip-utils_8h__dep__incl.map
%{_docdir}/%{name}/html/ip-utils_8h__dep__incl.md5
%{_docdir}/%{name}/html/ip-utils_8h__dep__incl.png
%{_docdir}/%{name}/html/ip-utils_8h__incl.map
%{_docdir}/%{name}/html/ip-utils_8h__incl.md5
%{_docdir}/%{name}/html/ip-utils_8h__incl.png
%{_docdir}/%{name}/html/ip-utils_8h_source.html
%{_docdir}/%{name}/html/janus-cfgconv_8c.html
%{_docdir}/%{name}/html/janus-cfgconv_8c__incl.map
%{_docdir}/%{name}/html/janus-cfgconv_8c__incl.md5
%{_docdir}/%{name}/html/janus-cfgconv_8c__incl.png
%{_docdir}/%{name}/html/janus-pp-rec_8c.html
%{_docdir}/%{name}/html/janus-pp-rec_8c__incl.map
%{_docdir}/%{name}/html/janus-pp-rec_8c__incl.md5
%{_docdir}/%{name}/html/janus-pp-rec_8c__incl.png
%{_docdir}/%{name}/html/janus_8c.html
%{_docdir}/%{name}/html/janus_8c__incl.map
%{_docdir}/%{name}/html/janus_8c__incl.md5
%{_docdir}/%{name}/html/janus_8c__incl.png
%{_docdir}/%{name}/html/janus_8h.html
%{_docdir}/%{name}/html/janus_8h__dep__incl.map
%{_docdir}/%{name}/html/janus_8h__dep__incl.md5
%{_docdir}/%{name}/html/janus_8h__dep__incl.png
%{_docdir}/%{name}/html/janus_8h__incl.map
%{_docdir}/%{name}/html/janus_8h__incl.md5
%{_docdir}/%{name}/html/janus_8h__incl.png
%{_docdir}/%{name}/html/janus_8h_source.html
%{_docdir}/%{name}/html/janus__audiobridge_8c.html
%{_docdir}/%{name}/html/janus__audiobridge_8c__incl.map
%{_docdir}/%{name}/html/janus__audiobridge_8c__incl.md5
%{_docdir}/%{name}/html/janus__audiobridge_8c__incl.png
%{_docdir}/%{name}/html/janus__duktape_8c.html
%{_docdir}/%{name}/html/janus__duktape_8c__incl.map
%{_docdir}/%{name}/html/janus__duktape_8c__incl.md5
%{_docdir}/%{name}/html/janus__duktape_8c__incl.png
%{_docdir}/%{name}/html/janus__duktape__data_8h.html
%{_docdir}/%{name}/html/janus__duktape__data_8h__dep__incl.map
%{_docdir}/%{name}/html/janus__duktape__data_8h__dep__incl.md5
%{_docdir}/%{name}/html/janus__duktape__data_8h__dep__incl.png
%{_docdir}/%{name}/html/janus__duktape__data_8h__incl.map
%{_docdir}/%{name}/html/janus__duktape__data_8h__incl.md5
%{_docdir}/%{name}/html/janus__duktape__data_8h__incl.png
%{_docdir}/%{name}/html/janus__duktape__data_8h_source.html
%{_docdir}/%{name}/html/janus__duktape__extra_8c.html
%{_docdir}/%{name}/html/janus__duktape__extra_8c__incl.map
%{_docdir}/%{name}/html/janus__duktape__extra_8c__incl.md5
%{_docdir}/%{name}/html/janus__duktape__extra_8c__incl.png
%{_docdir}/%{name}/html/janus__duktape__extra_8h.html
%{_docdir}/%{name}/html/janus__duktape__extra_8h__dep__incl.map
%{_docdir}/%{name}/html/janus__duktape__extra_8h__dep__incl.md5
%{_docdir}/%{name}/html/janus__duktape__extra_8h__dep__incl.png
%{_docdir}/%{name}/html/janus__duktape__extra_8h__incl.map
%{_docdir}/%{name}/html/janus__duktape__extra_8h__incl.md5
%{_docdir}/%{name}/html/janus__duktape__extra_8h__incl.png
%{_docdir}/%{name}/html/janus__duktape__extra_8h_source.html
%{_docdir}/%{name}/html/janus__echotest_8c.html
%{_docdir}/%{name}/html/janus__echotest_8c__incl.map
%{_docdir}/%{name}/html/janus__echotest_8c__incl.md5
%{_docdir}/%{name}/html/janus__echotest_8c__incl.png
%{_docdir}/%{name}/html/janus__gelfevh_8c.html
%{_docdir}/%{name}/html/janus__gelfevh_8c__incl.map
%{_docdir}/%{name}/html/janus__gelfevh_8c__incl.md5
%{_docdir}/%{name}/html/janus__gelfevh_8c__incl.png
%{_docdir}/%{name}/html/janus__http_8c.html
%{_docdir}/%{name}/html/janus__http_8c__incl.map
%{_docdir}/%{name}/html/janus__http_8c__incl.md5
%{_docdir}/%{name}/html/janus__http_8c__incl.png
%{_docdir}/%{name}/html/janus__jsonlog_8c.html
%{_docdir}/%{name}/html/janus__jsonlog_8c__incl.map
%{_docdir}/%{name}/html/janus__jsonlog_8c__incl.md5
%{_docdir}/%{name}/html/janus__jsonlog_8c__incl.png
%{_docdir}/%{name}/html/janus__lua_8c.html
%{_docdir}/%{name}/html/janus__lua_8c__incl.map
%{_docdir}/%{name}/html/janus__lua_8c__incl.md5
%{_docdir}/%{name}/html/janus__lua_8c__incl.png
%{_docdir}/%{name}/html/janus__lua__data_8h.html
%{_docdir}/%{name}/html/janus__lua__data_8h__dep__incl.map
%{_docdir}/%{name}/html/janus__lua__data_8h__dep__incl.md5
%{_docdir}/%{name}/html/janus__lua__data_8h__dep__incl.png
%{_docdir}/%{name}/html/janus__lua__data_8h__incl.map
%{_docdir}/%{name}/html/janus__lua__data_8h__incl.md5
%{_docdir}/%{name}/html/janus__lua__data_8h__incl.png
%{_docdir}/%{name}/html/janus__lua__data_8h_source.html
%{_docdir}/%{name}/html/janus__lua__extra_8c.html
%{_docdir}/%{name}/html/janus__lua__extra_8c__incl.map
%{_docdir}/%{name}/html/janus__lua__extra_8c__incl.md5
%{_docdir}/%{name}/html/janus__lua__extra_8c__incl.png
%{_docdir}/%{name}/html/janus__lua__extra_8h.html
%{_docdir}/%{name}/html/janus__lua__extra_8h__dep__incl.map
%{_docdir}/%{name}/html/janus__lua__extra_8h__dep__incl.md5
%{_docdir}/%{name}/html/janus__lua__extra_8h__dep__incl.png
%{_docdir}/%{name}/html/janus__lua__extra_8h__incl.map
%{_docdir}/%{name}/html/janus__lua__extra_8h__incl.md5
%{_docdir}/%{name}/html/janus__lua__extra_8h__incl.png
%{_docdir}/%{name}/html/janus__lua__extra_8h_source.html
%{_docdir}/%{name}/html/janus__mqtt_8c.html
%{_docdir}/%{name}/html/janus__mqtt_8c__incl.map
%{_docdir}/%{name}/html/janus__mqtt_8c__incl.md5
%{_docdir}/%{name}/html/janus__mqtt_8c__incl.png
%{_docdir}/%{name}/html/janus__mqttevh_8c.html
%{_docdir}/%{name}/html/janus__mqttevh_8c__incl.map
%{_docdir}/%{name}/html/janus__mqttevh_8c__incl.md5
%{_docdir}/%{name}/html/janus__mqttevh_8c__incl.png
%{_docdir}/%{name}/html/janus__nanomsg_8c.html
%{_docdir}/%{name}/html/janus__nanomsg_8c__incl.map
%{_docdir}/%{name}/html/janus__nanomsg_8c__incl.md5
%{_docdir}/%{name}/html/janus__nanomsg_8c__incl.png
%{_docdir}/%{name}/html/janus__nanomsgevh_8c.html
%{_docdir}/%{name}/html/janus__nanomsgevh_8c__incl.map
%{_docdir}/%{name}/html/janus__nanomsgevh_8c__incl.md5
%{_docdir}/%{name}/html/janus__nanomsgevh_8c__incl.png
%{_docdir}/%{name}/html/janus__nosip_8c.html
%{_docdir}/%{name}/html/janus__nosip_8c__incl.map
%{_docdir}/%{name}/html/janus__nosip_8c__incl.md5
%{_docdir}/%{name}/html/janus__nosip_8c__incl.png
%{_docdir}/%{name}/html/janus__pfunix_8c.html
%{_docdir}/%{name}/html/janus__pfunix_8c__incl.map
%{_docdir}/%{name}/html/janus__pfunix_8c__incl.md5
%{_docdir}/%{name}/html/janus__pfunix_8c__incl.png
%{_docdir}/%{name}/html/janus__rabbitmq_8c.html
%{_docdir}/%{name}/html/janus__rabbitmq_8c__incl.map
%{_docdir}/%{name}/html/janus__rabbitmq_8c__incl.md5
%{_docdir}/%{name}/html/janus__rabbitmq_8c__incl.png
%{_docdir}/%{name}/html/janus__rabbitmqevh_8c.html
%{_docdir}/%{name}/html/janus__rabbitmqevh_8c__incl.map
%{_docdir}/%{name}/html/janus__rabbitmqevh_8c__incl.md5
%{_docdir}/%{name}/html/janus__rabbitmqevh_8c__incl.png
%{_docdir}/%{name}/html/janus__recordplay_8c.html
%{_docdir}/%{name}/html/janus__recordplay_8c__incl.map
%{_docdir}/%{name}/html/janus__recordplay_8c__incl.md5
%{_docdir}/%{name}/html/janus__recordplay_8c__incl.png
%{_docdir}/%{name}/html/janus__sampleevh_8c.html
%{_docdir}/%{name}/html/janus__sampleevh_8c__incl.map
%{_docdir}/%{name}/html/janus__sampleevh_8c__incl.md5
%{_docdir}/%{name}/html/janus__sampleevh_8c__incl.png
%{_docdir}/%{name}/html/janus__sip_8c.html
%{_docdir}/%{name}/html/janus__sip_8c__incl.map
%{_docdir}/%{name}/html/janus__sip_8c__incl.md5
%{_docdir}/%{name}/html/janus__sip_8c__incl.png
%{_docdir}/%{name}/html/janus__streaming_8c.html
%{_docdir}/%{name}/html/janus__streaming_8c__incl.map
%{_docdir}/%{name}/html/janus__streaming_8c__incl.md5
%{_docdir}/%{name}/html/janus__streaming_8c__incl.png
%{_docdir}/%{name}/html/janus__textroom_8c.html
%{_docdir}/%{name}/html/janus__textroom_8c__incl.map
%{_docdir}/%{name}/html/janus__textroom_8c__incl.md5
%{_docdir}/%{name}/html/janus__textroom_8c__incl.png
%{_docdir}/%{name}/html/janus__videocall_8c.html
%{_docdir}/%{name}/html/janus__videocall_8c__incl.map
%{_docdir}/%{name}/html/janus__videocall_8c__incl.md5
%{_docdir}/%{name}/html/janus__videocall_8c__incl.png
%{_docdir}/%{name}/html/janus__videoroom_8c.html
%{_docdir}/%{name}/html/janus__videoroom_8c__incl.map
%{_docdir}/%{name}/html/janus__videoroom_8c__incl.md5
%{_docdir}/%{name}/html/janus__videoroom_8c__incl.png
%{_docdir}/%{name}/html/janus__voicemail_8c.html
%{_docdir}/%{name}/html/janus__voicemail_8c__incl.map
%{_docdir}/%{name}/html/janus__voicemail_8c__incl.md5
%{_docdir}/%{name}/html/janus__voicemail_8c__incl.png
%{_docdir}/%{name}/html/janus__websockets_8c.html
%{_docdir}/%{name}/html/janus__websockets_8c__incl.map
%{_docdir}/%{name}/html/janus__websockets_8c__incl.md5
%{_docdir}/%{name}/html/janus__websockets_8c__incl.png
%{_docdir}/%{name}/html/janus__wsevh_8c.html
%{_docdir}/%{name}/html/janus__wsevh_8c__incl.map
%{_docdir}/%{name}/html/janus__wsevh_8c__incl.md5
%{_docdir}/%{name}/html/janus__wsevh_8c__incl.png
%{_docdir}/%{name}/html/jquery.js
%{_docdir}/%{name}/html/js-dependencies.html
%{_docdir}/%{name}/html/js-modules.html
%{_docdir}/%{name}/html/js/bootstrap-3.4.1.min.js
%{_docdir}/%{name}/html/log_8c.html
%{_docdir}/%{name}/html/log_8c__incl.map
%{_docdir}/%{name}/html/log_8c__incl.md5
%{_docdir}/%{name}/html/log_8c__incl.png
%{_docdir}/%{name}/html/log_8h.html
%{_docdir}/%{name}/html/log_8h__dep__incl.map
%{_docdir}/%{name}/html/log_8h__dep__incl.md5
%{_docdir}/%{name}/html/log_8h__dep__incl.png
%{_docdir}/%{name}/html/log_8h__incl.map
%{_docdir}/%{name}/html/log_8h__incl.md5
%{_docdir}/%{name}/html/log_8h__incl.png
%{_docdir}/%{name}/html/log_8h_source.html
%{_docdir}/%{name}/html/logger_8h.html
%{_docdir}/%{name}/html/logger_8h__dep__incl.map
%{_docdir}/%{name}/html/logger_8h__dep__incl.md5
%{_docdir}/%{name}/html/logger_8h__dep__incl.png
%{_docdir}/%{name}/html/logger_8h__incl.map
%{_docdir}/%{name}/html/logger_8h__incl.md5
%{_docdir}/%{name}/html/logger_8h__incl.png
%{_docdir}/%{name}/html/logger_8h_source.html
%{_docdir}/%{name}/html/lua.html
%{_docdir}/%{name}/html/mach__gettime_8h.html
%{_docdir}/%{name}/html/mach__gettime_8h__incl.map
%{_docdir}/%{name}/html/mach__gettime_8h__incl.md5
%{_docdir}/%{name}/html/mach__gettime_8h__incl.png
%{_docdir}/%{name}/html/mach__gettime_8h_source.html
%{_docdir}/%{name}/html/mainpage_8dox.html
%{_docdir}/%{name}/html/meetecho-logo.png
%{_docdir}/%{name}/html/menudata.js
%{_docdir}/%{name}/html/mjr2pcap_8c.html
%{_docdir}/%{name}/html/mjr2pcap_8c__incl.map
%{_docdir}/%{name}/html/mjr2pcap_8c__incl.md5
%{_docdir}/%{name}/html/mjr2pcap_8c__incl.png
%{_docdir}/%{name}/html/modules.html
%{_docdir}/%{name}/html/mutex_8h.html
%{_docdir}/%{name}/html/mutex_8h__dep__incl.map
%{_docdir}/%{name}/html/mutex_8h__dep__incl.md5
%{_docdir}/%{name}/html/mutex_8h__dep__incl.png
%{_docdir}/%{name}/html/mutex_8h__incl.map
%{_docdir}/%{name}/html/mutex_8h__incl.md5
%{_docdir}/%{name}/html/mutex_8h__incl.png
%{_docdir}/%{name}/html/mutex_8h_source.html
%{_docdir}/%{name}/html/nav_f.png
%{_docdir}/%{name}/html/nav_fd.png
%{_docdir}/%{name}/html/nav_g.png
%{_docdir}/%{name}/html/nav_h.png
%{_docdir}/%{name}/html/nav_hd.png
%{_docdir}/%{name}/html/nosip.html
%{_docdir}/%{name}/html/open.png
%{_docdir}/%{name}/html/options_8c.html
%{_docdir}/%{name}/html/options_8c__incl.map
%{_docdir}/%{name}/html/options_8c__incl.md5
%{_docdir}/%{name}/html/options_8c__incl.png
%{_docdir}/%{name}/html/options_8h.html
%{_docdir}/%{name}/html/options_8h__dep__incl.map
%{_docdir}/%{name}/html/options_8h__dep__incl.md5
%{_docdir}/%{name}/html/options_8h__dep__incl.png
%{_docdir}/%{name}/html/options_8h__incl.map
%{_docdir}/%{name}/html/options_8h__incl.md5
%{_docdir}/%{name}/html/options_8h__incl.png
%{_docdir}/%{name}/html/options_8h_source.html
%{_docdir}/%{name}/html/pages.html
%{_docdir}/%{name}/html/pcap2mjr_8c.html
%{_docdir}/%{name}/html/pcap2mjr_8c__incl.map
%{_docdir}/%{name}/html/pcap2mjr_8c__incl.md5
%{_docdir}/%{name}/html/pcap2mjr_8c__incl.png
%{_docdir}/%{name}/html/plugin_8c.html
%{_docdir}/%{name}/html/plugin_8c__incl.map
%{_docdir}/%{name}/html/plugin_8c__incl.md5
%{_docdir}/%{name}/html/plugin_8c__incl.png
%{_docdir}/%{name}/html/plugin_8h.html
%{_docdir}/%{name}/html/plugin_8h__dep__incl.map
%{_docdir}/%{name}/html/plugin_8h__dep__incl.md5
%{_docdir}/%{name}/html/plugin_8h__dep__incl.png
%{_docdir}/%{name}/html/plugin_8h__incl.map
%{_docdir}/%{name}/html/plugin_8h__incl.md5
%{_docdir}/%{name}/html/plugin_8h__incl.png
%{_docdir}/%{name}/html/plugin_8h_source.html
%{_docdir}/%{name}/html/pluginslist.html
%{_docdir}/%{name}/html/pp-av1_8c.html
%{_docdir}/%{name}/html/pp-av1_8c__incl.map
%{_docdir}/%{name}/html/pp-av1_8c__incl.md5
%{_docdir}/%{name}/html/pp-av1_8c__incl.png
%{_docdir}/%{name}/html/pp-av1_8h.html
%{_docdir}/%{name}/html/pp-av1_8h__dep__incl.map
%{_docdir}/%{name}/html/pp-av1_8h__dep__incl.md5
%{_docdir}/%{name}/html/pp-av1_8h__dep__incl.png
%{_docdir}/%{name}/html/pp-av1_8h__incl.map
%{_docdir}/%{name}/html/pp-av1_8h__incl.md5
%{_docdir}/%{name}/html/pp-av1_8h__incl.png
%{_docdir}/%{name}/html/pp-av1_8h_source.html
%{_docdir}/%{name}/html/pp-avformat_8c.html
%{_docdir}/%{name}/html/pp-avformat_8c__incl.map
%{_docdir}/%{name}/html/pp-avformat_8c__incl.md5
%{_docdir}/%{name}/html/pp-avformat_8c__incl.png
%{_docdir}/%{name}/html/pp-avformat_8h.html
%{_docdir}/%{name}/html/pp-avformat_8h__dep__incl.map
%{_docdir}/%{name}/html/pp-avformat_8h__dep__incl.md5
%{_docdir}/%{name}/html/pp-avformat_8h__dep__incl.png
%{_docdir}/%{name}/html/pp-avformat_8h__incl.map
%{_docdir}/%{name}/html/pp-avformat_8h__incl.md5
%{_docdir}/%{name}/html/pp-avformat_8h__incl.png
%{_docdir}/%{name}/html/pp-avformat_8h_source.html
%{_docdir}/%{name}/html/pp-binary_8c.html
%{_docdir}/%{name}/html/pp-binary_8c__incl.map
%{_docdir}/%{name}/html/pp-binary_8c__incl.md5
%{_docdir}/%{name}/html/pp-binary_8c__incl.png
%{_docdir}/%{name}/html/pp-binary_8h.html
%{_docdir}/%{name}/html/pp-binary_8h__dep__incl.map
%{_docdir}/%{name}/html/pp-binary_8h__dep__incl.md5
%{_docdir}/%{name}/html/pp-binary_8h__dep__incl.png
%{_docdir}/%{name}/html/pp-binary_8h__incl.map
%{_docdir}/%{name}/html/pp-binary_8h__incl.md5
%{_docdir}/%{name}/html/pp-binary_8h__incl.png
%{_docdir}/%{name}/html/pp-binary_8h_source.html
%{_docdir}/%{name}/html/pp-g711_8c.html
%{_docdir}/%{name}/html/pp-g711_8c__incl.map
%{_docdir}/%{name}/html/pp-g711_8c__incl.md5
%{_docdir}/%{name}/html/pp-g711_8c__incl.png
%{_docdir}/%{name}/html/pp-g711_8h.html
%{_docdir}/%{name}/html/pp-g711_8h__dep__incl.map
%{_docdir}/%{name}/html/pp-g711_8h__dep__incl.md5
%{_docdir}/%{name}/html/pp-g711_8h__dep__incl.png
%{_docdir}/%{name}/html/pp-g711_8h__incl.map
%{_docdir}/%{name}/html/pp-g711_8h__incl.md5
%{_docdir}/%{name}/html/pp-g711_8h__incl.png
%{_docdir}/%{name}/html/pp-g711_8h_source.html
%{_docdir}/%{name}/html/pp-g722_8c.html
%{_docdir}/%{name}/html/pp-g722_8c__incl.map
%{_docdir}/%{name}/html/pp-g722_8c__incl.md5
%{_docdir}/%{name}/html/pp-g722_8c__incl.png
%{_docdir}/%{name}/html/pp-g722_8h.html
%{_docdir}/%{name}/html/pp-g722_8h__dep__incl.map
%{_docdir}/%{name}/html/pp-g722_8h__dep__incl.md5
%{_docdir}/%{name}/html/pp-g722_8h__dep__incl.png
%{_docdir}/%{name}/html/pp-g722_8h__incl.map
%{_docdir}/%{name}/html/pp-g722_8h__incl.md5
%{_docdir}/%{name}/html/pp-g722_8h__incl.png
%{_docdir}/%{name}/html/pp-g722_8h_source.html
%{_docdir}/%{name}/html/pp-h264_8c.html
%{_docdir}/%{name}/html/pp-h264_8c__incl.map
%{_docdir}/%{name}/html/pp-h264_8c__incl.md5
%{_docdir}/%{name}/html/pp-h264_8c__incl.png
%{_docdir}/%{name}/html/pp-h264_8h.html
%{_docdir}/%{name}/html/pp-h264_8h__dep__incl.map
%{_docdir}/%{name}/html/pp-h264_8h__dep__incl.md5
%{_docdir}/%{name}/html/pp-h264_8h__dep__incl.png
%{_docdir}/%{name}/html/pp-h264_8h__incl.map
%{_docdir}/%{name}/html/pp-h264_8h__incl.md5
%{_docdir}/%{name}/html/pp-h264_8h__incl.png
%{_docdir}/%{name}/html/pp-h264_8h_source.html
%{_docdir}/%{name}/html/pp-h265_8c.html
%{_docdir}/%{name}/html/pp-h265_8c__incl.map
%{_docdir}/%{name}/html/pp-h265_8c__incl.md5
%{_docdir}/%{name}/html/pp-h265_8c__incl.png
%{_docdir}/%{name}/html/pp-h265_8h.html
%{_docdir}/%{name}/html/pp-h265_8h__dep__incl.map
%{_docdir}/%{name}/html/pp-h265_8h__dep__incl.md5
%{_docdir}/%{name}/html/pp-h265_8h__dep__incl.png
%{_docdir}/%{name}/html/pp-h265_8h__incl.map
%{_docdir}/%{name}/html/pp-h265_8h__incl.md5
%{_docdir}/%{name}/html/pp-h265_8h__incl.png
%{_docdir}/%{name}/html/pp-h265_8h_source.html
%{_docdir}/%{name}/html/pp-options_8c.html
%{_docdir}/%{name}/html/pp-options_8c__incl.map
%{_docdir}/%{name}/html/pp-options_8c__incl.md5
%{_docdir}/%{name}/html/pp-options_8c__incl.png
%{_docdir}/%{name}/html/pp-options_8h.html
%{_docdir}/%{name}/html/pp-options_8h__dep__incl.map
%{_docdir}/%{name}/html/pp-options_8h__dep__incl.md5
%{_docdir}/%{name}/html/pp-options_8h__dep__incl.png
%{_docdir}/%{name}/html/pp-options_8h__incl.map
%{_docdir}/%{name}/html/pp-options_8h__incl.md5
%{_docdir}/%{name}/html/pp-options_8h__incl.png
%{_docdir}/%{name}/html/pp-options_8h_source.html
%{_docdir}/%{name}/html/pp-opus-silence_8h.html
%{_docdir}/%{name}/html/pp-opus-silence_8h__dep__incl.map
%{_docdir}/%{name}/html/pp-opus-silence_8h__dep__incl.md5
%{_docdir}/%{name}/html/pp-opus-silence_8h__dep__incl.png
%{_docdir}/%{name}/html/pp-opus-silence_8h_source.html
%{_docdir}/%{name}/html/pp-opus_8c.html
%{_docdir}/%{name}/html/pp-opus_8c__incl.map
%{_docdir}/%{name}/html/pp-opus_8c__incl.md5
%{_docdir}/%{name}/html/pp-opus_8c__incl.png
%{_docdir}/%{name}/html/pp-opus_8h.html
%{_docdir}/%{name}/html/pp-opus_8h__dep__incl.map
%{_docdir}/%{name}/html/pp-opus_8h__dep__incl.md5
%{_docdir}/%{name}/html/pp-opus_8h__dep__incl.png
%{_docdir}/%{name}/html/pp-opus_8h__incl.map
%{_docdir}/%{name}/html/pp-opus_8h__incl.md5
%{_docdir}/%{name}/html/pp-opus_8h__incl.png
%{_docdir}/%{name}/html/pp-opus_8h_source.html
%{_docdir}/%{name}/html/pp-rtp_8h.html
%{_docdir}/%{name}/html/pp-rtp_8h__dep__incl.map
%{_docdir}/%{name}/html/pp-rtp_8h__dep__incl.md5
%{_docdir}/%{name}/html/pp-rtp_8h__dep__incl.png
%{_docdir}/%{name}/html/pp-rtp_8h__incl.map
%{_docdir}/%{name}/html/pp-rtp_8h__incl.md5
%{_docdir}/%{name}/html/pp-rtp_8h__incl.png
%{_docdir}/%{name}/html/pp-rtp_8h_source.html
%{_docdir}/%{name}/html/pp-srt_8c.html
%{_docdir}/%{name}/html/pp-srt_8c__incl.map
%{_docdir}/%{name}/html/pp-srt_8c__incl.md5
%{_docdir}/%{name}/html/pp-srt_8c__incl.png
%{_docdir}/%{name}/html/pp-srt_8h.html
%{_docdir}/%{name}/html/pp-srt_8h__dep__incl.map
%{_docdir}/%{name}/html/pp-srt_8h__dep__incl.md5
%{_docdir}/%{name}/html/pp-srt_8h__dep__incl.png
%{_docdir}/%{name}/html/pp-srt_8h__incl.map
%{_docdir}/%{name}/html/pp-srt_8h__incl.md5
%{_docdir}/%{name}/html/pp-srt_8h__incl.png
%{_docdir}/%{name}/html/pp-srt_8h_source.html
%{_docdir}/%{name}/html/pp-webm_8c.html
%{_docdir}/%{name}/html/pp-webm_8c__incl.map
%{_docdir}/%{name}/html/pp-webm_8c__incl.md5
%{_docdir}/%{name}/html/pp-webm_8c__incl.png
%{_docdir}/%{name}/html/pp-webm_8h.html
%{_docdir}/%{name}/html/pp-webm_8h__dep__incl.map
%{_docdir}/%{name}/html/pp-webm_8h__dep__incl.md5
%{_docdir}/%{name}/html/pp-webm_8h__dep__incl.png
%{_docdir}/%{name}/html/pp-webm_8h__incl.map
%{_docdir}/%{name}/html/pp-webm_8h__incl.md5
%{_docdir}/%{name}/html/pp-webm_8h__incl.png
%{_docdir}/%{name}/html/pp-webm_8h_source.html
%{_docdir}/%{name}/html/record_8c.html
%{_docdir}/%{name}/html/record_8c__incl.map
%{_docdir}/%{name}/html/record_8c__incl.md5
%{_docdir}/%{name}/html/record_8c__incl.png
%{_docdir}/%{name}/html/record_8h.html
%{_docdir}/%{name}/html/record_8h__dep__incl.map
%{_docdir}/%{name}/html/record_8h__dep__incl.md5
%{_docdir}/%{name}/html/record_8h__dep__incl.png
%{_docdir}/%{name}/html/record_8h__incl.map
%{_docdir}/%{name}/html/record_8h__incl.md5
%{_docdir}/%{name}/html/record_8h__incl.png
%{_docdir}/%{name}/html/record_8h_source.html
%{_docdir}/%{name}/html/recordings.html
%{_docdir}/%{name}/html/recordplay.html
%{_docdir}/%{name}/html/refcount_8h.html
%{_docdir}/%{name}/html/refcount_8h__dep__incl.map
%{_docdir}/%{name}/html/refcount_8h__dep__incl.md5
%{_docdir}/%{name}/html/refcount_8h__dep__incl.png
%{_docdir}/%{name}/html/refcount_8h__incl.map
%{_docdir}/%{name}/html/refcount_8h__incl.md5
%{_docdir}/%{name}/html/refcount_8h__incl.png
%{_docdir}/%{name}/html/refcount_8h_source.html
%{_docdir}/%{name}/html/resources.html
%{_docdir}/%{name}/html/rest.html
%{_docdir}/%{name}/html/rtcp_8c.html
%{_docdir}/%{name}/html/rtcp_8c__incl.map
%{_docdir}/%{name}/html/rtcp_8c__incl.md5
%{_docdir}/%{name}/html/rtcp_8c__incl.png
%{_docdir}/%{name}/html/rtcp_8h.html
%{_docdir}/%{name}/html/rtcp_8h__dep__incl.map
%{_docdir}/%{name}/html/rtcp_8h__dep__incl.md5
%{_docdir}/%{name}/html/rtcp_8h__dep__incl.png
%{_docdir}/%{name}/html/rtcp_8h__incl.map
%{_docdir}/%{name}/html/rtcp_8h__incl.md5
%{_docdir}/%{name}/html/rtcp_8h__incl.png
%{_docdir}/%{name}/html/rtcp_8h_source.html
%{_docdir}/%{name}/html/rtp_8c.html
%{_docdir}/%{name}/html/rtp_8c__incl.map
%{_docdir}/%{name}/html/rtp_8c__incl.md5
%{_docdir}/%{name}/html/rtp_8c__incl.png
%{_docdir}/%{name}/html/rtp_8h.html
%{_docdir}/%{name}/html/rtp_8h__dep__incl.map
%{_docdir}/%{name}/html/rtp_8h__dep__incl.md5
%{_docdir}/%{name}/html/rtp_8h__dep__incl.png
%{_docdir}/%{name}/html/rtp_8h__incl.map
%{_docdir}/%{name}/html/rtp_8h__incl.md5
%{_docdir}/%{name}/html/rtp_8h__incl.png
%{_docdir}/%{name}/html/rtp_8h_source.html
%{_docdir}/%{name}/html/rtpsrtp_8h.html
%{_docdir}/%{name}/html/rtpsrtp_8h__dep__incl.map
%{_docdir}/%{name}/html/rtpsrtp_8h__dep__incl.md5
%{_docdir}/%{name}/html/rtpsrtp_8h__dep__incl.png
%{_docdir}/%{name}/html/rtpsrtp_8h__incl.map
%{_docdir}/%{name}/html/rtpsrtp_8h__incl.md5
%{_docdir}/%{name}/html/rtpsrtp_8h__incl.png
%{_docdir}/%{name}/html/rtpsrtp_8h_source.html
%{_docdir}/%{name}/html/sctp_8c.html
%{_docdir}/%{name}/html/sctp_8h.html
%{_docdir}/%{name}/html/sctp_8h__dep__incl.map
%{_docdir}/%{name}/html/sctp_8h__dep__incl.md5
%{_docdir}/%{name}/html/sctp_8h__dep__incl.png
%{_docdir}/%{name}/html/sctp_8h_source.html
%{_docdir}/%{name}/html/sdp-utils_8c.html
%{_docdir}/%{name}/html/sdp-utils_8c__incl.map
%{_docdir}/%{name}/html/sdp-utils_8c__incl.md5
%{_docdir}/%{name}/html/sdp-utils_8c__incl.png
%{_docdir}/%{name}/html/sdp-utils_8h.html
%{_docdir}/%{name}/html/sdp-utils_8h__dep__incl.map
%{_docdir}/%{name}/html/sdp-utils_8h__dep__incl.md5
%{_docdir}/%{name}/html/sdp-utils_8h__dep__incl.png
%{_docdir}/%{name}/html/sdp-utils_8h__incl.map
%{_docdir}/%{name}/html/sdp-utils_8h__incl.md5
%{_docdir}/%{name}/html/sdp-utils_8h__incl.png
%{_docdir}/%{name}/html/sdp-utils_8h_source.html
%{_docdir}/%{name}/html/sdp_8c.html
%{_docdir}/%{name}/html/sdp_8c__incl.map
%{_docdir}/%{name}/html/sdp_8c__incl.md5
%{_docdir}/%{name}/html/sdp_8c__incl.png
%{_docdir}/%{name}/html/sdp_8h.html
%{_docdir}/%{name}/html/sdp_8h__dep__incl.map
%{_docdir}/%{name}/html/sdp_8h__dep__incl.md5
%{_docdir}/%{name}/html/sdp_8h__dep__incl.png
%{_docdir}/%{name}/html/sdp_8h__incl.map
%{_docdir}/%{name}/html/sdp_8h__incl.md5
%{_docdir}/%{name}/html/sdp_8h__incl.png
%{_docdir}/%{name}/html/sdp_8h_source.html
%{_docdir}/%{name}/html/search/all_0.js
%{_docdir}/%{name}/html/search/all_1.js
%{_docdir}/%{name}/html/search/all_10.js
%{_docdir}/%{name}/html/search/all_11.js
%{_docdir}/%{name}/html/search/all_12.js
%{_docdir}/%{name}/html/search/all_13.js
%{_docdir}/%{name}/html/search/all_14.js
%{_docdir}/%{name}/html/search/all_15.js
%{_docdir}/%{name}/html/search/all_16.js
%{_docdir}/%{name}/html/search/all_2.js
%{_docdir}/%{name}/html/search/all_3.js
%{_docdir}/%{name}/html/search/all_4.js
%{_docdir}/%{name}/html/search/all_5.js
%{_docdir}/%{name}/html/search/all_6.js
%{_docdir}/%{name}/html/search/all_7.js
%{_docdir}/%{name}/html/search/all_8.js
%{_docdir}/%{name}/html/search/all_9.js
%{_docdir}/%{name}/html/search/all_a.js
%{_docdir}/%{name}/html/search/all_b.js
%{_docdir}/%{name}/html/search/all_c.js
%{_docdir}/%{name}/html/search/all_d.js
%{_docdir}/%{name}/html/search/all_e.js
%{_docdir}/%{name}/html/search/all_f.js
%{_docdir}/%{name}/html/search/classes_0.js
%{_docdir}/%{name}/html/search/classes_1.js
%{_docdir}/%{name}/html/search/classes_2.js
%{_docdir}/%{name}/html/search/classes_3.js
%{_docdir}/%{name}/html/search/classes_4.js
%{_docdir}/%{name}/html/search/classes_5.js
%{_docdir}/%{name}/html/search/classes_6.js
%{_docdir}/%{name}/html/search/close.svg
%{_docdir}/%{name}/html/search/defines_0.js
%{_docdir}/%{name}/html/search/defines_1.js
%{_docdir}/%{name}/html/search/defines_10.js
%{_docdir}/%{name}/html/search/defines_11.js
%{_docdir}/%{name}/html/search/defines_12.js
%{_docdir}/%{name}/html/search/defines_2.js
%{_docdir}/%{name}/html/search/defines_3.js
%{_docdir}/%{name}/html/search/defines_4.js
%{_docdir}/%{name}/html/search/defines_5.js
%{_docdir}/%{name}/html/search/defines_6.js
%{_docdir}/%{name}/html/search/defines_7.js
%{_docdir}/%{name}/html/search/defines_8.js
%{_docdir}/%{name}/html/search/defines_9.js
%{_docdir}/%{name}/html/search/defines_a.js
%{_docdir}/%{name}/html/search/defines_b.js
%{_docdir}/%{name}/html/search/defines_c.js
%{_docdir}/%{name}/html/search/defines_d.js
%{_docdir}/%{name}/html/search/defines_e.js
%{_docdir}/%{name}/html/search/defines_f.js
%{_docdir}/%{name}/html/search/enums_0.js
%{_docdir}/%{name}/html/search/enums_1.js
%{_docdir}/%{name}/html/search/enumvalues_0.js
%{_docdir}/%{name}/html/search/enumvalues_1.js
%{_docdir}/%{name}/html/search/enumvalues_2.js
%{_docdir}/%{name}/html/search/files_0.js
%{_docdir}/%{name}/html/search/files_1.js
%{_docdir}/%{name}/html/search/files_2.js
%{_docdir}/%{name}/html/search/files_3.js
%{_docdir}/%{name}/html/search/files_4.js
%{_docdir}/%{name}/html/search/files_5.js
%{_docdir}/%{name}/html/search/files_6.js
%{_docdir}/%{name}/html/search/files_7.js
%{_docdir}/%{name}/html/search/files_8.js
%{_docdir}/%{name}/html/search/files_9.js
%{_docdir}/%{name}/html/search/files_a.js
%{_docdir}/%{name}/html/search/files_b.js
%{_docdir}/%{name}/html/search/files_c.js
%{_docdir}/%{name}/html/search/files_d.js
%{_docdir}/%{name}/html/search/files_e.js
%{_docdir}/%{name}/html/search/functions_0.js
%{_docdir}/%{name}/html/search/functions_1.js
%{_docdir}/%{name}/html/search/functions_2.js
%{_docdir}/%{name}/html/search/functions_3.js
%{_docdir}/%{name}/html/search/functions_4.js
%{_docdir}/%{name}/html/search/functions_5.js
%{_docdir}/%{name}/html/search/groups_0.js
%{_docdir}/%{name}/html/search/groups_1.js
%{_docdir}/%{name}/html/search/groups_2.js
%{_docdir}/%{name}/html/search/groups_3.js
%{_docdir}/%{name}/html/search/groups_4.js
%{_docdir}/%{name}/html/search/groups_5.js
%{_docdir}/%{name}/html/search/groups_6.js
%{_docdir}/%{name}/html/search/mag.svg
%{_docdir}/%{name}/html/search/mag_d.svg
%{_docdir}/%{name}/html/search/mag_sel.svg
%{_docdir}/%{name}/html/search/mag_seld.svg
%{_docdir}/%{name}/html/search/pages_0.js
%{_docdir}/%{name}/html/search/pages_1.js
%{_docdir}/%{name}/html/search/pages_2.js
%{_docdir}/%{name}/html/search/pages_3.js
%{_docdir}/%{name}/html/search/pages_4.js
%{_docdir}/%{name}/html/search/pages_5.js
%{_docdir}/%{name}/html/search/pages_6.js
%{_docdir}/%{name}/html/search/pages_7.js
%{_docdir}/%{name}/html/search/pages_8.js
%{_docdir}/%{name}/html/search/pages_9.js
%{_docdir}/%{name}/html/search/pages_a.js
%{_docdir}/%{name}/html/search/pages_b.js
%{_docdir}/%{name}/html/search/pages_c.js
%{_docdir}/%{name}/html/search/pages_d.js
%{_docdir}/%{name}/html/search/pages_e.js
%{_docdir}/%{name}/html/search/search.css
%{_docdir}/%{name}/html/search/search.js
%{_docdir}/%{name}/html/search/searchdata.js
%{_docdir}/%{name}/html/search/typedefs_0.js
%{_docdir}/%{name}/html/search/typedefs_1.js
%{_docdir}/%{name}/html/search/typedefs_2.js
%{_docdir}/%{name}/html/search/typedefs_3.js
%{_docdir}/%{name}/html/search/typedefs_4.js
%{_docdir}/%{name}/html/search/typedefs_5.js
%{_docdir}/%{name}/html/search/typedefs_6.js
%{_docdir}/%{name}/html/search/typedefs_7.js
%{_docdir}/%{name}/html/search/variables_0.js
%{_docdir}/%{name}/html/search/variables_1.js
%{_docdir}/%{name}/html/search/variables_10.js
%{_docdir}/%{name}/html/search/variables_11.js
%{_docdir}/%{name}/html/search/variables_12.js
%{_docdir}/%{name}/html/search/variables_13.js
%{_docdir}/%{name}/html/search/variables_14.js
%{_docdir}/%{name}/html/search/variables_15.js
%{_docdir}/%{name}/html/search/variables_16.js
%{_docdir}/%{name}/html/search/variables_2.js
%{_docdir}/%{name}/html/search/variables_3.js
%{_docdir}/%{name}/html/search/variables_4.js
%{_docdir}/%{name}/html/search/variables_5.js
%{_docdir}/%{name}/html/search/variables_6.js
%{_docdir}/%{name}/html/search/variables_7.js
%{_docdir}/%{name}/html/search/variables_8.js
%{_docdir}/%{name}/html/search/variables_9.js
%{_docdir}/%{name}/html/search/variables_a.js
%{_docdir}/%{name}/html/search/variables_b.js
%{_docdir}/%{name}/html/search/variables_c.js
%{_docdir}/%{name}/html/search/variables_d.js
%{_docdir}/%{name}/html/search/variables_e.js
%{_docdir}/%{name}/html/search/variables_f.js
%{_docdir}/%{name}/html/service.html
%{_docdir}/%{name}/html/sip.html
%{_docdir}/%{name}/html/splitbar.png
%{_docdir}/%{name}/html/splitbard.png
%{_docdir}/%{name}/html/streaming.html
%{_docdir}/%{name}/html/structextended__report__block.html
%{_docdir}/%{name}/html/structjanus__audiobridge__message.html
%{_docdir}/%{name}/html/structjanus__audiobridge__message__coll__graph.map
%{_docdir}/%{name}/html/structjanus__audiobridge__message__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__audiobridge__message__coll__graph.png
%{_docdir}/%{name}/html/structjanus__audiobridge__participant.html
%{_docdir}/%{name}/html/structjanus__audiobridge__participant__coll__graph.map
%{_docdir}/%{name}/html/structjanus__audiobridge__participant__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__audiobridge__participant__coll__graph.png
%{_docdir}/%{name}/html/structjanus__audiobridge__plainrtp__media.html
%{_docdir}/%{name}/html/structjanus__audiobridge__plainrtp__media__coll__graph.map
%{_docdir}/%{name}/html/structjanus__audiobridge__plainrtp__media__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__audiobridge__plainrtp__media__coll__graph.png
%{_docdir}/%{name}/html/structjanus__audiobridge__room.html
%{_docdir}/%{name}/html/structjanus__audiobridge__room__coll__graph.map
%{_docdir}/%{name}/html/structjanus__audiobridge__room__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__audiobridge__room__coll__graph.png
%{_docdir}/%{name}/html/structjanus__audiobridge__rtp__forwarder.html
%{_docdir}/%{name}/html/structjanus__audiobridge__rtp__forwarder__coll__graph.map
%{_docdir}/%{name}/html/structjanus__audiobridge__rtp__forwarder__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__audiobridge__rtp__forwarder__coll__graph.png
%{_docdir}/%{name}/html/structjanus__audiobridge__rtp__relay__packet.html
%{_docdir}/%{name}/html/structjanus__audiobridge__rtp__relay__packet__coll__graph.map
%{_docdir}/%{name}/html/structjanus__audiobridge__rtp__relay__packet__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__audiobridge__rtp__relay__packet__coll__graph.png
%{_docdir}/%{name}/html/structjanus__audiobridge__session.html
%{_docdir}/%{name}/html/structjanus__audiobridge__session__coll__graph.map
%{_docdir}/%{name}/html/structjanus__audiobridge__session__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__audiobridge__session__coll__graph.png
%{_docdir}/%{name}/html/structjanus__av1__svc__context.html
%{_docdir}/%{name}/html/structjanus__av1__svc__template.html
%{_docdir}/%{name}/html/structjanus__callbacks.html
%{_docdir}/%{name}/html/structjanus__config.html
%{_docdir}/%{name}/html/structjanus__config__container.html
%{_docdir}/%{name}/html/structjanus__dtls__srtp.html
%{_docdir}/%{name}/html/structjanus__dtls__srtp__coll__graph.map
%{_docdir}/%{name}/html/structjanus__dtls__srtp__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__dtls__srtp__coll__graph.png
%{_docdir}/%{name}/html/structjanus__duktape__async__event.html
%{_docdir}/%{name}/html/structjanus__duktape__async__event__coll__graph.map
%{_docdir}/%{name}/html/structjanus__duktape__async__event__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__duktape__async__event__coll__graph.png
%{_docdir}/%{name}/html/structjanus__duktape__callback.html
%{_docdir}/%{name}/html/structjanus__duktape__rtp__relay__packet.html
%{_docdir}/%{name}/html/structjanus__duktape__rtp__relay__packet__coll__graph.map
%{_docdir}/%{name}/html/structjanus__duktape__rtp__relay__packet__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__duktape__rtp__relay__packet__coll__graph.png
%{_docdir}/%{name}/html/structjanus__duktape__session.html
%{_docdir}/%{name}/html/structjanus__duktape__session__coll__graph.map
%{_docdir}/%{name}/html/structjanus__duktape__session__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__duktape__session__coll__graph.png
%{_docdir}/%{name}/html/structjanus__echotest__message.html
%{_docdir}/%{name}/html/structjanus__echotest__message__coll__graph.map
%{_docdir}/%{name}/html/structjanus__echotest__message__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__echotest__message__coll__graph.png
%{_docdir}/%{name}/html/structjanus__echotest__session.html
%{_docdir}/%{name}/html/structjanus__echotest__session__coll__graph.map
%{_docdir}/%{name}/html/structjanus__echotest__session__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__echotest__session__coll__graph.png
%{_docdir}/%{name}/html/structjanus__eventhandler.html
%{_docdir}/%{name}/html/structjanus__http__msg.html
%{_docdir}/%{name}/html/structjanus__http__msg__coll__graph.map
%{_docdir}/%{name}/html/structjanus__http__msg__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__http__msg__coll__graph.png
%{_docdir}/%{name}/html/structjanus__http__request__timeout.html
%{_docdir}/%{name}/html/structjanus__http__request__timeout__coll__graph.map
%{_docdir}/%{name}/html/structjanus__http__request__timeout__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__http__request__timeout__coll__graph.png
%{_docdir}/%{name}/html/structjanus__http__session.html
%{_docdir}/%{name}/html/structjanus__http__session__coll__graph.map
%{_docdir}/%{name}/html/structjanus__http__session__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__http__session__coll__graph.png
%{_docdir}/%{name}/html/structjanus__ice__handle.html
%{_docdir}/%{name}/html/structjanus__ice__handle__coll__graph.map
%{_docdir}/%{name}/html/structjanus__ice__handle__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__ice__handle__coll__graph.png
%{_docdir}/%{name}/html/structjanus__ice__nacked__packet.html
%{_docdir}/%{name}/html/structjanus__ice__nacked__packet__coll__graph.map
%{_docdir}/%{name}/html/structjanus__ice__nacked__packet__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__ice__nacked__packet__coll__graph.png
%{_docdir}/%{name}/html/structjanus__ice__outgoing__traffic.html
%{_docdir}/%{name}/html/structjanus__ice__outgoing__traffic__coll__graph.map
%{_docdir}/%{name}/html/structjanus__ice__outgoing__traffic__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__ice__outgoing__traffic__coll__graph.png
%{_docdir}/%{name}/html/structjanus__ice__peerconnection.html
%{_docdir}/%{name}/html/structjanus__ice__peerconnection__coll__graph.map
%{_docdir}/%{name}/html/structjanus__ice__peerconnection__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__ice__peerconnection__coll__graph.png
%{_docdir}/%{name}/html/structjanus__ice__peerconnection__medium.html
%{_docdir}/%{name}/html/structjanus__ice__peerconnection__medium__coll__graph.map
%{_docdir}/%{name}/html/structjanus__ice__peerconnection__medium__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__ice__peerconnection__medium__coll__graph.png
%{_docdir}/%{name}/html/structjanus__ice__queued__packet.html
%{_docdir}/%{name}/html/structjanus__ice__queued__packet__coll__graph.map
%{_docdir}/%{name}/html/structjanus__ice__queued__packet__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__ice__queued__packet__coll__graph.png
%{_docdir}/%{name}/html/structjanus__ice__static__event__loop.html
%{_docdir}/%{name}/html/structjanus__ice__static__event__loop__coll__graph.map
%{_docdir}/%{name}/html/structjanus__ice__static__event__loop__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__ice__static__event__loop__coll__graph.png
%{_docdir}/%{name}/html/structjanus__ice__stats.html
%{_docdir}/%{name}/html/structjanus__ice__stats__coll__graph.map
%{_docdir}/%{name}/html/structjanus__ice__stats__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__ice__stats__coll__graph.png
%{_docdir}/%{name}/html/structjanus__ice__stats__info.html
%{_docdir}/%{name}/html/structjanus__ice__trickle.html
%{_docdir}/%{name}/html/structjanus__ice__trickle__coll__graph.map
%{_docdir}/%{name}/html/structjanus__ice__trickle__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__ice__trickle__coll__graph.png
%{_docdir}/%{name}/html/structjanus__json__parameter.html
%{_docdir}/%{name}/html/structjanus__jsonlog__line.html
%{_docdir}/%{name}/html/structjanus__log__buffer.html
%{_docdir}/%{name}/html/structjanus__log__buffer__coll__graph.map
%{_docdir}/%{name}/html/structjanus__log__buffer__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__log__buffer__coll__graph.png
%{_docdir}/%{name}/html/structjanus__logger.html
%{_docdir}/%{name}/html/structjanus__lua__async__event.html
%{_docdir}/%{name}/html/structjanus__lua__async__event__coll__graph.map
%{_docdir}/%{name}/html/structjanus__lua__async__event__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__lua__async__event__coll__graph.png
%{_docdir}/%{name}/html/structjanus__lua__callback.html
%{_docdir}/%{name}/html/structjanus__lua__rtp__relay__packet.html
%{_docdir}/%{name}/html/structjanus__lua__rtp__relay__packet__coll__graph.map
%{_docdir}/%{name}/html/structjanus__lua__rtp__relay__packet__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__lua__rtp__relay__packet__coll__graph.png
%{_docdir}/%{name}/html/structjanus__lua__session.html
%{_docdir}/%{name}/html/structjanus__lua__session__coll__graph.map
%{_docdir}/%{name}/html/structjanus__lua__session__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__lua__session__coll__graph.png
%{_docdir}/%{name}/html/structjanus__mqtt__context.html
%{_docdir}/%{name}/html/structjanus__mqtt__context__coll__graph.map
%{_docdir}/%{name}/html/structjanus__mqtt__context__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__mqtt__context__coll__graph.png
%{_docdir}/%{name}/html/structjanus__mqttevh__context.html
%{_docdir}/%{name}/html/structjanus__nack.html
%{_docdir}/%{name}/html/structjanus__nack__coll__graph.map
%{_docdir}/%{name}/html/structjanus__nack__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__nack__coll__graph.png
%{_docdir}/%{name}/html/structjanus__nanomsg__client.html
%{_docdir}/%{name}/html/structjanus__nanomsg__client__coll__graph.map
%{_docdir}/%{name}/html/structjanus__nanomsg__client__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__nanomsg__client__coll__graph.png
%{_docdir}/%{name}/html/structjanus__network__address.html
%{_docdir}/%{name}/html/structjanus__network__address__string__buffer.html
%{_docdir}/%{name}/html/structjanus__network__query__config.html
%{_docdir}/%{name}/html/structjanus__nosip__media.html
%{_docdir}/%{name}/html/structjanus__nosip__media__coll__graph.map
%{_docdir}/%{name}/html/structjanus__nosip__media__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__nosip__media__coll__graph.png
%{_docdir}/%{name}/html/structjanus__nosip__message.html
%{_docdir}/%{name}/html/structjanus__nosip__message__coll__graph.map
%{_docdir}/%{name}/html/structjanus__nosip__message__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__nosip__message__coll__graph.png
%{_docdir}/%{name}/html/structjanus__nosip__session.html
%{_docdir}/%{name}/html/structjanus__nosip__session__coll__graph.map
%{_docdir}/%{name}/html/structjanus__nosip__session__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__nosip__session__coll__graph.png
%{_docdir}/%{name}/html/structjanus__options.html
%{_docdir}/%{name}/html/structjanus__pfunix__client.html
%{_docdir}/%{name}/html/structjanus__pfunix__client__coll__graph.map
%{_docdir}/%{name}/html/structjanus__pfunix__client__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__pfunix__client__coll__graph.png
%{_docdir}/%{name}/html/structjanus__plugin.html
%{_docdir}/%{name}/html/structjanus__plugin__coll__graph.map
%{_docdir}/%{name}/html/structjanus__plugin__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__plugin__coll__graph.png
%{_docdir}/%{name}/html/structjanus__plugin__data.html
%{_docdir}/%{name}/html/structjanus__plugin__result.html
%{_docdir}/%{name}/html/structjanus__plugin__rtcp.html
%{_docdir}/%{name}/html/structjanus__plugin__rtp.html
%{_docdir}/%{name}/html/structjanus__plugin__rtp__coll__graph.map
%{_docdir}/%{name}/html/structjanus__plugin__rtp__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__plugin__rtp__coll__graph.png
%{_docdir}/%{name}/html/structjanus__plugin__rtp__extensions.html
%{_docdir}/%{name}/html/structjanus__plugin__session.html
%{_docdir}/%{name}/html/structjanus__plugin__session__coll__graph.map
%{_docdir}/%{name}/html/structjanus__plugin__session__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__plugin__session__coll__graph.png
%{_docdir}/%{name}/html/structjanus__pp__frame__packet.html
%{_docdir}/%{name}/html/structjanus__pp__frame__packet__coll__graph.map
%{_docdir}/%{name}/html/structjanus__pp__frame__packet__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__pp__frame__packet__coll__graph.png
%{_docdir}/%{name}/html/structjanus__pp__g711__wav.html
%{_docdir}/%{name}/html/structjanus__pp__g722__wav.html
%{_docdir}/%{name}/html/structjanus__pp__rtp__header.html
%{_docdir}/%{name}/html/structjanus__pp__rtp__header__extension.html
%{_docdir}/%{name}/html/structjanus__pp__rtp__skew__context.html
%{_docdir}/%{name}/html/structjanus__pprec__options.html
%{_docdir}/%{name}/html/structjanus__rabbitmq__client.html
%{_docdir}/%{name}/html/structjanus__rabbitmq__response.html
%{_docdir}/%{name}/html/structjanus__recorder.html
%{_docdir}/%{name}/html/structjanus__recorder__coll__graph.map
%{_docdir}/%{name}/html/structjanus__recorder__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__recorder__coll__graph.png
%{_docdir}/%{name}/html/structjanus__recordplay__frame__packet.html
%{_docdir}/%{name}/html/structjanus__recordplay__frame__packet__coll__graph.map
%{_docdir}/%{name}/html/structjanus__recordplay__frame__packet__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__recordplay__frame__packet__coll__graph.png
%{_docdir}/%{name}/html/structjanus__recordplay__message.html
%{_docdir}/%{name}/html/structjanus__recordplay__message__coll__graph.map
%{_docdir}/%{name}/html/structjanus__recordplay__message__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__recordplay__message__coll__graph.png
%{_docdir}/%{name}/html/structjanus__recordplay__recording.html
%{_docdir}/%{name}/html/structjanus__recordplay__recording__coll__graph.map
%{_docdir}/%{name}/html/structjanus__recordplay__recording__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__recordplay__recording__coll__graph.png
%{_docdir}/%{name}/html/structjanus__recordplay__rtp__header__extension.html
%{_docdir}/%{name}/html/structjanus__recordplay__session.html
%{_docdir}/%{name}/html/structjanus__recordplay__session__coll__graph.map
%{_docdir}/%{name}/html/structjanus__recordplay__session__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__recordplay__session__coll__graph.png
%{_docdir}/%{name}/html/structjanus__red__block.html
%{_docdir}/%{name}/html/structjanus__refcount.html
%{_docdir}/%{name}/html/structjanus__request.html
%{_docdir}/%{name}/html/structjanus__request__coll__graph.map
%{_docdir}/%{name}/html/structjanus__request__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__request__coll__graph.png
%{_docdir}/%{name}/html/structjanus__rtp__header__extension.html
%{_docdir}/%{name}/html/structjanus__rtp__packet.html
%{_docdir}/%{name}/html/structjanus__rtp__packet__coll__graph.map
%{_docdir}/%{name}/html/structjanus__rtp__packet__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__rtp__packet__coll__graph.png
%{_docdir}/%{name}/html/structjanus__rtp__simulcasting__context.html
%{_docdir}/%{name}/html/structjanus__rtp__switching__context.html
%{_docdir}/%{name}/html/structjanus__sdp.html
%{_docdir}/%{name}/html/structjanus__sdp__attribute.html
%{_docdir}/%{name}/html/structjanus__sdp__attribute__coll__graph.map
%{_docdir}/%{name}/html/structjanus__sdp__attribute__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__sdp__attribute__coll__graph.png
%{_docdir}/%{name}/html/structjanus__sdp__coll__graph.map
%{_docdir}/%{name}/html/structjanus__sdp__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__sdp__coll__graph.png
%{_docdir}/%{name}/html/structjanus__sdp__mdns__candidate.html
%{_docdir}/%{name}/html/structjanus__sdp__mdns__candidate__coll__graph.map
%{_docdir}/%{name}/html/structjanus__sdp__mdns__candidate__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__sdp__mdns__candidate__coll__graph.png
%{_docdir}/%{name}/html/structjanus__sdp__mline.html
%{_docdir}/%{name}/html/structjanus__sdp__mline__coll__graph.map
%{_docdir}/%{name}/html/structjanus__sdp__mline__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__sdp__mline__coll__graph.png
%{_docdir}/%{name}/html/structjanus__seq__info.html
%{_docdir}/%{name}/html/structjanus__seq__info__coll__graph.map
%{_docdir}/%{name}/html/structjanus__seq__info__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__seq__info__coll__graph.png
%{_docdir}/%{name}/html/structjanus__session.html
%{_docdir}/%{name}/html/structjanus__session__coll__graph.map
%{_docdir}/%{name}/html/structjanus__session__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__session__coll__graph.png
%{_docdir}/%{name}/html/structjanus__sip__account.html
%{_docdir}/%{name}/html/structjanus__sip__media.html
%{_docdir}/%{name}/html/structjanus__sip__media__coll__graph.map
%{_docdir}/%{name}/html/structjanus__sip__media__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__sip__media__coll__graph.png
%{_docdir}/%{name}/html/structjanus__sip__message.html
%{_docdir}/%{name}/html/structjanus__sip__message__coll__graph.map
%{_docdir}/%{name}/html/structjanus__sip__message__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__sip__message__coll__graph.png
%{_docdir}/%{name}/html/structjanus__sip__session.html
%{_docdir}/%{name}/html/structjanus__sip__session__coll__graph.map
%{_docdir}/%{name}/html/structjanus__sip__session__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__sip__session__coll__graph.png
%{_docdir}/%{name}/html/structjanus__sip__transfer.html
%{_docdir}/%{name}/html/structjanus__sip__transfer__coll__graph.map
%{_docdir}/%{name}/html/structjanus__sip__transfer__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__sip__transfer__coll__graph.png
%{_docdir}/%{name}/html/structjanus__sip__uri__t.html
%{_docdir}/%{name}/html/structjanus__streaming__codecs.html
%{_docdir}/%{name}/html/structjanus__streaming__file__source.html
%{_docdir}/%{name}/html/structjanus__streaming__file__source__coll__graph.map
%{_docdir}/%{name}/html/structjanus__streaming__file__source__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__streaming__file__source__coll__graph.png
%{_docdir}/%{name}/html/structjanus__streaming__helper.html
%{_docdir}/%{name}/html/structjanus__streaming__helper__coll__graph.map
%{_docdir}/%{name}/html/structjanus__streaming__helper__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__streaming__helper__coll__graph.png
%{_docdir}/%{name}/html/structjanus__streaming__message.html
%{_docdir}/%{name}/html/structjanus__streaming__message__coll__graph.map
%{_docdir}/%{name}/html/structjanus__streaming__message__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__streaming__message__coll__graph.png
%{_docdir}/%{name}/html/structjanus__streaming__mountpoint.html
%{_docdir}/%{name}/html/structjanus__streaming__mountpoint__coll__graph.map
%{_docdir}/%{name}/html/structjanus__streaming__mountpoint__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__streaming__mountpoint__coll__graph.png
%{_docdir}/%{name}/html/structjanus__streaming__rtp__keyframe.html
%{_docdir}/%{name}/html/structjanus__streaming__rtp__relay__packet.html
%{_docdir}/%{name}/html/structjanus__streaming__rtp__relay__packet__coll__graph.map
%{_docdir}/%{name}/html/structjanus__streaming__rtp__relay__packet__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__streaming__rtp__relay__packet__coll__graph.png
%{_docdir}/%{name}/html/structjanus__streaming__rtp__source.html
%{_docdir}/%{name}/html/structjanus__streaming__rtp__source__stream.html
%{_docdir}/%{name}/html/structjanus__streaming__rtp__source__stream__coll__graph.map
%{_docdir}/%{name}/html/structjanus__streaming__rtp__source__stream__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__streaming__rtp__source__stream__coll__graph.png
%{_docdir}/%{name}/html/structjanus__streaming__session.html
%{_docdir}/%{name}/html/structjanus__streaming__session__coll__graph.map
%{_docdir}/%{name}/html/structjanus__streaming__session__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__streaming__session__coll__graph.png
%{_docdir}/%{name}/html/structjanus__streaming__session__stream.html
%{_docdir}/%{name}/html/structjanus__streaming__session__stream__coll__graph.map
%{_docdir}/%{name}/html/structjanus__streaming__session__stream__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__streaming__session__stream__coll__graph.png
%{_docdir}/%{name}/html/structjanus__text2pcap.html
%{_docdir}/%{name}/html/structjanus__text2pcap__ethernet__header.html
%{_docdir}/%{name}/html/structjanus__text2pcap__global__header.html
%{_docdir}/%{name}/html/structjanus__text2pcap__ip__header.html
%{_docdir}/%{name}/html/structjanus__text2pcap__packet__header.html
%{_docdir}/%{name}/html/structjanus__text2pcap__udp__header.html
%{_docdir}/%{name}/html/structjanus__textroom__message.html
%{_docdir}/%{name}/html/structjanus__textroom__message__coll__graph.map
%{_docdir}/%{name}/html/structjanus__textroom__message__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__textroom__message__coll__graph.png
%{_docdir}/%{name}/html/structjanus__textroom__participant.html
%{_docdir}/%{name}/html/structjanus__textroom__participant__coll__graph.map
%{_docdir}/%{name}/html/structjanus__textroom__participant__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__textroom__participant__coll__graph.png
%{_docdir}/%{name}/html/structjanus__textroom__room.html
%{_docdir}/%{name}/html/structjanus__textroom__room__coll__graph.map
%{_docdir}/%{name}/html/structjanus__textroom__room__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__textroom__room__coll__graph.png
%{_docdir}/%{name}/html/structjanus__textroom__session.html
%{_docdir}/%{name}/html/structjanus__textroom__session__coll__graph.map
%{_docdir}/%{name}/html/structjanus__textroom__session__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__textroom__session__coll__graph.png
%{_docdir}/%{name}/html/structjanus__transport.html
%{_docdir}/%{name}/html/structjanus__transport__callbacks.html
%{_docdir}/%{name}/html/structjanus__transport__session.html
%{_docdir}/%{name}/html/structjanus__transport__session__coll__graph.map
%{_docdir}/%{name}/html/structjanus__transport__session__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__transport__session__coll__graph.png
%{_docdir}/%{name}/html/structjanus__videocall__message.html
%{_docdir}/%{name}/html/structjanus__videocall__message__coll__graph.map
%{_docdir}/%{name}/html/structjanus__videocall__message__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__videocall__message__coll__graph.png
%{_docdir}/%{name}/html/structjanus__videocall__session.html
%{_docdir}/%{name}/html/structjanus__videocall__session__coll__graph.map
%{_docdir}/%{name}/html/structjanus__videocall__session__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__videocall__session__coll__graph.png
%{_docdir}/%{name}/html/structjanus__videoroom.html
%{_docdir}/%{name}/html/structjanus__videoroom__coll__graph.map
%{_docdir}/%{name}/html/structjanus__videoroom__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__videoroom__coll__graph.png
%{_docdir}/%{name}/html/structjanus__videoroom__message.html
%{_docdir}/%{name}/html/structjanus__videoroom__message__coll__graph.map
%{_docdir}/%{name}/html/structjanus__videoroom__message__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__videoroom__message__coll__graph.png
%{_docdir}/%{name}/html/structjanus__videoroom__publisher.html
%{_docdir}/%{name}/html/structjanus__videoroom__publisher__coll__graph.map
%{_docdir}/%{name}/html/structjanus__videoroom__publisher__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__videoroom__publisher__coll__graph.png
%{_docdir}/%{name}/html/structjanus__videoroom__publisher__stream.html
%{_docdir}/%{name}/html/structjanus__videoroom__publisher__stream__coll__graph.map
%{_docdir}/%{name}/html/structjanus__videoroom__publisher__stream__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__videoroom__publisher__stream__coll__graph.png
%{_docdir}/%{name}/html/structjanus__videoroom__remote__recipient.html
%{_docdir}/%{name}/html/structjanus__videoroom__rtcp__receiver.html
%{_docdir}/%{name}/html/structjanus__videoroom__rtcp__receiver__coll__graph.map
%{_docdir}/%{name}/html/structjanus__videoroom__rtcp__receiver__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__videoroom__rtcp__receiver__coll__graph.png
%{_docdir}/%{name}/html/structjanus__videoroom__rtp__forwarder.html
%{_docdir}/%{name}/html/structjanus__videoroom__rtp__forwarder__coll__graph.map
%{_docdir}/%{name}/html/structjanus__videoroom__rtp__forwarder__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__videoroom__rtp__forwarder__coll__graph.png
%{_docdir}/%{name}/html/structjanus__videoroom__rtp__relay__packet.html
%{_docdir}/%{name}/html/structjanus__videoroom__rtp__relay__packet__coll__graph.map
%{_docdir}/%{name}/html/structjanus__videoroom__rtp__relay__packet__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__videoroom__rtp__relay__packet__coll__graph.png
%{_docdir}/%{name}/html/structjanus__videoroom__session.html
%{_docdir}/%{name}/html/structjanus__videoroom__session__coll__graph.map
%{_docdir}/%{name}/html/structjanus__videoroom__session__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__videoroom__session__coll__graph.png
%{_docdir}/%{name}/html/structjanus__videoroom__srtp__context.html
%{_docdir}/%{name}/html/structjanus__videoroom__subscriber.html
%{_docdir}/%{name}/html/structjanus__videoroom__subscriber__coll__graph.map
%{_docdir}/%{name}/html/structjanus__videoroom__subscriber__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__videoroom__subscriber__coll__graph.png
%{_docdir}/%{name}/html/structjanus__videoroom__subscriber__stream.html
%{_docdir}/%{name}/html/structjanus__videoroom__subscriber__stream__coll__graph.map
%{_docdir}/%{name}/html/structjanus__videoroom__subscriber__stream__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__videoroom__subscriber__stream__coll__graph.png
%{_docdir}/%{name}/html/structjanus__voicemail__message.html
%{_docdir}/%{name}/html/structjanus__voicemail__message__coll__graph.map
%{_docdir}/%{name}/html/structjanus__voicemail__message__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__voicemail__message__coll__graph.png
%{_docdir}/%{name}/html/structjanus__voicemail__session.html
%{_docdir}/%{name}/html/structjanus__voicemail__session__coll__graph.map
%{_docdir}/%{name}/html/structjanus__voicemail__session__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__voicemail__session__coll__graph.png
%{_docdir}/%{name}/html/structjanus__vp8__simulcast__context.html
%{_docdir}/%{name}/html/structjanus__vp9__svc__info.html
%{_docdir}/%{name}/html/structjanus__websockets__client.html
%{_docdir}/%{name}/html/structjanus__websockets__client__coll__graph.map
%{_docdir}/%{name}/html/structjanus__websockets__client__coll__graph.md5
%{_docdir}/%{name}/html/structjanus__websockets__client__coll__graph.png
%{_docdir}/%{name}/html/structjanus__wsevh__client.html
%{_docdir}/%{name}/html/structmjr2pcap__ethernet__header.html
%{_docdir}/%{name}/html/structmjr2pcap__global__header.html
%{_docdir}/%{name}/html/structmjr2pcap__ip__header.html
%{_docdir}/%{name}/html/structmjr2pcap__packet__header.html
%{_docdir}/%{name}/html/structmjr2pcap__udp__header.html
%{_docdir}/%{name}/html/structmultiple__fds.html
%{_docdir}/%{name}/html/structpcap2mjr__ethernet__header.html
%{_docdir}/%{name}/html/structreport__block.html
%{_docdir}/%{name}/html/structrtcp__app.html
%{_docdir}/%{name}/html/structrtcp__app__coll__graph.map
%{_docdir}/%{name}/html/structrtcp__app__coll__graph.md5
%{_docdir}/%{name}/html/structrtcp__app__coll__graph.png
%{_docdir}/%{name}/html/structrtcp__bye.html
%{_docdir}/%{name}/html/structrtcp__bye__coll__graph.map
%{_docdir}/%{name}/html/structrtcp__bye__coll__graph.md5
%{_docdir}/%{name}/html/structrtcp__bye__coll__graph.png
%{_docdir}/%{name}/html/structrtcp__context.html
%{_docdir}/%{name}/html/structrtcp__fb.html
%{_docdir}/%{name}/html/structrtcp__fb__coll__graph.map
%{_docdir}/%{name}/html/structrtcp__fb__coll__graph.md5
%{_docdir}/%{name}/html/structrtcp__fb__coll__graph.png
%{_docdir}/%{name}/html/structrtcp__fir.html
%{_docdir}/%{name}/html/structrtcp__header.html
%{_docdir}/%{name}/html/structrtcp__nack.html
%{_docdir}/%{name}/html/structrtcp__remb.html
%{_docdir}/%{name}/html/structrtcp__rr.html
%{_docdir}/%{name}/html/structrtcp__rr__coll__graph.map
%{_docdir}/%{name}/html/structrtcp__rr__coll__graph.md5
%{_docdir}/%{name}/html/structrtcp__rr__coll__graph.png
%{_docdir}/%{name}/html/structrtcp__sdes.html
%{_docdir}/%{name}/html/structrtcp__sdes__chunk.html
%{_docdir}/%{name}/html/structrtcp__sdes__coll__graph.map
%{_docdir}/%{name}/html/structrtcp__sdes__coll__graph.md5
%{_docdir}/%{name}/html/structrtcp__sdes__coll__graph.png
%{_docdir}/%{name}/html/structrtcp__sdes__item.html
%{_docdir}/%{name}/html/structrtcp__sr.html
%{_docdir}/%{name}/html/structrtcp__sr__coll__graph.map
%{_docdir}/%{name}/html/structrtcp__sr__coll__graph.md5
%{_docdir}/%{name}/html/structrtcp__sr__coll__graph.png
%{_docdir}/%{name}/html/structrtcp__transport__wide__cc__stats.html
%{_docdir}/%{name}/html/structrtcp__xr.html
%{_docdir}/%{name}/html/structrtcp__xr__coll__graph.map
%{_docdir}/%{name}/html/structrtcp__xr__coll__graph.md5
%{_docdir}/%{name}/html/structrtcp__xr__coll__graph.png
%{_docdir}/%{name}/html/structrtp__header.html
%{_docdir}/%{name}/html/structsender__info.html
%{_docdir}/%{name}/html/structssip__s.html
%{_docdir}/%{name}/html/structssip__s__coll__graph.map
%{_docdir}/%{name}/html/structssip__s__coll__graph.md5
%{_docdir}/%{name}/html/structssip__s__coll__graph.png
%{_docdir}/%{name}/html/structwav__header.html
%{_docdir}/%{name}/html/sync_off.png
%{_docdir}/%{name}/html/sync_on.png
%{_docdir}/%{name}/html/tab_a.png
%{_docdir}/%{name}/html/tab_ad.png
%{_docdir}/%{name}/html/tab_b.png
%{_docdir}/%{name}/html/tab_bd.png
%{_docdir}/%{name}/html/tab_h.png
%{_docdir}/%{name}/html/tab_hd.png
%{_docdir}/%{name}/html/tab_s.png
%{_docdir}/%{name}/html/tab_sd.png
%{_docdir}/%{name}/html/tabs.css
%{_docdir}/%{name}/html/text2pcap_8c.html
%{_docdir}/%{name}/html/text2pcap_8c__incl.map
%{_docdir}/%{name}/html/text2pcap_8c__incl.md5
%{_docdir}/%{name}/html/text2pcap_8c__incl.png
%{_docdir}/%{name}/html/text2pcap_8h.html
%{_docdir}/%{name}/html/text2pcap_8h__dep__incl.map
%{_docdir}/%{name}/html/text2pcap_8h__dep__incl.md5
%{_docdir}/%{name}/html/text2pcap_8h__dep__incl.png
%{_docdir}/%{name}/html/text2pcap_8h__incl.map
%{_docdir}/%{name}/html/text2pcap_8h__incl.md5
%{_docdir}/%{name}/html/text2pcap_8h__incl.png
%{_docdir}/%{name}/html/text2pcap_8h_source.html
%{_docdir}/%{name}/html/textroom.html
%{_docdir}/%{name}/html/transport_8c.html
%{_docdir}/%{name}/html/transport_8c__incl.map
%{_docdir}/%{name}/html/transport_8c__incl.md5
%{_docdir}/%{name}/html/transport_8c__incl.png
%{_docdir}/%{name}/html/transport_8h.html
%{_docdir}/%{name}/html/transport_8h__dep__incl.map
%{_docdir}/%{name}/html/transport_8h__dep__incl.md5
%{_docdir}/%{name}/html/transport_8h__dep__incl.png
%{_docdir}/%{name}/html/transport_8h__incl.map
%{_docdir}/%{name}/html/transport_8h__incl.md5
%{_docdir}/%{name}/html/transport_8h__incl.png
%{_docdir}/%{name}/html/transport_8h_source.html
%{_docdir}/%{name}/html/turnrest_8c.html
%{_docdir}/%{name}/html/turnrest_8h.html
%{_docdir}/%{name}/html/turnrest_8h__dep__incl.map
%{_docdir}/%{name}/html/turnrest_8h__dep__incl.md5
%{_docdir}/%{name}/html/turnrest_8h__dep__incl.png
%{_docdir}/%{name}/html/turnrest_8h_source.html
%{_docdir}/%{name}/html/utils_8c.html
%{_docdir}/%{name}/html/utils_8c__incl.map
%{_docdir}/%{name}/html/utils_8c__incl.md5
%{_docdir}/%{name}/html/utils_8c__incl.png
%{_docdir}/%{name}/html/utils_8h.html
%{_docdir}/%{name}/html/utils_8h__dep__incl.map
%{_docdir}/%{name}/html/utils_8h__dep__incl.md5
%{_docdir}/%{name}/html/utils_8h__dep__incl.png
%{_docdir}/%{name}/html/utils_8h__incl.map
%{_docdir}/%{name}/html/utils_8h__incl.md5
%{_docdir}/%{name}/html/utils_8h__incl.png
%{_docdir}/%{name}/html/utils_8h_source.html
%{_docdir}/%{name}/html/version_8c.html
%{_docdir}/%{name}/html/version_8c__incl.map
%{_docdir}/%{name}/html/version_8c__incl.md5
%{_docdir}/%{name}/html/version_8c__incl.png
%{_docdir}/%{name}/html/version_8h.html
%{_docdir}/%{name}/html/version_8h__dep__incl.map
%{_docdir}/%{name}/html/version_8h__dep__incl.md5
%{_docdir}/%{name}/html/version_8h__dep__incl.png
%{_docdir}/%{name}/html/version_8h_source.html
%{_docdir}/%{name}/html/videocall.html
%{_docdir}/%{name}/html/videoroom.html
%{_docdir}/%{name}/html/voicemail.html


%files tools
# binaries
%{_bindir}/janus-pp-rec
%{_bindir}/mjr2pcap
%{_bindir}/pcap2mjr

# manuals
%{_mandir}/man1/mjr2pcap.1.gz
%{_mandir}/man1/pcap2mjr.1.gz
%{_mandir}/man1/janus-pp-rec.1.gz


%changelog
* Wed Jan 04 2023 Renich Bon Ćirić <renich@woralelandia.com> - 1.1.1-4
- Applied patch to fix build. Upstream ticket is: https://github.com/meetecho/janus-gateway/pull/3138.

* Fri Dec 23 2022 Renich Bon Ćirić <renich@woralelandia.com> - 1.1.1-3
- Shortened summaries.
- Marked demos and docs as noarch.
- Removed the rs-jquery requirement.

* Sun Dec 18 2022 Renich Bon Ćirić <renich@woralelandia.com> - 1.1.1-2
- Converted remote web resources to local for docs and demos.
- Added a check finally.

* Fri Dec 16 2022 Renich Bon Ćirić <renich@woralelandia.com> - 1.1.1-1
- Updated to v1.1.1.
- Corrected plugins versions.

* Wed Nov 23 2022 Renich Bon Ćirić <renich@woralelandia.com> - 1.1.0-5
- Fixed file inclusion in order to avoid duplicates.

* Thu Nov 17 2022 Renich Bon Ćirić <renich@woralelandia.com> - 1.1.0-4
- Made dependency of janus in plugins more accurate.

* Mon Oct 31 2022 Renich Bon Ćirić <renich@woralelandia.com> - 1.1.0-3
- Fixed directory ownership.

* Tue Oct 18 2022 Renich Bon Ćirić <renich@woralelandia.com> - 1.1.0-2
- Re-adding demos and docs in HTML format.

* Mon Oct 03 2022 Renich Bon Ćirić <renich@woralelandia.com> - 1.0.4-7
- Adding noarch to doc subpackage.
- Removed doc and demos sub-package for now.

* Thu Sep 22 2022 Renich Bon Ćirić <renich@woralelandia.com> - 1.0.4-6
- Renamed package to janus to honor upstream's request.
- Added libpcap-devel so it builds pcap2mjr.
- Relocated some files due to upstream's advice.
- Properly adding configuration files.
- Added system user.

* Wed Sep 21 2022 Renich Bon Ćirić <renich@woralelandia.com> - 1.0.4-5
- Dividing package into sub-packages.
- Enabled the json-logger.

* Wed Sep 14 2022 Renich Bon Ćirić <renich@woralelandia.com> - 1.0.4-4
- Using name and version macros in main source declaration.
- Moved sample files into doc directory.

* Tue Aug 30 2022 Renich Bon Ćirić <renich@woralelandia.com> - 1.0.4-3
- Moved some headers to the -devel subpackage.
- Added BSD-3-Clause and MIT licenses.
- Added missing license file to the doc subpackage.

* Fri Aug 26 2022 Renich Bon Ćirić <renich@woralelandia.com> - 1.0.4-2
- Added missing BuildRequires for the systemd unit.

* Thu Aug 18 2022 Renich Bon Ćirić <renich@woralelandia.com> - 1.0.4-1
- first draft

Name: dragonfly-reverb
Version: 2.0.0
Release: 1%{?dist}
Summary: The Dragonfly Reverb audio effects

License: GPLv3+
URL: https://michaelwillis.github.io/dragonfly-reverb/	
Source0: https://github.com/michaelwillis/%{name}/releases/download/%{version}/DragonflyReverb-Source-v%{version}.tar.gz

BuildRequires: mesa-libGL-devel
BuildRequires: libX11-devel
BuildRequires: jack-audio-connection-kit-devel

%global common_desc \
Dragonfly Reverb is a bundle of two free audio effects: a concert hall reverb and a room reverb.

%description
%common_desc

The plugins are available in LV2 and Standalone JACK formats.
This package contains the common files and the Standalone JACK plugin.

%package -n lv2-%{name}-plugins
Summary:	Dragonfly Reverb plugins in LV2 format
Requires:	%{name} = %{version}-%{release}
Requires:	lv2core
 
%description -n lv2-%{name}-plugins
%common_desc

This package contains LV2 synthesizers and effects.

%prep
%setup -qn DragonflyReverb-Source-v%{version}

%build
make %{?_smp_mflags} DEBUG=true

%install
install -D -p -m755 bin/DragonflyHallReverb %{buildroot}%{_bindir}/DragonflyHallReverb
install -D -p -m755 bin/DragonflyRoomReverb %{buildroot}%{_bindir}/DragonflyRoomReverb

install -d %{buildroot}/%{_libdir}/lv2
cp -r bin/*.lv2 %{buildroot}/%{_libdir}/lv2/

%files
%doc README.md
%license LICENSE
%{_bindir}/DragonflyHallReverb
%{_bindir}/DragonflyRoomReverb

%files -n lv2-%{name}-plugins
%{_libdir}/lv2/*.lv2/

%changelog
* Wed Jan 08 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 2.0.0-1
- Initial build

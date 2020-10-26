Name: dragonfly-reverb
Version: 3.2.1
Release: 1%{?dist}
Summary: The Dragonfly Reverb audio effects

# common/freeverb/COPYING: GPLv2+
# common/libsamplerate2/COPYING: GPLv2+
# dpf/LICENSE: ISC
# common/NotoSans/SIL Open Font License.txt: OFL
# common/kiss_fft/COPYING.txt: BSD
License: GPLv3+ and GPLv2+ and ISC and OFL and BSD

URL: https://michaelwillis.github.io/dragonfly-reverb/	
Source0: https://github.com/michaelwillis/dragonfly-reverb/releases/download/%{version}/DragonflyReverb-Source-v%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: mesa-libGL-devel
BuildRequires: libX11-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: fftw-devel

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
%autosetup -n DragonflyReverb-Source-v%{version}

%build
%make_build DEBUG=true

%install
install -D -p -m755 bin/DragonflyEarlyReflections %{buildroot}%{_bindir}/DragonflyEarlyReflections
install -D -p -m755 bin/DragonflyHallReverb %{buildroot}%{_bindir}/DragonflyHallReverb
install -D -p -m755 bin/DragonflyPlateReverb %{buildroot}%{_bindir}/DragonflyPlateReverb
install -D -p -m755 bin/DragonflyRoomReverb %{buildroot}%{_bindir}/DragonflyRoomReverb

install -d %{buildroot}/%{_libdir}/lv2
cp -r bin/*.lv2 %{buildroot}/%{_libdir}/lv2/

%files
%doc README.md
%license LICENSE
%{_bindir}/DragonflyEarlyReflections
%{_bindir}/DragonflyHallReverb
%{_bindir}/DragonflyPlateReverb
%{_bindir}/DragonflyRoomReverb

%files -n lv2-%{name}-plugins
%{_libdir}/lv2/*.lv2/

%changelog
* Mon Oct 26 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 3.2.1-1
- Update to 3.2.1

* Tue Jul 14 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 3.2.0-1
- Update to 3.2.0

* Fri Mar 13 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 3.0.0-1
- Update to 3.0.0

* Wed Jan 08 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 2.0.0-1
- Initial build

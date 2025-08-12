Name:           autocutsel
Version:        0.10.1
Release:        1%{?dist}
Summary:        Synchronizes the X11 cutbuffer and CLIPBOARD selection

License:        GPLv2+
URL:            http://www.nongnu.org/autocutsel/
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc, make, libXtst-devel, xorg-x11-server-devel

%description
Autocutsel synchronizes the X11 cutbuffer and CLIPBOARD selection.

%prep
%setup -q

%build
./configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%files
/usr/local/bin/autocutsel
/usr/local/bin/cutsel

%changelog
* Tue Aug 12 2025 - 0.10.1-1
- Initial package

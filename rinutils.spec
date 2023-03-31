%define debug_package %{nil}
%global basen rinutils

Name: %{basen}
Version: 0.10.1
%global basenver %{basen}-%{version}
Release: 2
License: MIT
Source:  https://github.com/shlomif/rinutils/releases/download/%{version}/%{basenver}.tar.xz
URL: https://github.com/shlomif/rinutils/
Summary: Shlomi Fish's gnu11 C Library of Random headers
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	perl-devel
BuildRequires:	python

%description
Shlomi Fish's -std=gnu11 ( GCC / clang ) C library of random headers. Possibly
of limited general interest, but nevertheless free and open source software
(FOSS) under the MIT/Expat license.

%package devel
Summary: Shlomi Fish's gnu11 C Library of Random headers (development package)
Provides: %{basen}-static = %{version}-%{release}

%description devel
Shlomi Fish's -std=gnu11 ( GCC / clang ) C library of random headers. Possibly
of limited general interest, but nevertheless free and open source software
(FOSS) under the MIT/Expat license.

%prep
%autosetup -p1 -n %{basenver}
%cmake -DLOCALE_INSTALL_DIR=%{_datadir}/locale -DLIB_INSTALL_DIR=%{_libdir} -DWITH_TEST_SUITE=OFF -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files devel
%license LICENSE
%doc README.asciidoc NEWS.asciidoc
%{_includedir}/%{basen}
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/Rinutils

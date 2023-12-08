#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v3
# autospec commit: c1050fe
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : konquest
Version  : 23.08.3
Release  : 59
URL      : https://download.kde.org/stable/release-service/23.08.3/src/konquest-23.08.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.08.3/src/konquest-23.08.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.08.3/src/konquest-23.08.3.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GFDL-1.2 GPL-2.0
Requires: konquest-bin = %{version}-%{release}
Requires: konquest-data = %{version}-%{release}
Requires: konquest-license = %{version}-%{release}
Requires: konquest-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : libkdegames-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Konquest
--------
Konquest is a multi-player strategy game. The goal of
the game is to expand your interstellar empire across the
galaxy and, of course, crush your rivals in the process.

%package bin
Summary: bin components for the konquest package.
Group: Binaries
Requires: konquest-data = %{version}-%{release}
Requires: konquest-license = %{version}-%{release}

%description bin
bin components for the konquest package.


%package data
Summary: data components for the konquest package.
Group: Data

%description data
data components for the konquest package.


%package doc
Summary: doc components for the konquest package.
Group: Documentation

%description doc
doc components for the konquest package.


%package license
Summary: license components for the konquest package.
Group: Default

%description license
license components for the konquest package.


%package locales
Summary: locales components for the konquest package.
Group: Default

%description locales
locales components for the konquest package.


%prep
%setup -q -n konquest-23.08.3
cd %{_builddir}/konquest-23.08.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1702000519
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1702000519
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/konquest
cp %{_builddir}/konquest-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/konquest/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/konquest-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/konquest/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/konquest-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/konquest/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/konquest-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/konquest/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/konquest-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/konquest/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang konquest
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/konquest
/usr/bin/konquest

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.konquest.desktop
/usr/share/icons/hicolor/128x128/apps/konquest.png
/usr/share/icons/hicolor/16x16/apps/konquest.png
/usr/share/icons/hicolor/22x22/apps/konquest.png
/usr/share/icons/hicolor/32x32/apps/konquest.png
/usr/share/icons/hicolor/48x48/apps/konquest.png
/usr/share/icons/hicolor/64x64/apps/konquest.png
/usr/share/konquest/pics/default_theme.svgz
/usr/share/konquest/pics/konquest-splash.png
/usr/share/metainfo/org.kde.konquest.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/konquest/index.cache.bz2
/usr/share/doc/HTML/ca/konquest/index.docbook
/usr/share/doc/HTML/ca/konquest/ingame_window.png
/usr/share/doc/HTML/ca/konquest/main_game_window.png
/usr/share/doc/HTML/ca/konquest/new_game_settings.png
/usr/share/doc/HTML/de/konquest/index.cache.bz2
/usr/share/doc/HTML/de/konquest/index.docbook
/usr/share/doc/HTML/en/konquest/index.cache.bz2
/usr/share/doc/HTML/en/konquest/index.docbook
/usr/share/doc/HTML/en/konquest/ingame_window.png
/usr/share/doc/HTML/en/konquest/main_game_window.png
/usr/share/doc/HTML/en/konquest/new_game_settings.png
/usr/share/doc/HTML/es/konquest/index.cache.bz2
/usr/share/doc/HTML/es/konquest/index.docbook
/usr/share/doc/HTML/et/konquest/index.cache.bz2
/usr/share/doc/HTML/et/konquest/index.docbook
/usr/share/doc/HTML/fr/konquest/index.cache.bz2
/usr/share/doc/HTML/fr/konquest/index.docbook
/usr/share/doc/HTML/gl/konquest/index.cache.bz2
/usr/share/doc/HTML/gl/konquest/index.docbook
/usr/share/doc/HTML/it/konquest/index.cache.bz2
/usr/share/doc/HTML/it/konquest/index.docbook
/usr/share/doc/HTML/nl/konquest/index.cache.bz2
/usr/share/doc/HTML/nl/konquest/index.docbook
/usr/share/doc/HTML/pl/konquest/index.cache.bz2
/usr/share/doc/HTML/pl/konquest/index.docbook
/usr/share/doc/HTML/pt/konquest/index.cache.bz2
/usr/share/doc/HTML/pt/konquest/index.docbook
/usr/share/doc/HTML/pt_BR/konquest/index.cache.bz2
/usr/share/doc/HTML/pt_BR/konquest/index.docbook
/usr/share/doc/HTML/ru/konquest/index.cache.bz2
/usr/share/doc/HTML/ru/konquest/index.docbook
/usr/share/doc/HTML/sv/konquest/index.cache.bz2
/usr/share/doc/HTML/sv/konquest/index.docbook
/usr/share/doc/HTML/uk/konquest/index.cache.bz2
/usr/share/doc/HTML/uk/konquest/index.docbook
/usr/share/doc/HTML/uk/konquest/ingame_window.png
/usr/share/doc/HTML/uk/konquest/main_game_window.png
/usr/share/doc/HTML/uk/konquest/new_game_settings.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/konquest/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/konquest/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/konquest/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/konquest/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/konquest/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c

%files locales -f konquest.lang
%defattr(-,root,root,-)


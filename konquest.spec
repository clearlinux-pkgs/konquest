#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : konquest
Version  : 21.08.2
Release  : 30
URL      : https://download.kde.org/stable/release-service/21.08.2/src/konquest-21.08.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/21.08.2/src/konquest-21.08.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/21.08.2/src/konquest-21.08.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: konquest-bin = %{version}-%{release}
Requires: konquest-data = %{version}-%{release}
Requires: konquest-license = %{version}-%{release}
Requires: konquest-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : libkdegames-dev
BuildRequires : qtbase-dev mesa-dev

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
%setup -q -n konquest-21.08.2
cd %{_builddir}/konquest-21.08.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1634347272
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1634347272
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/konquest
cp %{_builddir}/konquest-21.08.2/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/konquest/7697008f58568e61e7598e796eafc2a997503fde
cp %{_builddir}/konquest-21.08.2/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/konquest/3e8971c6c5f16674958913a94a36b1ea7a00ac46
pushd clr-build
%make_install
popd
%find_lang konquest

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
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
/usr/share/package-licenses/konquest/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/konquest/7697008f58568e61e7598e796eafc2a997503fde

%files locales -f konquest.lang
%defattr(-,root,root,-)


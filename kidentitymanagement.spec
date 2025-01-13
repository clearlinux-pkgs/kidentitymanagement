#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: f4a13a5
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kidentitymanagement
Version  : 24.12.1
Release  : 80
URL      : https://download.kde.org/stable/release-service/24.12.1/src/kidentitymanagement-24.12.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.12.1/src/kidentitymanagement-24.12.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.12.1/src/kidentitymanagement-24.12.1.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause CC0-1.0 GPL-3.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: kidentitymanagement-data = %{version}-%{release}
Requires: kidentitymanagement-lib = %{version}-%{release}
Requires: kidentitymanagement-license = %{version}-%{release}
Requires: kidentitymanagement-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kpimtextedit-dev
BuildRequires : ktextaddons-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Analyzing Build Performance
For debug build time:
We need ClangBuildAnalyzer
git clone https://github.com/aras-p/ClangBuildAnalyzer
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=<path> ../
make install

%package data
Summary: data components for the kidentitymanagement package.
Group: Data

%description data
data components for the kidentitymanagement package.


%package dev
Summary: dev components for the kidentitymanagement package.
Group: Development
Requires: kidentitymanagement-lib = %{version}-%{release}
Requires: kidentitymanagement-data = %{version}-%{release}
Provides: kidentitymanagement-devel = %{version}-%{release}
Requires: kidentitymanagement = %{version}-%{release}

%description dev
dev components for the kidentitymanagement package.


%package lib
Summary: lib components for the kidentitymanagement package.
Group: Libraries
Requires: kidentitymanagement-data = %{version}-%{release}
Requires: kidentitymanagement-license = %{version}-%{release}

%description lib
lib components for the kidentitymanagement package.


%package license
Summary: license components for the kidentitymanagement package.
Group: Default

%description license
license components for the kidentitymanagement package.


%package locales
Summary: locales components for the kidentitymanagement package.
Group: Default

%description locales
locales components for the kidentitymanagement package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n kidentitymanagement-24.12.1
cd %{_builddir}/kidentitymanagement-24.12.1
pushd ..
cp -a kidentitymanagement-24.12.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1736727917
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
export GOAMD64=v2
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
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
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
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
export SOURCE_DATE_EPOCH=1736727917
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kidentitymanagement
cp %{_builddir}/kidentitymanagement-%{version}/.krazy.license %{buildroot}/usr/share/package-licenses/kidentitymanagement/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
cp %{_builddir}/kidentitymanagement-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/kidentitymanagement/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e || :
cp %{_builddir}/kidentitymanagement-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kidentitymanagement/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kidentitymanagement-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kidentitymanagement/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/kidentitymanagement-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kidentitymanagement/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kidentitymanagement-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kidentitymanagement/fa05e58320cb7c64786b26396f4b992579a628bc || :
cp %{_builddir}/kidentitymanagement-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/kidentitymanagement/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/kidentitymanagement-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kidentitymanagement/0b71159e19bef95069e18d17296291916e89b5cd || :
cp %{_builddir}/kidentitymanagement-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kidentitymanagement/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kidentitymanagement-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kidentitymanagement/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kidentitymanagement-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/kidentitymanagement/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang libkpimidentities6
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/interfaces/kf6_org.kde.pim.IdentityManager.xml
/usr/share/qlogging-categories6/kidentitymanagement.categories
/usr/share/qlogging-categories6/kidentitymanagement.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KPim6/KIdentityManagementCore/KIdentityManagementCore/Identity
/usr/include/KPim6/KIdentityManagementCore/KIdentityManagementCore/IdentityActivitiesAbstract
/usr/include/KPim6/KIdentityManagementCore/KIdentityManagementCore/IdentityManager
/usr/include/KPim6/KIdentityManagementCore/KIdentityManagementCore/IdentityModel
/usr/include/KPim6/KIdentityManagementCore/KIdentityManagementCore/IdentityTreeModel
/usr/include/KPim6/KIdentityManagementCore/KIdentityManagementCore/IdentityTreeSortProxyModel
/usr/include/KPim6/KIdentityManagementCore/KIdentityManagementCore/Signature
/usr/include/KPim6/KIdentityManagementCore/KIdentityManagementCore/Utils
/usr/include/KPim6/KIdentityManagementCore/kidentitymanagementcore/identity.h
/usr/include/KPim6/KIdentityManagementCore/kidentitymanagementcore/identityactivitiesabstract.h
/usr/include/KPim6/KIdentityManagementCore/kidentitymanagementcore/identitymanager.h
/usr/include/KPim6/KIdentityManagementCore/kidentitymanagementcore/identitymodel.h
/usr/include/KPim6/KIdentityManagementCore/kidentitymanagementcore/identitytreemodel.h
/usr/include/KPim6/KIdentityManagementCore/kidentitymanagementcore/identitytreesortproxymodel.h
/usr/include/KPim6/KIdentityManagementCore/kidentitymanagementcore/kidentitymanagementcore_export.h
/usr/include/KPim6/KIdentityManagementCore/kidentitymanagementcore/signature.h
/usr/include/KPim6/KIdentityManagementCore/kidentitymanagementcore/utils.h
/usr/include/KPim6/KIdentityManagementCore/kidentitymanagementcore_version.h
/usr/include/KPim6/KIdentityManagementQuick/KIdentityManagementQuick/CryptographyBackendInterface
/usr/include/KPim6/KIdentityManagementQuick/KIdentityManagementQuick/CryptographyEditorBackend
/usr/include/KPim6/KIdentityManagementQuick/KIdentityManagementQuick/KeyListModelInterface
/usr/include/KPim6/KIdentityManagementQuick/kidentitymanagementquick/cryptographybackendinterface.h
/usr/include/KPim6/KIdentityManagementQuick/kidentitymanagementquick/cryptographyeditorbackend.h
/usr/include/KPim6/KIdentityManagementQuick/kidentitymanagementquick/keylistmodelinterface.h
/usr/include/KPim6/KIdentityManagementQuick/kidentitymanagementquick/kidentitymanagementquick_export.h
/usr/include/KPim6/KIdentityManagementQuick/kidentitymanagementquick_version.h
/usr/include/KPim6/KIdentityManagementWidgets/KIdentityManagementWidgets/IdentityCombo
/usr/include/KPim6/KIdentityManagementWidgets/KIdentityManagementWidgets/IdentityTreeView
/usr/include/KPim6/KIdentityManagementWidgets/KIdentityManagementWidgets/SignatureConfigurator
/usr/include/KPim6/KIdentityManagementWidgets/kidentitymanagementwidgets/identitycombo.h
/usr/include/KPim6/KIdentityManagementWidgets/kidentitymanagementwidgets/identitytreeview.h
/usr/include/KPim6/KIdentityManagementWidgets/kidentitymanagementwidgets/kidentitymanagementwidgets_export.h
/usr/include/KPim6/KIdentityManagementWidgets/kidentitymanagementwidgets/signatureconfigurator.h
/usr/include/KPim6/KIdentityManagementWidgets/kidentitymanagementwidgets_version.h
/usr/lib64/cmake/KPim6IdentityManagementCore/KPim6IdentityManagementCoreConfig.cmake
/usr/lib64/cmake/KPim6IdentityManagementCore/KPim6IdentityManagementCoreConfigVersion.cmake
/usr/lib64/cmake/KPim6IdentityManagementCore/KPim6IdentityManagementCoreTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim6IdentityManagementCore/KPim6IdentityManagementCoreTargets.cmake
/usr/lib64/cmake/KPim6IdentityManagementQuick/KPim6IdentityManagementQuickConfig.cmake
/usr/lib64/cmake/KPim6IdentityManagementQuick/KPim6IdentityManagementQuickConfigVersion.cmake
/usr/lib64/cmake/KPim6IdentityManagementQuick/KPim6IdentityManagementQuickTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim6IdentityManagementQuick/KPim6IdentityManagementQuickTargets.cmake
/usr/lib64/cmake/KPim6IdentityManagementWidgets/KPim6IdentityManagementWidgetsConfig.cmake
/usr/lib64/cmake/KPim6IdentityManagementWidgets/KPim6IdentityManagementWidgetsConfigVersion.cmake
/usr/lib64/cmake/KPim6IdentityManagementWidgets/KPim6IdentityManagementWidgetsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim6IdentityManagementWidgets/KPim6IdentityManagementWidgetsTargets.cmake
/usr/lib64/libKPim6IdentityManagementCore.so
/usr/lib64/libKPim6IdentityManagementQuick.so
/usr/lib64/libKPim6IdentityManagementWidgets.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKPim6IdentityManagementCore.so.6.3.1
/V3/usr/lib64/libKPim6IdentityManagementQuick.so.6.3.1
/V3/usr/lib64/libKPim6IdentityManagementWidgets.so.6.3.1
/V3/usr/lib64/qt6/qml/org/kde/kidentitymanagement/libkidentitymanagement_quick_plugin.so
/usr/lib64/libKPim6IdentityManagementCore.so.6
/usr/lib64/libKPim6IdentityManagementCore.so.6.3.1
/usr/lib64/libKPim6IdentityManagementQuick.so.6
/usr/lib64/libKPim6IdentityManagementQuick.so.6.3.1
/usr/lib64/libKPim6IdentityManagementWidgets.so.6
/usr/lib64/libKPim6IdentityManagementWidgets.so.6.3.1
/usr/lib64/qt6/qml/org/kde/kidentitymanagement/BasicIdentityEditorCard.qml
/usr/lib64/qt6/qml/org/kde/kidentitymanagement/CryptographyEditorCard.qml
/usr/lib64/qt6/qml/org/kde/kidentitymanagement/IdentityConfigurationForm.qml
/usr/lib64/qt6/qml/org/kde/kidentitymanagement/IdentityEditorPage.qml
/usr/lib64/qt6/qml/org/kde/kidentitymanagement/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/kidentitymanagement/kidentitymanagement_quick_plugin.qmltypes
/usr/lib64/qt6/qml/org/kde/kidentitymanagement/libkidentitymanagement_quick_plugin.so
/usr/lib64/qt6/qml/org/kde/kidentitymanagement/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kidentitymanagement/0b71159e19bef95069e18d17296291916e89b5cd
/usr/share/package-licenses/kidentitymanagement/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kidentitymanagement/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e
/usr/share/package-licenses/kidentitymanagement/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/kidentitymanagement/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/kidentitymanagement/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kidentitymanagement/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kidentitymanagement/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/kidentitymanagement/fa05e58320cb7c64786b26396f4b992579a628bc

%files locales -f libkpimidentities6.lang
%defattr(-,root,root,-)


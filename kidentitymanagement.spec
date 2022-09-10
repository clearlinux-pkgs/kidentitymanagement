#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kidentitymanagement
Version  : 22.08.1
Release  : 44
URL      : https://download.kde.org/stable/release-service/22.08.1/src/kidentitymanagement-22.08.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.08.1/src/kidentitymanagement-22.08.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/22.08.1/src/kidentitymanagement-22.08.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 LGPL-2.0 LGPL-2.1
Requires: kidentitymanagement-data = %{version}-%{release}
Requires: kidentitymanagement-lib = %{version}-%{release}
Requires: kidentitymanagement-license = %{version}-%{release}
Requires: kidentitymanagement-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kcodecs-dev
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kio-dev
BuildRequires : kpimtextedit-dev
BuildRequires : ktextwidgets-dev
BuildRequires : kxmlgui-dev
BuildRequires : qt6base-dev

%description
No detailed description available

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
%setup -q -n kidentitymanagement-22.08.1
cd %{_builddir}/kidentitymanagement-22.08.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1662781654
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
export SOURCE_DATE_EPOCH=1662781654
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kidentitymanagement
cp %{_builddir}/kidentitymanagement-%{version}/.codespellrc.license %{buildroot}/usr/share/package-licenses/kidentitymanagement/c011fda7746c087a127999da1c4044854ee42238
cp %{_builddir}/kidentitymanagement-%{version}/.krazy.license %{buildroot}/usr/share/package-licenses/kidentitymanagement/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
cp %{_builddir}/kidentitymanagement-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kidentitymanagement/c085897bc39e05746ffd2d889a6e84ff1b7ae2d9
cp %{_builddir}/kidentitymanagement-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kidentitymanagement/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
cp %{_builddir}/kidentitymanagement-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kidentitymanagement/8287b608d3fa40ef401339fd907ca1260c964123
cp %{_builddir}/kidentitymanagement-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kidentitymanagement/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/kidentitymanagement-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/kidentitymanagement/6f1f675aa5f6a2bbaa573b8343044b166be28399
cp %{_builddir}/kidentitymanagement-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/kidentitymanagement/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
pushd clr-build
%make_install
popd
%find_lang libkpimidentities5

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/interfaces/kf5_org.kde.pim.IdentityManager.xml
/usr/share/qlogging-categories5/kidentitymanagement.categories
/usr/share/qlogging-categories5/kidentitymanagement.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KIdentityManagement/KIdentityManagement/Identity
/usr/include/KF5/KIdentityManagement/KIdentityManagement/IdentityManager
/usr/include/KF5/KIdentityManagement/KIdentityManagement/Signature
/usr/include/KF5/KIdentityManagement/KIdentityManagement/Utils
/usr/include/KF5/KIdentityManagement/kidentitymanagement/identity.h
/usr/include/KF5/KIdentityManagement/kidentitymanagement/identitymanager.h
/usr/include/KF5/KIdentityManagement/kidentitymanagement/kidentitymanagement_export.h
/usr/include/KF5/KIdentityManagement/kidentitymanagement/signature.h
/usr/include/KF5/KIdentityManagement/kidentitymanagement/utils.h
/usr/include/KF5/KIdentityManagement/kidentitymanagement_version.h
/usr/include/KF5/KIdentityManagementWidgets/KIdentityManagement/IdentityCombo
/usr/include/KF5/KIdentityManagementWidgets/KIdentityManagement/SignatureConfigurator
/usr/include/KF5/KIdentityManagementWidgets/kidentitymanagement/identitycombo.h
/usr/include/KF5/KIdentityManagementWidgets/kidentitymanagement/kidentitymanagementwidgets_export.h
/usr/include/KF5/KIdentityManagementWidgets/kidentitymanagement/signatureconfigurator.h
/usr/lib64/cmake/KF5IdentityManagement/KF5IdentityManagementConfig.cmake
/usr/lib64/cmake/KF5IdentityManagement/KF5IdentityManagementConfigVersion.cmake
/usr/lib64/cmake/KF5IdentityManagement/KF5IdentityManagementTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5IdentityManagement/KF5IdentityManagementTargets.cmake
/usr/lib64/libKF5IdentityManagement.so
/usr/lib64/libKF5IdentityManagementWidgets.so
/usr/lib64/qt5/mkspecs/modules/qt_KIdentityManagement.pri
/usr/lib64/qt5/mkspecs/modules/qt_KIdentityManagementWidgets.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5IdentityManagement.so.5
/usr/lib64/libKF5IdentityManagement.so.5.21.1
/usr/lib64/libKF5IdentityManagementWidgets.so.5
/usr/lib64/libKF5IdentityManagementWidgets.so.5.21.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kidentitymanagement/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kidentitymanagement/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/kidentitymanagement/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/kidentitymanagement/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kidentitymanagement/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kidentitymanagement/c011fda7746c087a127999da1c4044854ee42238
/usr/share/package-licenses/kidentitymanagement/c085897bc39e05746ffd2d889a6e84ff1b7ae2d9

%files locales -f libkpimidentities5.lang
%defattr(-,root,root,-)


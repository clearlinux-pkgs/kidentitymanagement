#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kidentitymanagement
Version  : 19.04.3
Release  : 11
URL      : https://download.kde.org/stable/applications/19.04.3/src/kidentitymanagement-19.04.3.tar.xz
Source0  : https://download.kde.org/stable/applications/19.04.3/src/kidentitymanagement-19.04.3.tar.xz
Source99 : https://download.kde.org/stable/applications/19.04.3/src/kidentitymanagement-19.04.3.tar.xz.sig
Summary  : KDE PIM libraries
Group    : Development/Tools
License  : LGPL-2.1
Requires: kidentitymanagement-data = %{version}-%{release}
Requires: kidentitymanagement-lib = %{version}-%{release}
Requires: kidentitymanagement-license = %{version}-%{release}
Requires: kidentitymanagement-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kpimtextedit-dev

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
%setup -q -n kidentitymanagement-19.04.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1562904073
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1562904073
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kidentitymanagement
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/kidentitymanagement/COPYING.LIB
pushd clr-build
%make_install
popd
%find_lang libkpimidentities5

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/interfaces/kf5_org.kde.pim.IdentityManager.xml
/usr/share/xdg/kidentitymanagement.categories
/usr/share/xdg/kidentitymanagement.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KIdentityManagement/KIdentityManagement/Identity
/usr/include/KF5/KIdentityManagement/KIdentityManagement/IdentityCombo
/usr/include/KF5/KIdentityManagement/KIdentityManagement/IdentityManager
/usr/include/KF5/KIdentityManagement/KIdentityManagement/Signature
/usr/include/KF5/KIdentityManagement/KIdentityManagement/SignatureConfigurator
/usr/include/KF5/KIdentityManagement/KIdentityManagement/Utils
/usr/include/KF5/KIdentityManagement/kidentitymanagement/identity.h
/usr/include/KF5/KIdentityManagement/kidentitymanagement/identitycombo.h
/usr/include/KF5/KIdentityManagement/kidentitymanagement/identitymanager.h
/usr/include/KF5/KIdentityManagement/kidentitymanagement/kidentitymanagement_export.h
/usr/include/KF5/KIdentityManagement/kidentitymanagement/signature.h
/usr/include/KF5/KIdentityManagement/kidentitymanagement/signatureconfigurator.h
/usr/include/KF5/KIdentityManagement/kidentitymanagement/utils.h
/usr/include/KF5/kidentitymanagement_version.h
/usr/lib64/cmake/KF5IdentityManagement/KF5IdentityManagementConfig.cmake
/usr/lib64/cmake/KF5IdentityManagement/KF5IdentityManagementConfigVersion.cmake
/usr/lib64/cmake/KF5IdentityManagement/KF5IdentityManagementTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5IdentityManagement/KF5IdentityManagementTargets.cmake
/usr/lib64/libKF5IdentityManagement.so
/usr/lib64/qt5/mkspecs/modules/qt_KIdentityManagement.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5IdentityManagement.so.5
/usr/lib64/libKF5IdentityManagement.so.5.11.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kidentitymanagement/COPYING.LIB

%files locales -f libkpimidentities5.lang
%defattr(-,root,root,-)


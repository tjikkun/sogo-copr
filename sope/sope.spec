Summary:      SOPE
Name:         sope
Version:      5.8.0
Release:      1%{dist}
License:      GPL
URL:          https://github.com/inverse-inc/sope
Group:        Development/Libraries/Objective C
Source:       https://packages.sogo.nu/sources/SOPE-%{version}.tar.gz

BuildRequires: gnustep-make
BuildRequires: gnustep-base
BuildRequires: gnustep-base-devel
BuildRequires: postgresql-devel
BuildRequires: mariadb-devel
BuildRequires: openldap-devel
BuildRequires: make
BuildRequires: gcc-objc
BuildRequires: libnsl2-devel
BuildRequires: libxml2-devel

%description
sope

#########################################
%package xml
Summary:      SOPE libraries for XML processing
Group:        Development/Libraries/Objective C

%description xml
The SOPE libraries for XML processing contain:

  * a SAX2 Implementation for Objective-C
  * an attempt to implement DOM on top of SaxObjC
  * an XML-RPC implementation (without a transport layer)

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

%package xml-devel
Summary:      Development files for the SOPE XML libraries
Group:        Development/Libraries/Objective C

%description xml-devel
This package contains the development files of the SOPE XML libraries.

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

#########################################
%package sbjson
Summary:      JSON framework
Group:        Development/Libraries/Objective C
Version:      %{version}

%description sbjson
The SBJson library is a high performance JSON library in Objective-C.

Project homepage is: http://code.google.com/p/json-framework/

%package sbjson-devel
Summary:      JSON framework (devel)
Group:        Development/Libraries/Objective C
Version:      %{version}

%description sbjson-devel
The SBJson library is a high performance JSON library in Objective-C.

Those are the files required for development.

Project homepage is: http://code.google.com/p/json-framework/

#########################################
%package core
Summary:      Core libraries of the SOPE application server
Group:        Development/Libraries/Objective C

%description core
The SOPE core libraries contain:

  * various Foundation extensions
  * a java.io like stream and socket library

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

%package core-devel
Summary:      Development files for the SOPE core libraries
Group:        Development/Libraries/Objective C

%description core-devel
This package contains the header files for the SOPE core
libraries,  which are part of the SOPE application server framework.

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

#########################################
%package mime
Summary:      SOPE libraries for MIME processing
Group:        Development/Libraries/Objective C

%description mime
The SOPE libraries for MIME processing contain:

  * classes for processing MIME entities
  * a full IMAP4 implementation
  * prototypical POP3 and SMTP processor

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

%package mime-devel
Summary:      Development files for the SOPE MIME libraries
Group:        Development/Libraries/Objective C

%description mime-devel
This package contains the development files of the SOPE
MIME libraries.

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

#########################################
%package appserver
Summary:      SOPE application server libraries
Group:        Development/Libraries/Objective C

%description appserver
The SOPE application server libraries provide:

  * template rendering engine, lots of dynamic elements
  * HTTP client/server
  * XML-RPC client
  * WebDAV server framework
  * session management
  * scripting extensions for Foundation, JavaScript bridge
  * DOM tree rendering library

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

%package appserver-devel
Summary:      Development files for the SOPE application server libraries
Group:        Development/Libraries/Objective C

%description appserver-devel
This package contains the development files for the SOPE application server
libraries.

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

#########################################
%package ldap
Summary:      SOPE libraries for LDAP access
Group:        Development/Libraries/Objective C

%description ldap
The SOPE libraries for LDAP access contain an Objective-C wrapper for
LDAP directory services.

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

%package ldap-devel
Summary:      Development files for the SOPE LDAP libraries
Group:        Development/Libraries/Objective C
Requires:     openldap-devel

%description ldap-devel
This package contains the development files of the SOPE
LDAP libraries.

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

#########################################
%package gdl1
Summary:      GNUstep database libraries for SOPE
Group:        Development/Libraries/Objective C

%description gdl1
This package contains a fork of the GNUstep database libraries used
by the SOPE application server (excluding GDLContentStore).

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

%package gdl1-postgresql
Summary:      PostgreSQL connector for SOPE's fork of the GNUstep database environment
Group:        Development/Libraries/Objective C

%description gdl1-postgresql
This package contains the PostgreSQL connector for SOPE's fork of the
GNUstep database libraries.

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

%package gdl1-mysql
Summary:      MySQL connector for SOPE's fork of the GNUstep database environment
Group:        Development/Libraries/Objective C

%description gdl1-mysql
This package contains the MySQL connector for SOPE's fork of the
GNUstep database libraries.


%package gdl1-devel
Summary:      Development files for the GNUstep database libraries
Group:        Development/Libraries/Objective C

%description gdl1-devel
This package contains the header files for SOPE's fork of the GNUstep
database libraries.

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

%prep
%autosetup -n SOPE

# ****************************** build ********************************
%build
#if [ -f /usr/lib/rpm/redhat/config.sub ]
#then
#  cp /usr/lib/rpm/redhat/{config.sub,config.guess} sope-core/NGStreams/
#elif [ -f /usr/lib/rpm/config.sub ]
#then
#  cp /usr/lib/rpm/{config.sub,config.guess} sope-core/NGStreams/
#fi

./configure \
            --disable-debug \
            --disable-strip \
            --with-gnustep
#            --enable-debug \

%make_build
cd sope-gdl1/MySQL
%make_build


%install
make DESTDIR=${RPM_BUILD_ROOT} \
     GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
     install

cd sope-gdl1/MySQL
make DESTDIR=${RPM_BUILD_ROOT} \
     GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
     install
rm -f ${RPM_BUILD_ROOT}%{_bindir}/otest
rm -fr ${RPM_BUILD_ROOT}%{_libdir}/GNUstep/GDLAdaptors-%{version}/SQLite3.gdladaptor

%files xml
%defattr(-,root,root,-)
%{_libdir}/libDOM*.so.*
%{_libdir}/libSaxObjC*.so.*
%{_libdir}/libXmlRpc*.so.*
%{_libdir}/GNUstep/SaxDrivers-*

%files xml-devel
%defattr(-,root,root,-)
%{_includedir}/DOM
%{_includedir}/SaxObjC
%{_includedir}/XmlRpc
%{_libdir}/libDOM*.so
%{_libdir}/libSaxObjC*.so
%{_libdir}/libXmlRpc*.so

%files sbjson
%defattr(-,root,root,-)
%{_libdir}/libSBJson.so.*

%files sbjson-devel
%defattr(-,root,root,-)
%{_includedir}/SBJson
%{_libdir}/libSBJson.so

%files core
%defattr(-,root,root,-)
%{_libdir}/libEOControl*.so.*
%{_libdir}/libNGExtensions*.so.*
%{_libdir}/libNGStreams*.so.*

%files core-devel
%defattr(-,root,root,-)
%{_includedir}/EOControl
%{_includedir}/NGExtensions
%{_includedir}/NGStreams
%{_libdir}/libEOControl*.so
%{_libdir}/libNGExtensions*.so
%{_libdir}/libNGStreams*.so

%files mime
%defattr(-,root,root,-)
%{_libdir}/libNGMime*.so.*

%files mime-devel
%defattr(-,root,root,-)
%{_includedir}/NGImap4
%{_includedir}/NGMail
%{_includedir}/NGMime
%{_libdir}/libNGMime*.so

%files appserver
%defattr(-,root,root,-)
%{_libdir}/libNGObjWeb*.so.*
%{_libdir}/libWEExtensions*.so.*
%{_libdir}/libWOExtensions*.so.*
%{_libdir}/GNUstep/Libraries/Resources/NGObjWeb/*
%{_libdir}/GNUstep/SoProducts-*
%{_libdir}/GNUstep/WOxElemBuilders-*

%files appserver-devel
%defattr(-,root,root,-)
%{_bindir}/wod
%{_includedir}/NGHttp
%{_includedir}/NGObjWeb
%{_includedir}/WEExtensions
%{_includedir}/WOExtensions
%{_libdir}/libNGObjWeb*.so
%{_libdir}/libWEExtensions*.so
%{_libdir}/libWOExtensions*.so
%{_libdir}/GNUstep/Makefiles

%files ldap
%defattr(-,root,root,-)
%{_libdir}/libNGLdap*.so.*

%files ldap-devel
%defattr(-,root,root,-)
%{_includedir}/NGLdap
%{_libdir}/libNGLdap*.so

%files gdl1
%defattr(-,root,root,-)
%{_bindir}/connect-EOAdaptor
%{_bindir}/load-EOAdaptor
%{_libdir}/libGDLAccess*.so.*

%files gdl1-postgresql
%defattr(-,root,root,-)
%{_libdir}/GNUstep/GDLAdaptors-*/PostgreSQL.gdladaptor

%files gdl1-mysql
%defattr(-,root,root,-)
%{_libdir}/GNUstep/GDLAdaptors-*/MySQL.gdladaptor

%files gdl1-devel
%defattr(-,root,root,-)
%{_includedir}/GDLAccess
%{_libdir}/libGDLAccess*.so

# ********************************* changelog *************************
%changelog
* Wed Jan 25 2023 Sander Hoentjen <sander@hoentjen.eu> - 5.8.0-1
- Initial packaging for Fedora

* Thu Aug 02 2012 Jean Raby <jraby@inverse.ca>
- Deduce the oracle lib path from the build arch
* Mon Dec 05 2011 Jean Raby <jraby@inverse.ca>
- adjust requires on new libfoundation
* Fri Sep 16 2005 Frank Reppin <frank@opengroupware.org>
- added WEPrototype and its lib to appserver/appserver-devel
* Fri Aug 26 2005 Frank Reppin <frank@opengroupware.org>
- added sope-gdl1-sqlite3 (as comment)
* Thu Apr 21 2005 Frank Reppin <frank@opengroupware.org>
- added sope-gdl1-mysql
* Tue Mar 22 2005 Frank Reppin <frank@opengroupware.org>
- added GDLContentStore to sope-gdl1
- reworked descriptions regarding GDLContentStore
- added new subpackage sope-gdl1-tools
- sope-gdl1 now depends on sope-xml due to -lDOM -lSaxObjC
  used by GDLContentStore
* Fri Jan 28 2005 Frank Reppin <frank@opengroupware.org>
- reworked dependencies
- deal with ld.so.conf in (post|preun) of appserver rather than core
* Tue Jan 25 2005 Frank Reppin <frank@opengroupware.org>
- fix for OGo Bug #1192
* Tue Jan 11 2005 Frank Reppin <frank@opengroupware.org>
- reworked all summaries and descriptions (taken from Debian control
  to be honest :>)
* Tue Nov 16 2004 Frank Reppin <frank@opengroupware.org>
- s^4.5^%{sope_version}^g everywhere bc .rpmmacros knows
  the current version we build for
* Sat Nov 06 2004 Helge Hess <helge.hess@opengroupware.org>
- updated to 4.5 version
* Thu Sep 09 2004 Frank Reppin <frank@opengroupware.org>
- initial build

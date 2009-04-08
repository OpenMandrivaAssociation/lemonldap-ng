Name:		lemonldap-ng
Summary:	A modular Web-SSO based on Apache::Session modules
Version:	0.9.2
Release:	%mkrel 2
URL:		http://wiki.lemonldap.objectweb.org/xwiki/bin/view/NG/Presentation
Source:		http://download.forge.objectweb.org/lemonldap/lemonldap-ng-%{version}.tar.gz
License:	Artistic
Group:		Development/Other
BuildRoot:	%{_tmppath}/%{name}-buildroot
%description
Lemonldap::NG is a modular Web-SSO based on Apache::Session modules.
It simplifies the build of a protected area with a few changes in the
application. It manages both authentication and authorization and provides
headers for accounting. So you can have a full AAA protection for your
web space as described below.

Lemonldap::NG is a complete rewrite of Lemonldap. All components needed
to use it and to aminister it are included in the tarball. Contrary,
all modules developed for Lemonldap may not work with Lemonldap::NG.

%prep
%setup -q

%build
%{__make}

%install
%{__rm} -Rf %{buildroot}
%{__make} DESTDIR=%{buildroot} INSTALLSITEBIN=%{_bindir} \
	  INSTALLSITESCRIPT=%{_bindir} INSTALLSITEMAN1DIR=%{_mandir}/man1 \
	  INSTALLSITEMAN3DIR=%{_mandir}/man3 INSTALLSITELIB=%perl_sitelib \
	  INSTALLSITEARCH=%perl_sitearch install

%clean
%{__rm} -Rf %{buildroot}

%files
%defattr(-,root,root)
%doc README TODO COPYING changelog doc/*
%{_bindir}/lmConfig_File2MySQL
%{_mandir}/man1/*
%{_mandir}/man3/*
%perl_sitelib/Lemonldap/NG/*
%perl_sitelib/auto/Lemonldap/NG/*


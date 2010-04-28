Name:		lemonldap-ng
Summary:	A modular Web-SSO based on Apache::Session modules
Version:	1.0
Release:	%mkrel 0.2.rc1
URL:		http://wiki.lemonldap.objectweb.org/xwiki/bin/view/NG/Presentation
Source:		http://download.forge.objectweb.org/lemonldap/lemonldap-ng-%{version}rc1.tar.gz
License:	Artistic
Group:		Development/Other
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch
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
%setup -q -n %{name}-%{version}rc1

%build
%{__make} INSTALLSITEBIN=%{_bindir} \
	  INSTALLSITESCRIPT=%{_bindir} INSTALLSITEMAN1DIR=%{_mandir}/man1 \
	  INSTALLSITEMAN3DIR=%{_mandir}/man3 INSTALLSITELIB=%perl_sitelib \
	  INSTALLSITEARCH=%perl_sitearch DOCUMENTROOT=%{_datadir}/%{name} \
	  CONF=%{_sysconfdir} BINDIR=%{_bindir} CRONDIR=%{_sysconfdir}/cron.d \
	  DATADIR=%{_var}/lib/%{name} HANDLERDIR=%{_datadir}/%{name}/handler \
	  TOOLSDIR=%{_datadir}/%{name}/tools EXAMPLESDIR=%{_datadir}/%{name}/examples \
	  CONFDIR=%{_sysconfdir}/%{name}

%install
%{__rm} -Rf %{buildroot}
%{__make} DESTDIR=%{buildroot} INSTALLSITEBIN=%{_bindir} \
	  INSTALLSITESCRIPT=%{_bindir} INSTALLSITEMAN1DIR=%{_mandir}/man1 \
	  INSTALLSITEMAN3DIR=%{_mandir}/man3 INSTALLSITELIB=%perl_sitelib \
	  INSTALLSITEARCH=%perl_sitearch DOCUMENTROOT=%{_datadir}/%{name} \
	  CONF=%{_sysconfdir} BINDIR=%{_bindir} CRONDIR=%{_sysconfdir}/cron.d \
	  DATADIR=%{_var}/lib/%{name} HANDLERDIR=%{_datadir}/%{name}/handler \
	  TOOLSDIR=%{_datadir}/%{name}/tools EXAMPLESDIR=%{_datadir}/%{name}/examples \
	  CONFDIR=%{_sysconfdir}/%{name} \
	install

pushd %{buildroot}%{_sysconfdir}/%{name}
%{__mkdir_p} %{buildroot}%_webappconfdir
for file in *.conf
do
  ln -s %{_sysconfdir}/%{name}/$file %{buildroot}%{_webappconfdir}/$file
done
popd

%clean
%{__rm} -Rf %{buildroot}

%post
%_post_webapp

%postun
%_postun_webapp

%files
%defattr(-,root,root)
%doc README COPYING changelog doc/*
%{_mandir}/man3/*
%perl_sitelib/Lemonldap/NG/*
%perl_sitelib/auto/Lemonldap/NG/*
%{_datadir}/%{name}
%{_var}/lib/%{name}
%config(noreplace) %{_sysconfdir}/cron.d/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*
%{_webappconfdir}/*.conf
%{_bindir}/*


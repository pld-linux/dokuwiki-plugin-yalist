%define		plugin		yalist
Summary:	DokuWiki Simple universal list plugin
Name:		dokuwiki-plugin-%{plugin}
Version:	20080708
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://www.paranoiacs.org/~sluskyb/hacks/dokuwiki/yalist/yalist-%{version}.tar.gz
# Source0-md5:	59b41460b9cb765b97ea1a93eca66f37
URL:		http://www.dokuwiki.org/plugin:yalist
Requires:	dokuwiki >= 20070626
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}

%description
This plugin extends DokuWiki's list markup syntax to allow definition
lists and list items with multiple paragraphs.

%prep
%setup -q -n %{plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
# force css cache refresh
if [ -f %{dokuconf}/local.php ]; then
	touch %{dokuconf}/local.php
fi

%files
%defattr(644,root,root,755)
%dir %{plugindir}
%{plugindir}/syntax.php
%{plugindir}/*.css

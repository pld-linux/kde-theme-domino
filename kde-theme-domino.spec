
%define         _name domino

Summary:	KDE theme - %{_name}
Summary(pl):	Motyw do KDE - %{_name}
Name:		kde-theme-%{_name}
Version:	0.4
Release:	1
License:	GPL
Group:		Themes
Source0:	http://kde-apps.org/CONTENT/content-files/42804-%{_name}-%{version}.tar.bz2
# Source0-md5:	c67bb1b986c4ff98ae640acff7b8562f
Patch0:		%{name}-am110.patch
Patch1:		kde-ac260-lt.patch
URL:		http://www.kde-look.org/content/show.php?content=42804
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.5.0
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	kde-colorscheme-%{_name}
Requires:	kde-decoration-%{_name}
Requires:	kde-style-%{_name}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{_name} KDE theme.

%description -l pl
Motyw KDE %{_name}.

%package -n kde-style-%{_name}
Summary:	KDE style - %{_name}
Summary(pl):	Styl do KDE - %{_name}
Group:		Themes
Requires:	kdelibs

%description -n kde-style-%{_name}
Domino is a style with a soft look. It allows to fine adjust the
shininess of the widgets by customizable color gradients.

%description -n kde-style-%{_name} -l pl
Domino jest stylem o miêkkim wygl±dzie. Umo¿liwia dopieszczenie
jasno¶ci widgetów dziêki configurowalnym gradientom.

%package -n kde-colorscheme-%{_name}
Summary:	Color scheme for KDE style - %{_name}
Summary(pl):	Schemat kolorów do stylu KDE - %{_name}
Group:		Themes
Requires:	kdebase-core

%description -n kde-colorscheme-%{_name}
Color scheme for KDE style - %{_name}.

%description -n kde-colorscheme-%{_name} -l pl
Schemat kolorów do stylu KDE - %{_name}.

%package -n kde-decoration-%{_name}
Summary:	Kwin decoration - %{_name}
Summary(pl):	Dekoracja kwin - %{_name}
Group:		Themes
Requires:	kdebase-desktop-libs

%description -n kde-decoration-%{_name}
Kwin decoration - %{_name}.

%description -n kde-decoration-%{_name} -l pl
Dekoracja kwin - %{_name}.

%prep
%setup -q -n %{_name}-%{version}
%patch0 -p0
%patch1 -p1

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir="%{_kdedocdir}"

%clean
rm -rf $RPM_BUILD_ROOT

%files

%files -n kde-style-%{_name}
%defattr(644,root,root,755)
%{_libdir}/kde3/kstyle_*.la
%attr(755,root,root) %{_libdir}/kde3/kstyle_*.so
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/*.so
%{_libdir}/kde3/plugins/styles/*.la
%{_datadir}/apps/kstyle/themes/*.themerc

%files -n kde-decoration-%{_name}
%defattr(644,root,root,755)
%{_libdir}/kde3/kwin3_domino.la
%attr(755,root,root) %{_libdir}/kde3/kwin3_domino.so
%{_libdir}/kde3/kwin_domino_config.la
%attr(755,root,root) %{_libdir}/kde3/kwin_domino_config.so
%{_datadir}/apps/kwin/domino.desktop

%files -n kde-colorscheme-%{_name}
%defattr(644,root,root,755)
%{_datadir}/apps/kdisplay/color-schemes/Domino.kcsrc

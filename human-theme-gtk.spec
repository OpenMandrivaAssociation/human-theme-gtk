Name:		human-theme-gtk
Version:	2.3.0
Release:	1
URL:           https://github.com/luigifab/human-theme
Source0:       %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Summary:	Human theme for GTK
License:	GPL-3.0-or-later AND LGPL-2.1-or-later AND CC-BY-SA-3.0
Group:		Themes/GTK

BuildArch:     noarch
BuildRequires: aspell-fr
Recommends:    dmz-cursor-themes
Recommends:    mate-icon-theme
Recommends:    gtk-murrine-engine

%description
Human theme for GTK that works with GTK 2.24 (with gtk-murrine-engine), GTK 3.24, and GTK 4.12. Intended for MATE and XFCE.


%prep
%setup -q -n human-theme-%{version}
sed -i 's/IconTheme=gnome/IconTheme=mate/g' src/*/index.theme

%install
install -dm 755 %{buildroot}%{_datadir}/themes/
cp -a src/human-theme/           %{buildroot}%{_datadir}/themes/
cp -a src/human-theme-blue/      %{buildroot}%{_datadir}/themes/
cp -a src/human-theme-green/     %{buildroot}%{_datadir}/themes/
cp -a src/human-theme-orange/    %{buildroot}%{_datadir}/themes/
install -Dpm 644 data/profile.sh %{buildroot}/etc/profile.d/%{name}.sh

%files
%config(noreplace) /etc/profile.d/%{name}.sh
%license LICENSE
%doc README.md
# the entire source code is GPL-3.0-or-later, except metacity-1/* which is LGPL-2.1-or-later,
# and gtk-2.0/* which is CC-BY-SA-3.0-or-later
%{_datadir}/themes/human-theme/
%{_datadir}/themes/human-theme-blue/
%{_datadir}/themes/human-theme-green/
%{_datadir}/themes/human-theme-orange/

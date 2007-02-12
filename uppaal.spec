Summary:	Environment for modeling, simulation and verification of real-time systems
Summary(pl.UTF-8):   Środowisko do modelowania, symulacji i weryfikacji systemów czasu rzeczywistego
Name:		uppaal
Version:	4.0.2
Release:	0.1
License:	free for non-profit (non-distributable)
Group:		Development/Tools
# http://www.docs.uu.se/docs/rtmv/uppaal/download.html
Source0:	%{name}-%{version}.zip
# NoSource0-md5:	6698f31403a6543d850e43d4a85025f4
NoSource:	0
URL:		http://www.uppaal.com/
BuildRequires:	unzip
Requires:	jre > 1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Uppaal is an integrated tool environment for modeling, validation and
verification of real-time systems modeled as networks of timed
automata, extended with data types (bounded integers, arrays, etc.).

%description -l pl.UTF-8
Uppaal to zintegrowane środowisko narzędzi do modelowania, sprawdzania
poprawności i weryfikacji systemów czasu rzeczywistego modelowanych
jako sieci automatów czasowych, rozszerzonych o typy danych
(ograniczone liczby całkowite, tablice itp.).

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/%{name}/{lib,demo,bin-Linux}}
install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name},%{_mandir}/man1}

install man/man1/* $RPM_BUILD_ROOT%{_mandir}/man1
install uppaal.jar $RPM_BUILD_ROOT%{_libdir}/%{name}
install demo/* $RPM_BUILD_ROOT%{_libdir}/%{name}/demo
install lib/* $RPM_BUILD_ROOT%{_libdir}/%{name}/lib
install bin-Linux/* $RPM_BUILD_ROOT%{_libdir}/%{name}/bin-Linux

cat <<EOF >$RPM_BUILD_ROOT%{_bindir}/uppaal
#!/bin/sh

JAR=%{_libdir}/%{name}/uppaal.jar
ENGINE=%{_libdir}/%{name}/bin-Linux
if [ "$DISPLAY" = ":0.0" ]; then
	java -jar \$JAR -enginePath \$ENGINE \$*
else
	java -jar \$JAR -enginePath \$ENGINE -antialias off \$*
fi
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt README
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/bin-Linux
%dir %{_libdir}/%{name}/demo
%dir %{_libdir}/%{name}/lib
%{_libdir}/%{name}/*.jar
%{_libdir}/%{name}/demo/*
%{_libdir}/%{name}/lib/*.jar
%attr(755, root, root) %{_libdir}/%{name}/bin-Linux/*
%{_mandir}/man1/*

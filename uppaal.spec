Summary:	Environment for modeling, simulation and verification of real-time systems
Summary(pl):	�rodowisko do modelowania, symulacji i weryfikacji system�w czasu rzeczywistego
Name:		uppaal
Version:	3.4.3
Release:	0.1
License:	free for non-profit (non-distributable)
Group:		Development/Tools
# http://www.docs.uu.se/docs/rtmv/uppaal/download.html
Source0:	uppaal2k.zip
# NoSource0-md5:	567d0ea89e0965e633ee0ce7d1987d42
NoSource:	0
URL:		http://www.uppaal.com/
BuildRequires:	unzip
Requires:	jre > 1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Uppaal is an integrated tool environment for modeling, validation and
verification of real-time systems modeled as networks of timed
automata, extended with data types (bounded integers, arrays, etc.).

%description -l pl
Uppaal to zintegrowane �rodowisko narz�dzi do modelowania, sprawdzania
poprawno�ci i weryfikacji system�w czasu rzeczywistego modelowanych
jako sieci automat�w czasowych, rozszerzonych o typy danych
(ograniczone liczby ca�kowite, tablice itp.).

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/%{name}/{lib,demo,bin-Linux}}
install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name},%{_mandir}/man1}

install man/man1/* $RPM_BUILD_ROOT%{_mandir}/man1
install uppaal2k.jar $RPM_BUILD_ROOT%{_libdir}/%{name}
install demo/* $RPM_BUILD_ROOT%{_libdir}/%{name}/demo
install lib/* $RPM_BUILD_ROOT%{_libdir}/%{name}/lib
install bin-Linux/* $RPM_BUILD_ROOT%{_libdir}/%{name}/bin-Linux

cat <<EOF >$RPM_BUILD_ROOT%{_bindir}/uppaal
#!/bin/sh

JAR=%{_libdir}/%{name}/uppaal2k.jar
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
%doc readme.txt README License-ASF
%attr(755,root,root) %{_bindir}/*
%{_libdir}/%{name}
%{_mandir}/man1/*

Name:		file_couner
Version:	1.0
Release:	1%{?dist}
Summary:	count regular files in /etc

License:	GPL
BuildArch:	noarch
Source0:	file_counter.tar.gz

%description
Simple bash script that counts regular files in /etc directory

%prep
%setup -q -c

%install
mkdir -p %{buildroot}/usr/local/bin
install -m 755 count_files.sh %{buildroot}/usr/local/bin/count_files.sh

%files
/usr/local/bin/count_files.sh

%changelog
* Sun Jan 18 2026 Mkols <mykols@email> - 1.0-1
- Initial RPM package


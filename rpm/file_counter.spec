Name:           file-counter
Version:        1.0
Release:        1%{?dist}
Summary:        Count regular files in /etc

License:        MIT
BuildArch:      noarch
Source0:        %{name}-%{version}.tar.gz

%description
Simple script to count regular files in /etc directory.

%prep
%setup -q

%build
# nothing to build

%install
mkdir -p %{buildroot}/usr/local/bin
install -m 755 count_files.sh %{buildroot}/usr/local/bin/file-counter

%files
/usr/local/bin/file-counter

%changelog
* Sun Jan 19 2026 Mykola <mykols@example.com> - 1.0-1
- Initial RPM release


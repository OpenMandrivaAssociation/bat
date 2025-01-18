# Generated by rust2rpm 13
# * assert_cmd is not packaged
%bcond_with check
%global __cargo_skip_build 0

%global crate bat

Name:           rust-%{crate}
Version:        0.25.0
Release:        1
Summary:        cat(1) clone with wings

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/bat
Source0:         https://github.com/sharkdp/bat/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.xz

BuildRequires:  rust-packaging

%global _description %{expand:
Cat(1) clone with wings.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE-MIT LICENSE-APACHE
%doc README.md
%{_bindir}/bat
%doc %{_mandir}/man1/bat.1*

%prep
%autosetup -n %{name}-%{version}  -p1 -a 1
%cargo_prep -v vendor
cat >>.cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF
%build
%cargo_build

%install
%cargo_install
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 \
  doc/bat.1

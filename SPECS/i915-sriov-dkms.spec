Summary:         Linux i915 module patched with SR-IOV support
Name:            i915-sriov-dkms
Version:         6.1.11
Release:         1
Source0:         https://github.com/sihawken/i915-sriov-dkms/archive/refs/tags/v6.1.11.tar.gz
License:         GPLv2
Group:           System Environment/Kernel
URL:             https://github.com/strongtz/i915-sriov-dkms
Requires(post):  dkms
Requires(preun): dkms
Requires:        kernel-devel
ExclusiveArch:   x86_64

%description
This package enables a new i915 driver from intel that supports SR-IOV.

%prep
%setup

%build

%install
# sources to be used by DKMS
mkdir -p %{buildroot}%{_usr}/src/%{name}-%{version}

cp -fr ./* %{buildroot}%{_usrsrc}/%{name}-%{version}/

%post
dkms --rpm_safe_upgrade add -m %{dkms_name} -v %{version} -k $(rpm -qa kernel --queryformat '%{VERSION}-%{RELEASE}.%{ARCH}') -q || :
dkms --rpm_safe_upgrade build -m %{dkms_name} -v %{version} -k $(rpm -qa kernel --queryformat '%{VERSION}-%{RELEASE}.%{ARCH}') -q || :
dkms --rpm_safe_upgrade install -m %{dkms_name} -v %{version} -k $(rpm -qa kernel --queryformat '%{VERSION}-%{RELEASE}.%{ARCH}') -q --force || :

%preun
dkms --rpm_safe_upgrade remove 

%files
%dir %{_usr}/src/%{name}-%{version}
%{_usr}/src/%{name}-%{version}/*

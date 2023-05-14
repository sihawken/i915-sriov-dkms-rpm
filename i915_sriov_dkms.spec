
Summary:         Linux i915 module patched with SR-IOV support
Name:            i915_sriov_dkms
Version:         6.1.11
Release:         1
Source0:         https://github.com/sihawken/i915-sriov-dkms/archive/refs/tags/v6.1.11.tar.gz
License:         GPLv2
Group:           System Environment/Kernel
URL:             https://github.com/strongtz/i915-sriov-dkms
Requires(post):  dkms
Requires(preun): dkms
Requires:        kernel-devel
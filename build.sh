mkdir BUILD
mkdir BUILDROOT
mkdir RPMS
mkdir SOURCES
mkdir SRPMS
rpmbuild --undefine=_disable_source_fetch -bb SPECS/i915_sriov_dkms.spec
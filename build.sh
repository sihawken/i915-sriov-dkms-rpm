mkdir BUILD
mkdir BUILDROOT
mkdir RPMS
mkdir SOURCES
mkdir SRPMS
rpmbuild --undefine=_disable_source_fetch -ba SPECS/i915-sriov-dkms.spec
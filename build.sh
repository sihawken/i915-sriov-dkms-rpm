#!/usr/bin/env bash

set -oue pipefail
mkdir -p ../{BUILD,BUILDROOT,RPMS,SOURCES,SRPMS}
wget https://github.com/sihawken/i915-sriov-dkms/archive/refs/tags/v6.1.11.tar.gz -O ./SOURCES/v6.1.11.tar.gz
rpmbuild --define "_topdir `pwd`" -ba SPECS/i915-sriov-dkms.spec

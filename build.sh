#!/usr/bin/env bash

set -oue pipefail
mkdir -p ../{BUILD,BUILDROOT,RPMS,SOURCES,SRPMS}

rpmbuild --define "_topdir `pwd`" --undefine=_disable_source_fetch -ba SPECS/i915-sriov-dkms.spec

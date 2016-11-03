Name: pcs		
Version: 0.9.152
Release: 10%{?dist}
License: GPLv2
URL: https://github.com/ClusterLabs/pcs
Group: System Environment/Base
Summary: Pacemaker Configuration System	
#building only for architectures with pacemaker and corosync available
ExclusiveArch: i686 x86_64 s390x
#part after last slash is recognized as filename in look-aside repository
#desired name is achived by trick with hash anchor
Source0: %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: HAM-logo.png
Source2: pcsd-bundle-config-1
Source3: https://rubygems.org/downloads/backports-3.6.8.gem
Source4: https://rubygems.org/downloads/eventmachine-1.2.0.1.gem
Source5: https://rubygems.org/downloads/multi_json-1.12.0.gem
Source6: https://rubygems.org/downloads/open4-1.3.4.gem
Source7: https://rubygems.org/downloads/orderedhash-0.0.6.gem
Source8: https://rubygems.org/downloads/rack-protection-1.5.3.gem
Source9: https://rubygems.org/downloads/rack-test-0.6.3.gem
Source10: https://rubygems.org/downloads/rack-1.6.4.gem
Source11: https://rubygems.org/downloads/rpam-ruby19-1.2.1.gem
Source12: https://rubygems.org/downloads/sinatra-contrib-1.4.7.gem
Source13: https://rubygems.org/downloads/sinatra-1.4.7.gem
Source14: https://rubygems.org/downloads/tilt-2.0.3.gem
Source15: https://github.com/testing-cabal/mock/archive/1.0.1.tar.gz#/mock-1.0.1.tar.gz

Patch0: bz1315371-01-add-support-for-pacemaker-alerts.patch
Patch1: bz1158805-01-add-support-for-qdevice-qnetd-provided-.patch
Patch2: bz1164402-01-sbd-fix-call_node-calls-on-python3.patch
Patch3: bz1346852-01-fix-bad-request-when-resource-removal-t.patch
Patch4: bz1327739-01-add-pcs-quorum-expected-votes-command.patch
Patch5: bz1348579-01-add-a-wrapper-for-holding-SELinux-conte.patch
Patch6: bz1349465-01-allow-to-specify-bash-completion-install-dir.patch
Patch7: fix-qdevice-tests-failing-due-to-multithreading.patch
Patch8: bz1281364-01-gui-add-constraint-colocation-set-support.patch
Patch9: bz1269242-01-fix-displaying-cluster-config-when-cib-is-provided-a.patch
Patch10: bz1353607-01-tests-use-safe-node-names.patch
Patch11: bz1315371-02-use-recipient-id-as-identifier-instead-of-its-value.patch
Patch12: bz1158805-01-cli-improve-quorum-device-commands-syntax.patch
Patch13: bz1289418-01-fixes-for-pcs-cli-running-on-a-remote-node.patch
Patch14: pcsd-fix-syntax-error-on-ruby-1.8.patch
Patch15: bz1348579-02-fix-traceback-when-stopping-pcsd-shortly-after-start.patch
Patch16: bz1225423-01-allow-to-remove-a-dead-node-from-a-cluster.patch
Patch17: bz1357945-01-add-support-for-clufter-s-dist-parameter.patch
Patch18: bz1302010-01-fix-filter-by-property-name-in-pcs-property-show.patch
Patch19: bz1301993-01-improve-node-properties-commands.patch
Patch20: bz1346852-02-web-UI-fix-error-when-removing-resources-takes-long.patch
Patch21: bz1231858-01-web-UI-fix-occasional-issue-with-not-showing-optiona.patch
Patch22: bz1315371-03-improve-alerts-help.patch
Patch23: bz1346852-03-web-UI-correct-handling-of-timeout-when-removing-mul.patch
Patch24: bz1303136-01-fix-check-if-id-exists-in-cib.patch
Patch25: bz1329472-01-when-removing-a-remote-node-remove-it-from-pacemakers-caches-as-well.patch
Patch26: test-fix-an-occasional-multithread-test-fail.patch
Patch27: bz1359154-01-fix-exceptions-when-authenticating-cluster-nodes.patch
Patch28: bz1231858-02-web-UI-don-t-change-current-resource-in-URL-if-not-i.patch
Patch29: bz1349465-02-install-bash-completion-with-standard-permissions.patch
Patch30: bz1357945-02-doc-fixes-regarding-clufter.patch
Patch31: bz1281391-01-web-UI-add-possibility-to-change-order-of-resources-.patch
Patch32: bz1264360-01-web-UI-add-support-for-unmanaged-resources.patch
Patch33: bz1308514-01-add-booth-support.patch
Patch34: bz1298585-01-add-possibility-to-hide-inactive-resources-in-pcs-resource-show.patch
Patch35: bz1354498-01-handle-exceptions-when-waiting-for-response-from-user.patch
Patch36: bz1346852-04-fix-detecting-nonexisting-resources-in-pcsd.patch
Patch37: bz1164402-02-sbd-fixes.patch
Patch38: bz1315371-04-alerts-related-fixes.patch
Patch39: bz1366307-01-web-ui-fix-bad-using-of-html-ids.patch
Patch40: bz1247088-01-fix-error-message-in-node-maintenanceunmaintenance-commands.patch
Patch41: bz1308514-02-booth-support-improvements.patch
Patch42: bz1164402-03-sbd-fix-check-if-atb-is-required-when-enabling-sbd.patch
Patch43: bz1264360-02-web-ui-change-way-of-displaying-status-of-unmanaged-primitive-resources.patch
Patch44: test-corrections.patch
Patch45: bz1158805-02-add-support-for-qdeviceqnetd-provided-by-corosync.patch
Patch46: bz1308514-03-wider-support-for-booth-configuration-beside-mere.patch
#forgotten patch (chronologically should be before Patch0
Patch47: fix-pcs-constraint-ticket-set-help.patch
Patch48: bz1305049-01-pcs-does-not-support-ticket-constraints.patch
Patch49: bz1158500-01-add-support-for-utilization-attributes.patch
Patch50: bz1281391-02-web-ui-reset-selected-group-when-displaying-new-resource-dialog.patch
Patch51: bz1231858-03-resourcefence-agent-options-form-needs-an-overhau.patch
Patch52: bz1158805-03-add-support-for-qdeviceqnetd-provided-by-corosync.patch
Patch53: bz1305049-02-pcs-does-not-support-ticket-constraints.patch
Patch54: rhel7.patch
Patch55: change-cman-to-rhel6-in-messages.patch
Patch56: show-only-warning-when-crm_mon-xml-is-invalid.patch

BuildRequires: python2-devel python-setuptools
BuildRequires: gcc gcc-c++
BuildRequires: ruby >= 2.0.0 ruby-devel rubygems pam-devel git
BuildRequires: rubygem-json
BuildRequires: systemd-units rubygem-bundler
BuildRequires: rubygem-minitest
# following for UpdateTimestamps sanitization function
BuildRequires: diffstat
#following BuildRequires are needed by tests
BuildRequires: python-lxml
BuildRequires: corosync
BuildRequires: pacemaker
BuildRequires: pacemaker-cli
BuildRequires: fence-agents-all

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Requires: corosync pacemaker pacemaker-cli
Requires: psmisc openssl
Requires: python-lxml
Requires: python-setuptools
Requires: python-clufter >= 0.59.0
Requires: ruby >= 2.0.0
Requires: rubygem-json

Provides: bundled(rubygem-backports) = 3.6.8
Provides: bundled(rubygem-eventmachine) = 1.2.0.1
Provides: bundled(rubygem-multi_json) = 1.12.0
Provides: bundled(rubygem-open4) = 1.3.4
Provides: bundled(rubygem-orderedhash) = 0.0.6
Provides: bundled(rubygem-rack) = 1.6.4
Provides: bundled(rubygem-rack-protection) = 1.5.3
Provides: bundled(rubygem-rack-test) = 0.6.3
Provides: bundled(rubygem-rpam-ruby19) = 1.2.1
Provides: bundled(rubygem-sinatra) = 1.4.7
Provides: bundled(rubygem-sinatra-contrib) = 1.4.7
Provides: bundled(rubygem-tilt) = 2.0.3

%description
pcs is a corosync and pacemaker configuration tool.  It permits users to
easily view, modify and created pacemaker based clusters.

%define PCS_PREFIX /usr
%prep
%autosetup -p1 -S git

# -- following borrowed from python-simplejon.el5 --
# Update timestamps on the files touched by a patch, to avoid non-equal
# .pyc/.pyo files across the multilib peers within a build, where "Level"
# is the patch prefix option (e.g. -p1)
UpdateTimestamps() {
  Level=$1
  PatchFile=$2
  # Locate the affected files:
  for f in $(diffstat $Level -l $PatchFile); do
    # Set the files to have the same timestamp as that of the patch:
    touch -r $PatchFile $f
  done
}
UpdateTimestamps -p1 %{PATCH0}
UpdateTimestamps -p1 %{PATCH1}
UpdateTimestamps -p1 %{PATCH2}
UpdateTimestamps -p1 %{PATCH3}
UpdateTimestamps -p1 %{PATCH4}
UpdateTimestamps -p1 %{PATCH5}
UpdateTimestamps -p1 %{PATCH6}
UpdateTimestamps -p1 %{PATCH7}
UpdateTimestamps -p1 %{PATCH8}
UpdateTimestamps -p1 %{PATCH9}
UpdateTimestamps -p1 %{PATCH10}
UpdateTimestamps -p1 %{PATCH11}
UpdateTimestamps -p1 %{PATCH12}
UpdateTimestamps -p1 %{PATCH13}
UpdateTimestamps -p1 %{PATCH14}
UpdateTimestamps -p1 %{PATCH15}
UpdateTimestamps -p1 %{PATCH16}
UpdateTimestamps -p1 %{PATCH17}
UpdateTimestamps -p1 %{PATCH18}
UpdateTimestamps -p1 %{PATCH19}
UpdateTimestamps -p1 %{PATCH20}
UpdateTimestamps -p1 %{PATCH21}
UpdateTimestamps -p1 %{PATCH22}
UpdateTimestamps -p1 %{PATCH23}
UpdateTimestamps -p1 %{PATCH24}
UpdateTimestamps -p1 %{PATCH25}
UpdateTimestamps -p1 %{PATCH26}
UpdateTimestamps -p1 %{PATCH27}
UpdateTimestamps -p1 %{PATCH28}
UpdateTimestamps -p1 %{PATCH29}
UpdateTimestamps -p1 %{PATCH30}
UpdateTimestamps -p1 %{PATCH31}
UpdateTimestamps -p1 %{PATCH32}
UpdateTimestamps -p1 %{PATCH33}
UpdateTimestamps -p1 %{PATCH34}
UpdateTimestamps -p1 %{PATCH35}
UpdateTimestamps -p1 %{PATCH36}
UpdateTimestamps -p1 %{PATCH37}
UpdateTimestamps -p1 %{PATCH38}
UpdateTimestamps -p1 %{PATCH39}
UpdateTimestamps -p1 %{PATCH40}
UpdateTimestamps -p1 %{PATCH41}
UpdateTimestamps -p1 %{PATCH42}
UpdateTimestamps -p1 %{PATCH43}
UpdateTimestamps -p1 %{PATCH44}
UpdateTimestamps -p1 %{PATCH45}
UpdateTimestamps -p1 %{PATCH46}
UpdateTimestamps -p1 %{PATCH47}
UpdateTimestamps -p1 %{PATCH48}
UpdateTimestamps -p1 %{PATCH49}
UpdateTimestamps -p1 %{PATCH50}
UpdateTimestamps -p1 %{PATCH51}
UpdateTimestamps -p1 %{PATCH52}
UpdateTimestamps -p1 %{PATCH53}
UpdateTimestamps -p1 %{PATCH54}

cp -f %SOURCE1 pcsd/public/images

mkdir -p pcsd/.bundle
cp -f %SOURCE2 pcsd/.bundle/config

mkdir -p pcsd/vendor/cache
#copy ruby gems
cp -f %SOURCE3 pcsd/vendor/cache
cp -f %SOURCE4 pcsd/vendor/cache
cp -f %SOURCE5 pcsd/vendor/cache
cp -f %SOURCE6 pcsd/vendor/cache
cp -f %SOURCE7 pcsd/vendor/cache
cp -f %SOURCE8 pcsd/vendor/cache
cp -f %SOURCE9 pcsd/vendor/cache
cp -f %SOURCE10 pcsd/vendor/cache
cp -f %SOURCE11 pcsd/vendor/cache
cp -f %SOURCE12 pcsd/vendor/cache
cp -f %SOURCE13 pcsd/vendor/cache
cp -f %SOURCE14 pcsd/vendor/cache
#ruby gems copied

%build

%install
rm -rf $RPM_BUILD_ROOT
pwd
make install \
  DESTDIR=$RPM_BUILD_ROOT \
  PYTHON_SITELIB=%{python_sitelib} \
  PREFIX=%{PCS_PREFIX} \
  BASH_COMPLETION_DIR=$RPM_BUILD_ROOT/usr/share/bash-completion/completions
make install_pcsd \
  DESTDIR=$RPM_BUILD_ROOT \
  PYTHON_SITELIB=%{python_sitelib} \
  hdrdir="%{_includedir}" \
  rubyhdrdir="%{_includedir}" \
  includedir="%{_includedir}" \
  PREFIX=%{PCS_PREFIX}

%check
run_all_tests(){
  #prepare environmet for tests
  sitelib=$RPM_BUILD_ROOT%{python_sitelib}
  pcsd_dir=$RPM_BUILD_ROOT%{PCS_PREFIX}/lib/pcsd

  #run pcs tests and remove them, we do not distribute them in rpm
  #python2-mock package is required but is only in epel so we will install it
  #manually
  #we do not have permissions to write anywhere else than $RPM_BUILD_ROOT
  #so we must install python2-mock there
  #disabled tests:
  #pcs.test.test_lib_external.ParallelCommunicationHelperTest.test_success \
  #   File "/builddir/build/BUILDROOT/pcs-0.9.152-5.el7.x86_64/usr/lib/python2.7/site-packages/pcs/test/test_lib_external.py", line 865, in test_success
  #     func.assert_has_calls(expected_calls)...
  # Expected: [call(0, a=0), call(1, a=2), call(2, a=4)]
  # Actual: [call(1, a=2), call(0, a=0), call(2, a=4)]
  #
  #pcs.lib.booth.test.test_env.SetKeyfileAccessTest.test_set_desired_file_access \
  # Traceback (most recent call last):
  #   File "/builddir/build/BUILDROOT/pcs-0.9.152-6.el7.x86_64/usr/lib/python2.7/site-packages/pcs/lib/booth/test/test_env.py", line 148, in test_set_desired_file_access
  #     env.set_keyfile_access(file_path)
  #   File "/builddir/build/BUILDROOT/pcs-0.9.152-6.el7.x86_64/usr/lib/python2.7/site-packages/pcs/lib/booth/env.py", line 63, in set_keyfile_access
  #     raise report_keyfile_io_error(file_path, "chown", e)
  # LibraryError: ERROR FILE_IO_ERROR: {u'reason': u"Operation not permitted: '/builddir/build/BUILDROOT/pcs-0.9.152-6.el7.x86_64/usr/lib/python2.7/site-packages/pcs/test/resources/temp-keyfile'", u'file_role': u'BOOTH_KEY', u'file_path': u'/builddir/build/BUILDROOT/pcs-0.9.152-6.el7.x86_64/usr/lib/python2.7/site-packages/pcs/test/resources/temp-keyfile', u'operation': u'chown'}

  export PYTHONPATH="${PYTHONPATH}:${sitelib}"
  easy_install -d ${sitelib} %SOURCE15
  python ${sitelib}/pcs/test/suite.py -v --no-color --all-but \
    pcs.test.test_resource.ResourceTest.testAddResources \
    pcs.test.test_cluster.ClusterTest.testUIDGID \
    pcs.test.test_utils.RunParallelTest.test_wait_for_slower_workers \
    pcs.test.test_stonith.StonithTest.test_stonith_create_provides_unfencing \
    pcs.test.test_lib_external.ParallelCommunicationHelperTest.test_success \
    pcs.lib.booth.test.test_env.SetKeyfileAccessTest.test_set_desired_file_access \

  test_result_python=$?

  find ${sitelib}/pcs -name test -type d -print0|xargs -0 rm -r -v --
  #we installed python2-mock inside $RPM_BUILD_ROOT and now we need to remove
  #it because it does not belong into pcs package
  #easy_install does not provide uninstall and pip is not an option (is in
  #epel) so it must be cleaned manually
  rm -v ${sitelib}/easy-install.pth
  rm -v ${sitelib}/mock-1.0.1-py2.7.egg
  rm -v ${sitelib}/site.py
  rm -v ${sitelib}/site.pyc


  #run pcsd tests and remove them
  GEM_HOME=${pcsd_dir}/vendor/bundle/ruby ruby \
    -I${pcsd_dir} \
    -I${pcsd_dir}/test \
    ${pcsd_dir}/test/test_all_suite.rb
  test_result_ruby=$?
  #remove tests after use here to be symmetrical with pcs tests
  rm -r -v ${pcsd_dir}/test

  if [ $test_result_python -ne 0 ]; then
    return $test_result_python
  fi
  return $test_result_ruby
}

run_all_tests

%post
%systemd_post pcsd.service

%preun
%systemd_preun pcsd.service

%postun
%systemd_postun_with_restart pcsd.service

%files
%{python_sitelib}/pcs
%{python_sitelib}/pcs-%{version}-py2.*.egg-info
/usr/sbin/pcs
/usr/lib/pcsd/*
/usr/lib/pcsd/.bundle/config
/usr/lib/systemd/system/pcsd.service
/usr/share/bash-completion/completions/pcs
/var/lib/pcsd
/etc/pam.d/pcsd
/etc/logrotate.d/pcsd
%dir /var/log/pcsd
%config(noreplace) /etc/sysconfig/pcsd
%ghost %config(noreplace) /var/lib/pcsd/cfgsync_ctl
%ghost %config(noreplace) /var/lib/pcsd/pcsd.cookiesecret
%ghost %config(noreplace) /var/lib/pcsd/pcsd.crt
%ghost %config(noreplace) /var/lib/pcsd/pcsd.key
%ghost %config(noreplace) /var/lib/pcsd/pcs_settings.conf
%ghost %config(noreplace) /var/lib/pcsd/pcs_users.conf
%ghost %config(noreplace) /var/lib/pcsd/tokens
%{_mandir}/man8/pcs.*
%exclude /usr/lib/pcsd/*.debian
%exclude /usr/lib/pcsd/pcsd.service
%exclude /usr/lib/pcsd/pcsd.conf
%exclude %{python_sitelib}/pcs/bash_completion.sh
%exclude %{python_sitelib}/pcs/pcs.8
%exclude %{python_sitelib}/pcs/pcs

%doc COPYING README

%changelog
* Tue Sep 20 2016 Ivan Devat <idevat@redhat.com> - 0.9.152-10
- Fixed error when stopping qdevice if is not running
- Fixed removing qdevice from a cluster
- Fixed documentation regarding booth
- Fixed return code when no matching ticket constraint found during remove
- Resolves: rhbz#1158805 rhbz#1305049

* Wed Sep 14 2016 Ivan Devat <idevat@redhat.com> - 0.9.152-9
- Added warning when stopping/destroying qdevice instance which is being used 
- Fiexed removing qdevice from a cluster which uses sbd
- Fixed re-running "pcs cluster node add" if it failed due to qdevice
- Fixed documentation regarding booth
- Added warning when using unknown booth ticket option
- Added constraint ticket remove command
- Fixed return code and message when displaying node utilization for nonexistent node
- Fixed setting utilization attributes in web UI
- Fixed support for node utilization on remote node
- Fixed updating of selected group when displaying new resource dialog
- Fixed group list when managing cluster running older pcs in web UI 
- Fixed displaying unmanaged status for resources for older pcs in web UI
- Fixed clone/master/unclone group/ungroup buttons for older pcs in web UI
- Fixed node standby/unstandby for older pcs in web UI
- Resolves: rhbz#1158805 rhbz#1308514 rhbz#1305049 rhbz#1158500 rhbz#1231858

* Wed Aug 31 2016 Ivan Devat <idevat@redhat.com> - 0.9.152-8
- Fixed error message in node maintenance/unmaintenance commands
- Fixed missing line at the end of booth config 
- Fixed documentation regarding booth
- Fixed remove multiple booth resources with "--force" flag
- Fixed cleanup of ip resource if it fails to create booth resource
- Added bash completion for booth
- Fixed display full booth configuration
- Added ability to display booth config from remote node
- Added support for ticket options during adding booth ticket
- Fixed adding node to cluster when booth is not installed
- Added restart command for booth
- Fixed check if auto_tie_breaker is required when enabling sbd
- Improved way of displaying status of unmanaged primitive resources in web UI
- Resolves: rhbz#1247088 rhbz#1308514 rhbz#1164402 rhbz#1264360

* Fri Aug 19 2016 Ivan Devat <idevat@redhat.com> - 0.9.152-7
- Added possibility to hide inactive resources in "pcs resource show" command
- Fixed exceptions handling when waiting for response from user in command line
- Fixed nonexisting resource detection in pcsd
- Fixed SBD_WATCHDOG_TIMEOUT option value validation
- Removed possibility to change SBD_PACEMAKER
- Fixed exception when disabling service on systemd systems
- Added automatic auto_tie_breaker quorum option set whenever it is needed for SBD to work
- Fixed setting sbd watchdog in config
- Fixed error handling when upgrading cib schema
- Improved consistency of syntax 'pcs alert recipient add' command
- Resolves: rhbz#1298585 rhbz#1354498 rhbz#1346852 rhbz#1164402 rhbz#1315371 rhbz#1366307

* Fri Aug 05 2016 Ivan Devat <idevat@redhat.com> - 0.9.152-6
- Fixed documentation regarding clufter
- Added possibility to change order of resources in a group in web UI
- Added support for unmanaged resources in web UI
- Added support for booth (cluster ticket manager)
- Resolves: rhbz#1357945 rhbz#1281391 rhbz#1264360 rhbz#1308514

* Thu Jul 28 2016 Ivan Devat <idevat@redhat.com> - 0.9.152-5
- Fixed traceback when stopping pcsd shortly after start
- Fixed removing a dead node from a cluster
- Added support for clufter's 'dist' parameter
- Fixed filtering by property name in "pcs property show"
- Fixed an error in web UI when removing resources takes a long time
- Fixed occasional missing optional arguments of resources in web UI
- Improved help for alerts
- Fixed recreating a remote node resource
- Fixed exceptions when authenticating cluster nodes
- Fixed permissions for bash completion file
- Resolves: rhbz#1348579 rhbz#1225423 rhbz#1357945 rhbz#1302010 rhbz#1301993 rhbz#1346852 rhbz#1231858 rhbz#1315371 rhbz#1303136 rhbz#1329472 rhbz#1359154 rhbz#1349465

* Fri Jul 15 2016 Ivan Devat <idevat@redhat.com> - 0.9.152-4
- Added colocation constraint support in web UI
- Fixed displaying cluster config when cib is provided as a file
- Removed side effect on /etc/hosts during build
- Recipient id is used as identifier in alarms
- Improved quorum device commands syntax
- Fixed pcs client for running on a remote node
- Resolves: rhbz#1281364 rhbz#1269242 rhbz#1353607 rhbz#1315371 rhbz#1158805 rhbz#1289418

* Fri Jul 01 2016 Ivan Devat <idevat@redhat.com> - 0.9.152-3
- Added support for pacemaker alerts
- Added support for qdevice/qnetd provided by corosync
- Fixed sbd calls on python3
- Fixed bad request when resource removal takes longer than pcs expects
- Added support for set expected votes on a live cluster
- Added a wrapper for holding SELinux context when pcsd is started by systemd
- Resolves: rhbz#1315371 rhbz#1158805 rhbz#1164402 rhbz#1346852 rhbz#1327739 rhbz#1348579 rhbz#1349465

* Wed Jun 22 2016 Ivan Devat <idevat@redhat.com> - 0.9.152-2
- Specified achitectures matching with pacemaker and corosync
- Resolves: rhbz#1299847

* Tue Jun 21 2016 Ivan Devat <idevat@redhat.com> - 0.9.152-1
- Rebased to latest upstream sources
- Added support for sbd configuration
- Added support for constraint tickets in web UI
- Added warning to pcs quorum unblock command
- Fixes in manpage and built-in help
- Config files marked as config
- Resolves: rhbz#1299847 rhbz#1164402 rhbz#1305049 rhbz#1264566 rhbz#1225946 rhbz#1231858 rhbz#1328066 rhbz#1341114

* Fri Jun 03 2016 Ivan Devat <idevat@redhat.com> - 0.9.151-2
- Added missing requirements for python-setuptools
- Resolves: rhbz#1299847

* Tue May 31 2016 Ivan Devat <idevat@redhat.com> - 0.9.151-1
- Rebased to latest upstream sources
- Added support for utilization attributes
- Optimized pcs status command
- Fixes in manpage and built-in help
- Improved resource cleanups
- Added --wait support for cluster start and node standby commands
- Improved resource and fence agent options in web UI
- Added ability to put a node into maintenance mode
- Fixed adding acl permission when targed id does not exists
- Fixed deleting resource when referenced in acl
- Improved pcsd launch script
- Added automatically setting provides=unfencing meta attribute for stonith device
- Improved Cluster Properties page in web UI
- Fixed page update after adding group in web UI
- Fixed deleting group (clones) when managing older cluster in web UI
- Fixed stonith update command when fence agents fails to get metadata
- Added support for putting Pacemaker Remote nodes into standby
- Added support for omission stopped resources in status command
- Added login input sanitization in web UI
- Added config settings for SSL options and ciphers
- Improved resource update command to inform user about missused op settings
- Spec file fixes
- Added support for constraint tickets from command line
- Fixed CVE-2016-0720 pcs: Cross-Site Request Forgery in web UI
- Fixed CVE-2016-0721 pcs: cookies are not invalidated upon logout
- Resolves: rhbz#1299847 rhbz#1158500 rhbz#1207405 rhbz#1219581 rhbz#1225946 rhbz#1220512 rhbz#1229822 rhbz#1231858 rhbz#1247088 rhbz#1248990 rhbz#1249085 rhbz#1252050 rhbz#1262773 rhbz#1281371 rhbz#1283562 rhbz#1286664 rhbz#1287320 rhbz#1290512 rhbz#1298585 rhbz#1305786 rhbz#1315652 rhbz#1321021 rhbz#1315743 rhbz#1315357 rhbz#1305049 rhbz#1335779 rhbz#1330884

* Wed Oct 21 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.143-15
- Fixed setting cluster properties in web UI
- Resolves: rhbz#1272412

* Wed Oct 07 2015 Chris Feist <cfeist@redhat.com> - 0.9.143-14
- Fixed remaining issues when managing resources/groups/etc. that were
  previously unmanaged
- Resolves: rhbz#1268801

* Tue Oct 06 2015 Chris Feist <cfeist@redhat.com> - 0.9.143-12
- Fixed issue managing resources that were clones and had the unmanaged
  meta attribute set under the clone/master
- Resolves: rhbz#1268801

* Wed Sep 23 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.143-11
- Fix for crm_node -l output change
- Resolves: rhbz#1265425

* Tue Sep 22 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.143-10
- Web UI fixes
- Added more detailed warnings for 'pcs stonith confirm'
- Resolves: rhbz#1189857 rhbz#1245264

* Wed Sep 16 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.143-9
- Multiple fixes in web UI (dashboard, nodes, resources, fence devices)
- Fixed an authentication issue in web UI
- Port parameter of fence agents is now considered optional
- Resolves: rhbz#1158566 rhbz#1188361 rhbz#1189857

* Tue Sep 08 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.143-8
- Fixes in loading cluster status for web UI
- Fixed checking user/group membership
- Fixed a typo in an error message
- Resolves: #rhbz1158566 #rhbz1158569 #rhbz1158571

* Mon Sep 07 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.143-7
- Multiple fixes in web UI
- Fixed crash on missing nagios agents metadata
- Check user/group membership on each request
- Print output of crm_resource in pcs resource cleanup
- Resolves: #rhbz1158571 #rhbz1189857 #rhbz1235022 #rhbz1257369

* Tue Sep 01 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.143-6
- Added missing dependency on openssl
- Resolves: #rhbz1158577

* Tue Sep 01 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.143-5
- Fixed pcsd certificates synchronization
- Multiple fixes in web UI
- Resolves: #rhbz1158566 #rhbz1158577 #rhbz1189857

* Mon Aug 31 2015 Chris Feist <cfeist@redhat.com> - 0.9.143-4
- Fixed issue causing traceback on pcsd stop
- Resolves: #rhbz#1258619

* Wed Aug 26 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.143-3
- Fixed relocation of remote nodes to their optimal node
- Fixed pcs/pcsd path detection
- Fixed command injection vulnerability
- Resolves: #rhbz1122818 #rhbz1253294 #rhbz1253491

* Fri Aug 14 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.143-2
- Fixed relocation of unique clone resources to their optimal node
- Improved logging of node to node communication
- Fixed 'Add resource' form in web UI
- Fixed support for nagios agents
- Resolves: rhbz#1122818 rhbz#1158577 rhbz#1189857 rhbz#1235022

* Mon Aug 10 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.143-1
- Added support for setting permissions for users and groups to clusters managed by web UI
- Resources are now displayed in a tree (clone, master/slave, group, primitive) in web UI
- Renamed 'pcs resource relocate clean' command to 'pcs resource relocate clear'
- Improved logging of config files synchronization
- Various fixes in Resources tab in web UI
- Added missing dependecy on initscripts to the spec file
- Fixed traceback when running 'pcs resource enable clvmd --wait'
- Resolves: rhbz#1122818 rhbz#1158571 rhbz#1158577 rhbz#1182119 rhbz#1189857 rhbz#1198640 rhbz#1219574 rhbz#1243579 rhbz#1247818 rhbz#1250720

* Fri Jul 10 2015 Chris Feist <cfeist@redhat.com> - 0.9.142-2
- Cleaned up tarball

* Thu Jul 09 2015 Chris Feist <cfeist@redhat.com> - 0.9.142-1
- Rebase to latest upstream sources
- Added ability to set hostname when using IP address to create a cluster
- Added ability to clear out tokens with pcs pcsd clear-auth
- Added ability to use nagios agents
- Fixed issue with orphaned resources causing GUI to fail to work properly
- More dashboard fixes
- Synchronize files between pcsd instances in a cluster to allow for HA pcsd
- ACL role fixes for pcs/pcsd
- Resolves: rhbz#118310 rhbz#1207805 rhbz#1235022 rhbz#1198222 rhbz#1158566 rhbz#1158577 rhbz#1166160

* Tue Jun 23 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.141-1
- Rebased to latest upstream packages
- Added a command to relocate resources to their preferred host
- Fixed the dashboard in web UI
- Configure corosync to log to a file
- Added warning when creating a duplicate resource operation
- Added support for debugging resource agents
- Do not automatically use --force when removing a resource using web UI
- Fixed pcsd communication when one of the nodes is not authenticated
- Updated ruby gems
- Spec file fixes
- Resolves: rhbz#1198265 rhbz#1122818 rhbz#1158566 rhbz#1163671 rhbz#1175400 rhbz#1185096 rhbz#1198274 rhbz#1213429 rhbz#1231987 rhbz#1232644 rhbz#1233574

* Wed Jun 03 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.140-1
- Rebased to latest upstream packages
- Added a note to man page and help poiting to cluster properties description
- Fixed parsing of the corosync.conf file
- Fixed diferences between the 'pcs cluster status' and 'pcs status cluster' commands as one is documented to be an alias of the other
- Do not remove constraints referencing a group when removing a resource from the group
- Added dashboard showing status of clusters to web UI
- Added node authentication dialog to web UI
- Added synchronization of web UI configuration files across cluster nodes
- Fixed node authentication when one of the nodes is unreachable
- Fixed an error message in the 'pcs config restore' command if a node is not authenticated
- Fixed parsing of 'pcs acl role create' command's parameters
- Properly overwrite a tokens file if its contents is unparsable
- The 'pcs config' command now displays resources defaults and operations defaults
- Show a useful error message when attempting to add a duplicate fence level in web UI
- Added the require-all parameter to ordering constraints listing
- Fixed VirtualDomain resource removal when there are constraints for the resource
- Added a warning when removing a cluster node may cause a loss of the quorum
- Fixed an error when uncloning a non-cloned resource
- Fixed an error when removing a resource from a cloned group
- Fixed waiting for resource commands to finish
- Fixed 'pcs cluster start' and similar commands when run under a non-root account
- Fixed parsing of 'pcs constraint order set' command's parameters
- Fixed an error when creating a resource with an id which already exists
- Improved man page and help for the 'pcs resource move' and 'pcs resource ban' commands
- Fixed an error when referencing a non-existing acl role in 'pcs acl' commands
- Fixed an error when adding an invalid stonith level
- Fixed constraints removal and node standby / unstandby using remote web UI
- Fixed formatting of resource / fence agent description
- Fence agent description now contains information about the agent
- The 'pcs status --full' command now displays node attributes and migration summary
- Clufter moved to a standalone package
- Fixed pcsd communication when one of the nodes is not authenticated
- Fixed a timeout value in the fence_xvm agent form
- Fixed the 'pcs resource enable' command when working with clones and multi-state resources
- Resolves: rhbz#1198265 rhbz#1121791 rhbz#1134426 rhbz#1158491 rhbz#1158537 rhbz#1158566 rhbz#1158569 rhbz#1158577 rhbz#1163682 rhbz#1165803 rhbz#1166160 rhbz#1170205 rhbz#1176687 rhbz#1182793 rhbz#1182986 rhbz#1183752 rhbz#1186692 rhbz#1187320 rhbz#1187571 rhbz#1188571 rhbz#1196412 rhbz#1197758 rhbz#1199073 rhbz#1201452 rhbz#1202457 rhbz#1204880 rhbz#1205653 rhbz#1206214 rhbz#1206219 rhbz#1206223 rhbz#1212904 rhbz#1213429 rhbz#1215198 rhbz#1218979

* Tue Jun 02 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.137-16
- Fixes cluster property name validation
- Resolves: rhbz#1218478

* Wed Apr 15 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.137-15
- Fixes issues with cookie signing in pcsd
- Resolves: rhbz#1211568

* Mon Mar 09 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.137-14
- Do not set two_nodes=1 in corosync.conf when auto_tie_breaker=1 is set
- Resolves: rhbz#1197770

* Tue Jan 20 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.137-13
- Keep cluster quorate during destruction as long as possible
- Resolves: rhbz#1180506

* Mon Jan 19 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.137-12
- Warn if stopping nodes will cause a loss of the quorum
- Resolves: rhbz#1180506

* Thu Jan 15 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.137-11
- Stop cluster nodes in parallel and keep cluster quorate during pacemaker
  shutdown
- Resolves: rhbz#1180506

* Fri Jan 09 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.137-10
- Stop deleted resource before removing its constraints
- Resolves: rhbz#1180390

* Thu Jan 08 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.137-9
- Added acl enable and disable commands
- Display whether acls are enabled in the 'pcs acl' output
- Resolves: rhbz#1054491

* Wed Jan 07 2015 Chris Feist <cfeist@redhat.cmo> 0.9.137-8
- Configuration of resource-discovery is now available on advanced location
  constraint rules
- Resolves: rhbz#1054491

* Wed Jan 07 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.137-7
- When a role is removed in the GUI the user is now automatically deleted
  if they aren't members of another role
- Resolves: rhbz#1054491

* Mon Jan 05 2015 Chris Feist <cfeist@redhat.com> - 0.9.137-6
- Allowed configuration of resource-discovery option on location constraint
  rules
- Resolves: rhbz#1054491

* Fri Dec 19 2014 Chris Feist <cfeist@redhat.com> - 0.9.137-5
- Fixed error message when creating a user with the same name as a role
- When a role is removed in the GUI the user is now automatically deleted
  if they aren't members of another role
- Resolves: rhbz#1054491

* Wed Dec 17 2014 Tomas Jelinek <tojeline@redhat.com> - 0.9.137-4
- Fixed displaying globally-unique clones in GUI
- Added latest version of clufter package
- Resolves: rhbz#1170150 rhbz#1133897

* Mon Dec 8 2014 Chris Feist <cfeist@redhat.com> - 0.9.137-3
- Added latest version of clufter package
- Resolves: rhbz#1133897

* Mon Dec 8 2014 Tomas Jelinek <tojeline@redhat.com> - 0.9.137-2
- Improved error messages for scoped cib operations
- Fixed waiting for resource commands to finish
- Resolves: rhbz#1115537 rhbz#1156311

* Tue Nov 25 2014 Tomas Jelinek <tojeline@redhat.com> - 0.9.137-1
- Added support for score-attribute in location rules in GUI
- Added ability to wait for resource commands to finish
- Fix clufter doc files installed with executable flag
- Resolves: rhbz#1111368 rhbz#1156311 rhbz#1073075 rhbz#1133897

* Mon Nov 24 2014 Chris Feist <cfeist@redhat.com> - 0.9.136-2
- Added latest version of clufter package
- Resolves: rhbz#1133897

* Wed Nov 19 2014 Chris Feist <cfeist@redhat.com> - 0.9.136-1
- Added support for 'pcs resource restart'
- Added ability to wait for a resource to start after creation
- Fixed issue with backports and ruby 2.0.0p576
- Fix for deleting a resource with a large number of options
- Fix warning when unpacking a pcs config tarball
- Resolves: rhbz#1111368 rhbz#1156311 rhbz#1156597

* Sat Oct 18 2014 Chris Feist <cfeist@redhat.com> - 0.9.135-1
- Added new clufter package
- Rebased to latest upstream sources
- Constraints tables are collapsed properly
- Resolves: rhbz#1111368 rhbz#1145560

* Sat Oct 18 2014 Chris Feist <cfeist@redhat.com> - 0.9.134-1
- Rebased to latest upstream packages
- Resolves: rhbz#1111368

* Fri Oct 17 2014 Chris Feist <cfeist@redhat.com> - 0.9.133-1
- Rebased to latest upstream packages
- Resolves: rhbz#1111368

* Tue Oct 07 2014 Tomas Jelinek <tojeline@redhat.com> - 0.9.132-1
- Rebased to latest upstream packages
- Resolves: rhbz#1111368

* Mon Sep 29 2014 Tomas Jelinek <tojeline@redhat.com> - 0.9.131-1
- Rebased to latest upstream packages
- Resolves: rhbz#1111368
- Added python-clufter subpackage (configuration conversion tool)
- Related:  rhbz#1133897

* Fri Sep 26 2014 Tomas Jelinek <tojeline@redhat.com> - 0.9.130-1
- Rebased to latest upstream packages
- Resolves: rhbz#1111368

* Mon Sep 22 2014 Tomas Jelinek <tojeline@redhat.com> - 0.9.129-1
- Rebased to latest upstream packages
- Resolves: rhbz#1111368

* Thu Sep 18 2014 Tomas Jelinek <tojeline@redhat.com> - 0.9.128-1
- Rebased to latest upstream packages
- Resolves: rhbz#1111368

* Fri Sep 12 2014 Chris Feist <cfeist@redhat.com> - 0.9.127-1
- Rebased to latest upstream packages
- Resolves: rhbz#1111368

* Fri Sep 05 2014 Chris Feist <cfeist@redhat.com> - 0.9.126-1
- Rebased to latest upstream packages
- Resolves: rhbz#1111368

* Tue Mar 25 2014 Chris Feist <cfeist@redhat.com> - 0.9.115-32
- Add ability to set totem options with pcs during cluster setup

* Tue Feb 25 2014 Chris Feist <cfeist@redhat.com> - 0.9.115-31
- Add ability to see group/clone/ms constraints and meta attributes in pcsd

* Mon Feb 24 2014 Chris Feist <cfeist@redhat.com> - 0.9.115-30
- Fix traceback with bad arguments to location rules
- Fix results code when attempting to remove an order that doesn't exist

* Fri Feb 21 2014 Chris Feist <cfeist@redhat.com> - 0.9.115-29
- Don't allow users to clone groups that have already been cloned
- Fix order remove <resource> to remove resources from sets
- Don't allow a user to force-start a group, clone or master/slave
- When using debug-start use proper return code
- Added cluster properties hover text
- Fixed issue with stripping a nil value
- HTML escape resource descriptions

* Wed Feb 19 2014 Chris Feist <cfeist@redhat.com> - 0.9.115-28
- Remove leading/trailing white space in resource descriptions
- Added tooltips for advanced cluster creation options
- Fixed other 'Remove fence devices' button
- When deleting a resource with pcsd use --force to prevent issues
- Add proper tooltip for resource description info icon
- Fix for long cluster names in menu
- Do a better job of detecting when to send a redirect and when to notif
- Don't silently ignore bad operation names

* Tue Feb 18 2014 Chris Feist <cfeist@redhat.com> - 0.9.115-27
- Added --nodesc option to pcs stonith list
- Don't attempt to print metadata for fence_sanlockd

* Tue Feb 18 2014 Chris Feist <cfeist@redhat.com> - 0.9.115-26
- Fixed dialog text when removing a fence device
- Show tool tips for optional fence agent arguments
- Fix bad link on resource remove sprite
- When removing a resource or fence device, show blank info
- Fix resource management issues when pacemaker is not running
- If first node is down, allow other nodes to show resource/stonith forms
- Removing all nodes, now removes cluster configuration
- Added ability to see nodes corosync/pacemaker/pcsd startup settings
- Added extra colspan to improve long cluster name display
- Added ability to configure IPv6 cluster
- Added ability to set corosync transport in GUI
- Added ability to set advanced cluster options on creation
- Renamed last_node_standing to last_man_standing
- On cluster creation color unauthorized nodes in orange
- Added proper redirect when session variable times out
- Fixed traceback when missing authentication tokens

* Mon Feb 17 2014 Chris Feist <cfeist@redhat.com> - 0.9.115-24
- Added support for meta attributes in the GUI
- Moved pcmk_host_list/map/check to optional arguments

* Wed Feb 12 2014 Chris Feist <cfeist@redhat.com> - 0.9.115-23
- Added ability to use 'and/or' with rules
- Fixed stonith optional arguments in pcsd

* Tue Feb 11 2014 Chris Feist <cfeist@redhat.com> - 0.9.115-22
- Fixed selection arrow when selecting new resource on resources page
- Fixed permissions on pcsd.service file

* Thu Feb 06 2014 Chris Feist <cfeist@redhat.com> - 0.9.115-21
- Added support for resource descriptions
- Show all nodes a resource is on for cloned resources
- Improve visibility of dropdown menus
- Keep last attempted login username if login fails

* Tue Feb 04 2014 Chris Feist <cfeist@redhat.com> - 0.9.115-20
- Fixed issue when removing all resources or fence devices
- Fixed duplicate id on fence device page

* Mon Feb 03 2014 Chris Feist <cfeist@redhat.com> - 0.9.115-19
- Fixed issue when creating a cluster from the GUI on a node that isn't in
  the newly formed cluster
- The GUI is now better at keeping track of nodes in the cluster

* Tue Jan 28 2014 Chris Feist <cfeist@redhat.com> - 0.9.115-17
- Fixed issue with cluster properties not displaying properly when running
  pcsd on a node that was not in the cluster being managed
- Fixed /etc/sysconfig/pcsd file for pcsd

* Tue Jan 28 2014 Chris Feist <cfeist@redhat.com> - 0.9.115-1
- Re-synced to upstream sources

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 0.9.114-2
- Mass rebuild 2014-01-24

* Thu Jan 23 2014 Chris Feist <cfeist@redhat.com> - 0.9.114-1
- Re-synced to upstream sources

* Wed Jan 22 2014 Chris Feist <cfeist@redhat.com> - 0.9.113-1
- Re-synced to upstream sources

* Mon Jan 20 2014 Chris Feist <cfeist@redhat.com> - 0.9.112-1
- Re-synced to upstream sources

* Mon Jan 20 2014 Chris Feist <cfeist@redhat.com> - 0.9.111-1
- Re-synced to upstream sources

* Fri Jan 17 2014 Chris Feist <cfeist@redhat.com> - 0.9.110-1
- Re-synced to upstream sources

* Wed Jan 15 2014 Chris Feist <cfeist@redhat.com> - 0.9.108-1
- Re-synced to upstream sources

* Wed Jan 15 2014 Chris Feist <cfeist@redhat.com> - 0.9.107-1
- Re-synced to upstream sources

* Tue Jan 14 2014 Chris Feist <cfeist@redhat.com> - 0.9.106-1
- Re-synced to upstream sources

* Mon Jan 13 2014 Chris Feist <cfeist@redhat.com> - 0.9.105-1
- Re-synced to upstream sources

* Fri Jan 10 2014 Chris Feist <cfeist@redhat.com> - 0.9.104-1
- Re-synced to upstream sources

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.9.100-2
- Mass rebuild 2013-12-27

* Tue Nov 12 2013 Chris Feist <cfeist@redhat.com> - 0.9.100-1
- Re-synced to upstream sources

* Thu Nov 07 2013 Chris Feist <cfeist@redhat.com> - 0.9.99-2
- Re-synced to upstream sources

* Wed Nov 06 2013 Chris Feist <cfeist@redhat.com> - 0.9.98-1
- Re-synced to upstream sources

* Tue Nov 05 2013 Chris Feist <cfeist@redhat.com> - 0.9.96-2
- Re-synced to upstream sources

* Tue Oct 29 2013 Chris Feist <cfeist@redhat.com> - 0.9.96-2
- Re-synced to upstream sources

* Tue Oct 22 2013 Chris Feist <cfeist@redhat.com> - 0.9.95-2
- Re-synced to upstream sources

* Tue Oct 22 2013 Chris Feist <cfeist@redhat.com> - 0.9.94-1
- Re-synced to upstream sources

* Wed Oct 16 2013 Chris Feist <cfeist@redhat.com> - 0.9.91-1
- Re-synced to upstream sources

* Tue Oct 15 2013 Chris Feist <cfeist@redhat.com> - 0.9.92-2
- Re-synced to upstream sources

* Wed Oct 09 2013 Chris Feist <cfeist@redhat.com> - 0.9.91-1
- Re-synced to upstream sources

* Wed Sep 18 2013 Chris Feist <cfeist@redhat.com> - 0.9.84-1
- Re-synced to upstream sources

* Tue Sep 03 2013 Chris Feist <cfeist@redhat.com> - 0.9.77-1
- Re-synced to upstreams sources

* Tue Sep 03 2013 Chris Feist <cfeist@redhat.com> - 0.9.76-1
- Re-synced to upstreams sources

* Fri Aug 09 2013 Chris Feist <cfeist@redhat.com> - 0.9.71-1
- Rebuilt with new upstream sources

* Fri Aug 09 2013 Chris Feist <cfeist@redhat.com> - 0.9.63-1
- Rebuilt with new upstream sources

* Wed Aug 07 2013 Chris Feist <cfeist@redhat.com> - 0.9.62-1
- Rebuilt with new upstream sources

* Tue Aug 06 2013 Chris Feist <cfeist@redhat.com> - 0.9.61-1
- Rebuilt with new upstream sources

* Mon Jul 29 2013 Chris Feist <cfeist@redhat.cmo> - 0.9.60-1
- Rebuilt with new upstream sources
- Added pcsd wizards

* Tue Jul 23 2013 Chris Feist <cfeist@redhat.cmo> - 0.9.58-1
- Rebuilt with new upstream sources

* Tue Jul 23 2013 Chris Feist <cfeist@redhat.cmo> - 0.9.57-1
- Rebuilt with new upstream sources

* Mon Jul 22 2013 Chris Feist <cfeist@redhat.cmo> - 0.9.56-1
- Rebuilt with upstream source
- Added missing bash completion file

* Mon Jul 22 2013 Chris Feist <cfeist@redhat.cmo> - 0.9.55-1
- Rebuilt with upstream source

* Wed Jul 10 2013 Chris Feist <cfeist@redhat.com> - 0.9.54-4
- Fix rpam error after adding systemd macros

* Wed Jul 10 2013 Chris Feist <cfeist@redhat.com> - 0.9.54-3
- Rebuild with proper upstream sources

* Wed Jul 10 2013 Chris Feist <cfeist@redhat.com> - 0.9.54-1
- Rebuild with upstream sources

* Wed Jul 10 2013 Chris Feist <cfeist@redhat.com> - 0.9.53-2
- Added systemd macros

* Tue Jul 09 2013 Chris Feist <cfeist@redhat.com> - 0.9.53-1
- Rebuild with upstream sources

* Mon Jul 08 2013 Chris Feist <cfeist@redhat.com> - 0.9.52-1
- Rebuild with upstream sources

* Mon Jul 01 2013 Chris Feist <cfeist@redhat.com> - 0.9.49-3
- Fix pcsd.conf source file location.

* Mon Jul 01 2013 Chris Feist <cfeist@redhat.com> - 0.9.49-1
- Rebuild with upstream sources

* Tue Jun 18 2013 Chris Feist <cfeist@redhat.com> - 0.9.48-1
- Rebuild with upstream sources

* Wed Jun 12 2013 Chris Feist <cfeist@redhat.com> - 0.9.47-1
- Rebuild with upstream sources

* Mon Jun 10 2013 Chris Feist <cfeist@redhat.com> - 0.9.46-1
- Rebuild with upstream sources

* Wed Jun 05 2013 Chris Feist <cfeist@redhat.com> - 0.9.45-2
- Rebuild with upstream sources

* Mon Jun 03 2013 Chris Feist <cfeist@redhat.com> - 0.9.44-4
- Rebuild with upstream sources

* Thu May 30 2013 Chris Feist <cfeist@redhat.com> - 0.9.44-1
- Rebuild with upstream sources

* Wed May 29 2013 Chris Feist <cfeist@redhat.com> - 0.9.43-1
- Rebuild with upstream sources

* Wed May 29 2013 Chris Feist <cfeist@redhat.com> - 0.9.42-5
- Fix issues with ruby 2.0 build

* Wed May 29 2013 Chris Feist <cfeist@redhat.com> - 0.9.42-1
- Rebuild with upstream sources

* Tue May 07 2013 Chris Feist <cfeist@redhat.com> - 0.9.41-1
- Rebuild with upstream sources

* Tue Apr 30 2013 Chris Feist <cfeist@redhat.com> - 0.9.40-1
- Rebuild with upstream sources

* Wed Apr 17 2013 Chris Feist <cfeist@redhat.com> - 0.9.39-1
- Rebuild with upstream sources

* Tue Apr 09 2013 Chris Feist <cfeist@redhat.com> - 0.9.38-1
- Rebuild with upstream sources

* Wed Apr 03 2013 Chris Feist <cfeist@redhat.com> - 0.9.37-4
- Re-enable gem builds with fix for ruby 2.0.0

* Tue Mar 26 2013 Chris Feist <cfeist@redhat.com> - 0.9.37-2
- Temporarily disable gem builds for ruby 2.0.0

* Wed Mar 20 2013 Chris Feist <cfeist@redhat.com> - 0.9.37-1
- Re-synced to upstream

* Fri Mar 15 2013 Chris Feist <cfeist@redhat.com> - 0.9.35-1
- Re-synced to upstream

* Tue Mar 12 2013 Chris Feist <cfeist@redhat.com> - 0.9.34-1
- Re-synced to upstream
- Updated pcsd location to /usr/lib

* Wed Feb 20 2013 Chris Feist <cfeist@redhat.com> - 0.9.32-1
- Re-synced to upstream

* Mon Feb 18 2013 Chris Feist <cfeist@redhat.com> - 0.9.31-1
- Re-synced to upstream

* Mon Jan 14 2013 Chris Feist <cfeist@redhat.com> - 0.9.30-1
- Updated build to properly manage combined pcs/pcsd

* Wed Jan 02 2013 Chris Feist <cfeist@redhat.com> - 0.9.29-4
- Updated certificate generation code to fix firefox issues

* Fri Dec 07 2012 Chris Feist <cfeist@redhat.com> - 0.9.29-3
- Added in missing pam service

* Thu Nov 29 2012 Chris Feist <cfeist@redhat.com> - 0.9.29-2
- Add pam-devel to BuildRequires

* Thu Nov 29 2012 Chris Feist <cfeist@redhat.com> - 0.9.29-1
- Resync to latest version of pcs/pcsd

* Fri Sep 28 2012 Chris Feist <cfeist@redhat.com> - 0.9.26-1
- Resync to latest version of pcs/pcsd

* Tue Aug 21 2012 Chris Feist <cfeist@redhat.com> - 0.9.15-1.test.1
- Resync to latest version of pcs/pcsd

* Mon Aug 13 2012 Chris Feist <cfeist@redhat.com> - 0.9.14-1.test.1
- Resync to latest version of pcs/pcsd

* Thu Aug 09 2012 Chris Feist <cfeist@redhat.com> - 0.9.13-1.test.1
- Resync to latest version of pcs and rename pcs-gui to pcsd

* Mon Jun 11 2012 Chris Feist <cfeist@redhat.com> - 0.9.5-5.test.1
- Resync to latest version of pcs

* Mon Jun 11 2012 Chris Feist <cfeist@redhat.com> - 0.9.5-4
- Resync to latest version of pcs

* Thu May 24 2012 Chris Feist <cfeist@redhat.com> - 0.9.4-1
- Resync to latest version of pcs
- Move cluster creation options to cluster sub command.

* Mon May 07 2012 Chris Feist <cfeist@redhat.com> - 0.9.3.1-1
- Resync to latest version of pcs which includes fixes to work with F17.

* Mon Mar 19 2012 Chris Feist <cfeist@redhat.com> - 0.9.2.4-1
- Resynced to latest version of pcs

* Mon Jan 23 2012 Chris Feist <cfeist@redhat.com> - 0.9.1-1
- Updated BuildRequires and %doc section for fedora

* Fri Jan 20 2012 Chris Feist <cfeist@redhat.com> - 0.9.0-2
- Updated spec file for fedora specific changes

* Mon Jan 16 2012 Chris Feist <cfeist@redhat.com> - 0.9.0-1
- Initial Build


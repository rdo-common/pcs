Name: pcs		
Version: 0.9.115
Release: 32%{?dist}.1
License: GPLv2
URL: http://github.com/feist/pcs
Group: System Environment/Base
#BuildArch: x86_64
BuildRequires: python2-devel
Summary: Pacemaker Configuration System	
Source0: http://people.redhat.com/cfeist/pcs/pcs-withgems-%{version}.tar.gz
Source1: HAM-logo.png
Patch1: rebase.patch
Patch2: bz1078343-Add-support-for-setting-certain-corosync-totem-optio.patch
Patch3: bz1184223-clone-one-step-fix.patch
BuildRequires: ruby >= 2.0.0 ruby-devel rubygems pam-devel git
BuildRequires: systemd-units rubygem-bundler
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Requires: pacemaker-cli corosync ruby >= 2.0.0 pacemaker

%description
pcs is a corosync and pacemaker configuration tool.  It permits users to
easily view, modify and created pacemaker based clusters.

%prep
%autosetup -p1 -S git

cp -f %SOURCE1 pcsd/public/images

%build

%install
rm -rf $RPM_BUILD_ROOT
pwd
make install DESTDIR=$RPM_BUILD_ROOT PYTHON_SITELIB=%{python_sitelib}
make install_pcsd DESTDIR=$RPM_BUILD_ROOT PYTHON_SITELIB=%{python_sitelib} hdrdir="%{_includedir}" rubyhdrdir="%{_includedir}" includedir="%{_includedir}"
chmod 755 $RPM_BUILD_ROOT/%{python_sitelib}/pcs/pcs.py

# Temporary fix for ruby-2.0.0 and rpam
#cp $RPM_BUILD_ROOT/usr/lib/pcsd/gemhome/gems/rpam-ruby19-1.2.1/ext/Rpam/rpam_ext.so $RPM_BUILD_ROOT/usr/lib/pcsd/gemhome/gems/rpam-ruby19-1.2.1/lib

%post
%systemd_post pcsd.service

%preun
%systemd_preun pcsd.service

%postun
%systemd_postun_with_restart pcsd.service

%files
%defattr(-,root,root,-)
%{python_sitelib}/pcs
%{python_sitelib}/pcs-%{version}-py2.*.egg-info
/usr/sbin/pcs
/usr/lib/pcsd/*
/usr/lib/pcsd/.bundle/config
/usr/lib/pcsd/.gitignore
/usr/lib/systemd/system/pcsd.service
/var/lib/pcsd
/etc/pam.d/pcsd
/etc/bash_completion.d/pcs
/etc/logrotate.d/pcsd
%dir /var/log/pcsd
/etc/sysconfig/pcsd
%{_mandir}/man8/pcs.*

%doc COPYING README

%changelog
* Tue Jan 20 2015 Chris Feist <cfeist@redhat.com> - 0.9.115-32.el7_0.1
- Do pcs resource create --clone/--master/--group in one step instead of
  two to prevent race conditions
- Resolves: rhbz#1184223

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


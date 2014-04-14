# SourcePath: zlib/20130402dev

Summary: compression library - runtime
Name: sony-target-dev-cpio
%define pkgname %{sony_tool_triplet}-%{sony_target_dialect}-dev-cpio
Version: 2.11
Release: 11000001
Source          : cpio-%{version}.tar.gz
# LOT scripts
# Source10: sony-cpio-libopt-build-cpio
Patch0: cpio_edit.patch 
License: Other
URL: http://www.zlib.net/
Group: %{sony_group}
Distribution: %{sony_distribution}
Vendor: %{sony_vendor}
Packager: %{sony_packager}
BuildRoot: %{_tmppath}/%{name}-root
Prefix: %{sony_target_dir}



# %define _bindir         %{sony_target_dir}%{sony_target_dev_bin_dir}
# %define _datadir        %{sony_target_dir}%{sony_target_dev_sharedstate_dir}
# %define _infodir        %{sony_target_dir}%{sony_target_dev_info_dir}
# %define _mandir         %{sony_target_dir}%{sony_target_dev_man_dir}
# %define _docdir         %{sony_target_dir}%{sony_target_dev_doc_dir}
# %define _rbindir        %{sony_target_dir}%{sony_target_dev_dir}/bin


%description

 

%package -n %{pkgname}
Summary: compression library - runtime
Group: %{sony_group}
AutoReqProv: no

%description -n %{pkgname}

### %package -n %{pkgname}-dev
### Summary: compression library - development
### Group: %{sony_group}
### AutoReqProv: no

### %description -n %{pkgname}-dev




### %package -n %{pkgname}-bin
### Summary         : compression library - sample programs
### Group: %{sony_group}

### %description -n %{pkgname}-bin



%prep
%setup -n cpio-%{version}
%patch0 -p1
%build
%sony_target_dev_setup
autoreconf
#autoconf
./configure --host=arm-sony-linux-gnueabi  --build=x86_64-pc-linux-gnu --prefix=/usr --includedir=/tool//usr/include --disable-nls





make 
%install
%sony_target_dev_setup

make DESTDIR=%{buildroot}%{sony_target_dir} install




 rm -rf %{buildroot}%{sony_target_dir}%{sony_target_dev_data_dir}/info
 rm -rf %{buildroot}%{sony_target_dir}%{sony_target_dev_data_dir}/man

%clean
rm -rf %{buildroot}


%files -n %{pkgname}
%defattr(-,root,root,-)
%{sony_target_dir}%{sony_target_dev_bin_dir}/cpio
%{sony_target_dir}%{sony_target_dev_prefix}/libexec/rmt

 

### %doc ChangeLog FAQ README build.log LICENSE



# for LOT


%changelog
* Tue Apr 02 2013 Sony Corporation
- update to 1.2.7

*Fri Apr 22 2005 Sony Corporation
- update to 1.2.2

* Thu Jan 13 2005 Sony Corporation
- delete minizip miniunzip command

* Thu Jan 13 2005 Sony Corporation
- delete tmpl pml files

* Tue Nov 16 2004 Sony Corporation
- 3 package -> 1 package 

* Thu Nov 10 2004 Sony Corporation
- change  Name: zlib -> Name: sony-target-dev-zlib

* Thu Oct 15 2004 Sony Corporation
- Initial build

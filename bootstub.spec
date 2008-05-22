Summary: this package provides bootstub binary for mrst power on
Name: bootstub
Version: 0.1
Release: 1%{?dist}
License: GPLv2
Group: System Environment/Shells
Source: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)  
Requires: make gcc awk dd ld bzip2

%description 
this package provides bootstub to create NAND boot image

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/boot
install -m 755 bootstub $RPM_BUILD_ROOT/boot/

%clean

%files
%defattr(-,root,root,-)
/boot/bootstub

%changelog
* Mon May 5 2008 Martin Xu <martin.xu@intel.com > - 0.1-1
- create initial package

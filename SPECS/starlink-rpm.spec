Name:     pycupid-libs
Version:	0.1
Release:	1%{?dist}
Summary:	Starlink's cupid rpm for Manylinux x86_64 (CentOs 5.11)
License:	LGPL
URL: https://github.com/cvalenzu/starlink-rpm
Group: Applications
BuildRoot: %{_topdir}/BUILDROOT/%{name}-%{version}
Source0:	%{name}-%{version}.tar.gz
BuildRequires: gcc gcc-c++ gcc-gfortran csh libXext-devel libXau-devel libX11-devel libXt-devel libxml2-devel ncurses-devel python-devel Cython
Requires: gcc gcc-g++ gcc-gfortran csh libXext-devel libXau-devel libX11-devel libXt-devel libxml2-devel ncurses-devel python-devel Cython

%description
Starlink package for Manylinux, useful for python wrappers.

%prep
%setup -q

%build
#Creating folder
rm -rf %{_builddir}/star
mkdir -p %{_builddir}/star

##Exporting environment variables
export STARLINK_DIR=%{_builddir}/star

##Remove update submodules (it should be updated)
sed -i '177d' %{_builddir}/%{name}-%{version}/starlink/bootstrap

##Compiling starlink
cd %{_builddir}/%{name}-%{version}
make

strip -S --strip-unneeded --remove-section=.note.gnu.gold-version --remove-section=.comment --remove-section=.note --remove-section=.note.gnu.build-id --remove-section=.note.ABI-tag %{_builddir}/star/lib/*.so

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/opt/pycupid
cp -rf %{_builddir}/star %{buildroot}/opt/pycupid


%clean

%post

%files
/opt/pycupid/lib/*

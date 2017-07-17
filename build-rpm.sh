#!/bin/bash
VERSION=0.1

echo "##################################################################################"
echo "                       Installing Dependencies                                    "
echo "##################################################################################"

#Installing required packages
yum groupinstall -y "Development Tools"
yum install -y  gcc gcc-c++ gcc-gfortran csh libXext-devel libXau-devel libX11-devel \
              libXt-devel libxml2-devel ncurses-devel texlive-multirow python-devel Cython sshpass

#Installing rpmbuild package
yum install -y rpm-build rpmdevtools


echo "##################################################################################"
echo "                        Packing Sources                                    "
echo "##################################################################################"

cd /pycupid-libs
#Compressing the source files
cd SOURCES
mkdir -p pycupid-libs-$VERSION
cp -rf starlink pycupid-libs-$VERSION/
cp Makefile pycupid-libs-$VERSION
tar -zcf pycupid-libs-$VERSION.tar.gz pycupid-libs-$VERSION
rm -rf pycupid-libs-$VERSION
cd ..

cd SPECS
cp starlink-rpm.spec pycupid-libs-$VERSION.spec
cd ..

echo "##################################################################################"
echo "                       Compiling                                   "
echo "##################################################################################"

mkdir BUILD
mkdir BUILDROOT
mkdir RPMS
mkdir SRPMS
rpmbuild -ba SPECS/pycupid-libs-$VERSION.spec --define "_topdir $PWD"


#docker run --rm --name builder -v `pwd`:/pycupid-libs/ quay.io/pypa/manylinux1_x86_64 /pycupid-libs/build-rpm.sh

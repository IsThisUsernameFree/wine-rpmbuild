# Prerequisites

Install rpm-build and wine build prerequisites 

```
yum install rpm-build
yum groupinstall "Development Tools"

```

Install wine build prerequisites 

`yum-builddep SPECS/wine.spec`

# Build instructions

## Get latest Wine archive, eg:

`curl https://dl.winehq.org/wine/source/8.x/wine-8.7.tar.xz -O SOURCES/wine.tar.xz`

## Build the RPM

Build package (base, debug and src)

`rpmbuild -ba ./SPECS/wine.spec`

For other options, please refer to https://linux.die.net/man/8/rpmbuild


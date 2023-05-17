#Instructions :


```
# Move into rpmbuild directory 
cd  wine-rpmbuild

# Install required packages
yum install rpm-build
yum groupinstall "Development Tools"

# Install wine build dependencies
yum-builddep SPECS/wine.spec

# Download Wine sources
mkdir SOURCES
curl https://dl.winehq.org/wine/source/8.x/wine-8.7.tar.xz -o SOURCES/wine.tar.xz

# Build package(s)
## All packages
rpmbuild -ba ./SPECS/wine.spec --define "_topdir $(pwd)" --define "version 8.7"

## Binary package
rpmbuild -bb ./SPECS/wine.spec --define "_topdir $(pwd)" --define "version 8.7"

## Source package
rpmbuild -bs ./SPECS/wine.spec --define "_topdir $(pwd)" --define "version 8.7"
```

For other options, please refer to https://linux.die.net/man/8/rpmbuild


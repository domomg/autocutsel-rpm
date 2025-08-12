# Autocutsel RPM Package

This repository automates the compilation and packaging of Autocutsel into an RPM for Fedora, which currently does not include Autocutsel in its repositories.

## About Autocutsel

Autocutsel synchronizes the X11 cutbuffer and CLIPBOARD selection. This utility is useful for ensuring that clipboard operations work seamlessly across different applications in X11 environments.

- **Official Website:** [https://www.nongnu.org/autocutsel/](https://www.nongnu.org/autocutsel/)
- **Source Tarball:** [autocutsel-0.10.1.tar.gz](https://github.com/sigmike/autocutsel/releases/download/0.10.1/autocutsel-0.10.1.tar.gz)

## Purpose

This repository provides a simple solution for Fedora users to build and obtain an RPM package of Autocutsel. The automation is achieved via GitHub Actions.

## Usage

To download and install the RPM package, visit the [Releases](https://github.com/domomg/autocutsel-rpm/releases) page of this repository. Follow these steps to install the package:

1. Download the RPM from the latest release.
2. Install the RPM using the following command:

   ```bash
   sudo rpm -ivh autocutsel-0.10.1-1.x86_64.rpm

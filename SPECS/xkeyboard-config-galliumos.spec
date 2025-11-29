# COPR SPEC FILE: xkeyboard-config-galliumos.spec
# Fetches the pre-patched source from the GalliumOS GitHub release.

# --- PACKAGE METADATA ---
Name:           xkeyboard-config-galliumos
Version:        1.0.0
Release:        1%{?dist}
Summary:        X Keyboard Extension config data modified for GalliumOS/Chromebooks

License:        X11
URL:            https://github.com/GalliumOS/xkeyboard-config

# Fetches the remote ZIP file containing the already-modified source.
Source0:        https://github.com/GalliumOS/xkeyboard-config/archive/refs/tags/release-1.0.zip

# Standard Build Dependencies for xkeyboard-config (Autotools setup)
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext
BuildRequires:  libX11-devel
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  intltool
BuildRequires:  perl
BuildRequires:  xsltproc

%description
This package contains X Keyboard Extension (XKB) configuration data
with custom keymap and model settings optimized for GalliumOS and
Chromebook hardware.

%prep
# Unpack Source0 (the remote ZIP file).
# The archive unpacks to a directory named xkeyboard-config-release-1.0
%setup -q -n xkeyboard-config-release-1.0

# The source comes from a git snapshot and is missing the generated
# 'configure' script, so we must run autogen.sh.
sh autogen.sh

# PATCHES ARE OMITTED as the source is pre-patched.

%build
# Standard Autotools build process
%configure
%make_build


%install
# Install files into the temporary build root
%make_install

# Clean up unnecessary files
find %{buildroot} -name "*.la" -delete


%files
%license COPYING
%doc AUTHORS README NEWS ChangeLog TODO
# All XKB data files
%{_datadir}/X11/xkb/*
# All documentation and translation files
%{_datadir}/locale/*
%{_mandir}/man7/*


%changelog
* Fri Nov 29 2025 Your Name <you@example.com> - 1.0.0-1
- Initial COPR package build using the pre-patched GalliumOS source archive.
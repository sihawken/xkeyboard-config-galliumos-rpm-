# The name of your COPR package. Must be unique.
Name:           xkeyboard-config-galliumos
# The package version should reflect the source (release-1.0)
Version:        1.0.0
Release:        1%{?dist}
Summary:        X Keyboard Extension config data modified for GalliumOS/Chromebooks

License:        X11
URL:            https://github.com/GalliumOS/xkeyboard-config

%define git_commit      master
%define short_name      xkeyboard-config

# Source0 fetches the archive of the defined git_commit.
Source0:        https://github.com/GalliumOS/%{short_name}/archive/%{git_commit}/%{short_name}-%{git_commit}.tar.gz

# Custom patches (must be present in the SOURCES/ directory)
Patch1:         chromebook.patch
Patch2:         docs.diff
Patch3:         fix-typo.diff
Patch4:         revert-goodmap-badmap-for-apple.diff

# Standard Build Dependencies for xkeyboard-config
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  intltool
BuildRequires:  perl
BuildRequires:  xsltproc

%description
This package contains X Keyboard Extension (XKB) configuration data
with custom keymap and model settings optimized for GalliumOS and
Chromebook hardware, based on the GalliumOS/xkeyboard-config source.

%prep
# Unpack Source0 (the remote ZIP file).
# The downloaded file is xkeyboard-config-release-1.0.zip, which unpacks
# to a directory named xkeyboard-config-release-1.0. We use the -n flag
# to specify that directory name.
%setup -q -n xkeyboard-config-release-1.0

# The source comes from a git snapshot and is missing the generated
# 'configure' script, so we must run autogen.sh.
sh autogen.sh

# Apply all patches using the standard -p1 strip level
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1


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
- Initial Fedora package build for COPR, fetching source from release-1.0 tag.
- Applied patches for Chromebook support.
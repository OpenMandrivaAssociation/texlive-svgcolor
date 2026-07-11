%global tl_name svgcolor
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Define SVG named colours
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/svgcolor
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/svgcolor.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/svgcolor.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package defines the W3C Scalable Vector Graphics (SVG) colour names
for use with both the color and PSTricks packages.


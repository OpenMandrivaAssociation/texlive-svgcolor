Name:		texlive-svgcolor
Version:	15878
Release:	2
Summary:	Define SVG named colours
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/svgcolor
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/svgcolor.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/svgcolor.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines the W3C Scalable Vector Graphics (SVG)
colour names for use with both the color and PSTricks packages.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/svgcolor/svgcolor.sty
%doc %{_texmfdistdir}/doc/latex/svgcolor/README

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}

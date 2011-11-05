# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/svgcolor
# catalog-date 2006-08-27 16:41:02 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-svgcolor
Version:	1.0
Release:	1
Summary:	Define SVG named colours
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/svgcolor
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/svgcolor.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/svgcolor.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3

%description
The package defines the W3C Scalable Vector Graphics (SVG)
colour names for use with both the color and PSTricks packages.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/svgcolor/svgcolor.sty
%doc %{_texmfdistdir}/doc/latex/svgcolor/README
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}

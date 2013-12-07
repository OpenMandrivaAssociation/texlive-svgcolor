# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/svgcolor
# catalog-date 2006-08-27 16:41:02 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-svgcolor
Version:	1.0
Release:	4
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 756357
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 719615
- texlive-svgcolor
- texlive-svgcolor
- texlive-svgcolor
- texlive-svgcolor


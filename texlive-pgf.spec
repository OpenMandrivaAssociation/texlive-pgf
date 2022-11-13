Name:		texlive-pgf
Version:	59210
Release:	1
Summary:	Create PostScript and PDF graphics in TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/base
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-xkeyval

%description
PGF is a macro package for creating graphics. It is platform-
and format-independent and works together with the most
important TeX backend drivers, including pdftex and dvips. It
comes with a user-friendly syntax layer called TikZ. Its usage
is similar to pstricks and the standard picture environment.
PGF works with plain (pdf-)TeX, (pdf-)LaTeX, and ConTeXt.
Unlike pstricks, it can produce either PostScript or PDF
output.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/context/third/pgf
%{_texmfdistdir}/tex/generic/pgf
%{_texmfdistdir}/tex/latex/pgf
%{_texmfdistdir}/tex/plain/pgf
%doc %{_texmfdistdir}/doc/generic/pgf
#- source
%doc %{_texmfdistdir}/source/generic/pgf

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

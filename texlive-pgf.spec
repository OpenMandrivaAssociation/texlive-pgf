%global tl_name pgf
%global tl_revision 78101

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.1.11a
Release:	%{tl_revision}.1
Summary:	Create PostScript and PDF graphics in TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/base
License:	lppl1.3c gpl2 fdl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(atveryend)
Requires:	texlive(fp)
Requires:	texlive(graphics)
Requires:	texlive(pdftexcmds)
Requires:	texlive(xcolor)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
PGF is a macro package for creating graphics. It is platform- and
format-independent and works together with the most important TeX
backend drivers, including pdfTeX and dvips. It comes with a user-
friendly syntax layer called TikZ. Its usage is similar to pstricks and
the standard picture environment. PGF works with plain (pdf-)TeX,
(pdf-)LaTeX, and ConTeXt. Unlike pstricks, it can produce either
PostScript or PDF output.


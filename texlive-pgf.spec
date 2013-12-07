# revision 22614
# category Package
# catalog-ctan /graphics/pgf/base
# catalog-date 2010-10-27 12:56:09 +0200
# catalog-license lppl1.3
# catalog-version 2.10
Name:		texlive-pgf
Version:	2.10
Release:	4
Summary:	Create PostScript and PDF graphics in TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/base
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf.source.tar.xz
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
%{_texmfdistdir}/tex/context/third/pgf/basiclayer/t-pgf.tex
%{_texmfdistdir}/tex/context/third/pgf/basiclayer/t-pgfbim.tex
%{_texmfdistdir}/tex/context/third/pgf/basiclayer/t-pgfbla.tex
%{_texmfdistdir}/tex/context/third/pgf/basiclayer/t-pgfbma.tex
%{_texmfdistdir}/tex/context/third/pgf/basiclayer/t-pgfbpl.tex
%{_texmfdistdir}/tex/context/third/pgf/basiclayer/t-pgfbpt.tex
%{_texmfdistdir}/tex/context/third/pgf/basiclayer/t-pgfbsh.tex
%{_texmfdistdir}/tex/context/third/pgf/basiclayer/t-pgfbsn.tex
%{_texmfdistdir}/tex/context/third/pgf/basiclayer/t-pgfcor.tex
%{_texmfdistdir}/tex/context/third/pgf/frontendlayer/t-tikz.tex
%{_texmfdistdir}/tex/context/third/pgf/math/t-pgfmat.tex
%{_texmfdistdir}/tex/context/third/pgf/systemlayer/t-pgfsys.tex
%{_texmfdistdir}/tex/context/third/pgf/utilities/t-pgfcal.tex
%{_texmfdistdir}/tex/context/third/pgf/utilities/t-pgffor.tex
%{_texmfdistdir}/tex/context/third/pgf/utilities/t-pgfkey.tex
%{_texmfdistdir}/tex/context/third/pgf/utilities/t-pgfmod.tex
%{_texmfdistdir}/tex/context/third/pgf/utilities/t-pgfrcs.tex
%{_texmfdistdir}/tex/generic/pgf/basiclayer/pgfcore.code.tex
%{_texmfdistdir}/tex/generic/pgf/basiclayer/pgfcorearrows.code.tex
%{_texmfdistdir}/tex/generic/pgf/basiclayer/pgfcoreexternal.code.tex
%{_texmfdistdir}/tex/generic/pgf/basiclayer/pgfcoregraphicstate.code.tex
%{_texmfdistdir}/tex/generic/pgf/basiclayer/pgfcoreimage.code.tex
%{_texmfdistdir}/tex/generic/pgf/basiclayer/pgfcorelayers.code.tex
%{_texmfdistdir}/tex/generic/pgf/basiclayer/pgfcoreobjects.code.tex
%{_texmfdistdir}/tex/generic/pgf/basiclayer/pgfcorepathconstruct.code.tex
%{_texmfdistdir}/tex/generic/pgf/basiclayer/pgfcorepathprocessing.code.tex
%{_texmfdistdir}/tex/generic/pgf/basiclayer/pgfcorepathusage.code.tex
%{_texmfdistdir}/tex/generic/pgf/basiclayer/pgfcorepatterns.code.tex
%{_texmfdistdir}/tex/generic/pgf/basiclayer/pgfcorepoints.code.tex
%{_texmfdistdir}/tex/generic/pgf/basiclayer/pgfcorequick.code.tex
%{_texmfdistdir}/tex/generic/pgf/basiclayer/pgfcorescopes.code.tex
%{_texmfdistdir}/tex/generic/pgf/basiclayer/pgfcoreshade.code.tex
%{_texmfdistdir}/tex/generic/pgf/basiclayer/pgfcoretransformations.code.tex
%{_texmfdistdir}/tex/generic/pgf/basiclayer/pgfcoretransparency.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/svg/svgpgf.cfg
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/svg/svgpgf.xmt
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/svg/svgtest.cfg
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/svg/svgtest.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/svg/svgtest.xml
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/circuits/tikzlibrarycircuits.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/circuits/tikzlibrarycircuits.ee.IEC.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/circuits/tikzlibrarycircuits.ee.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/circuits/tikzlibrarycircuits.logic.CDH.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/circuits/tikzlibrarycircuits.logic.IEC.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/circuits/tikzlibrarycircuits.logic.US.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/circuits/tikzlibrarycircuits.logic.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/datavisualization/tikzlibrarydatavisualization.3d.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/datavisualization/tikzlibrarydatavisualization.barcharts.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/datavisualization/tikzlibrarydatavisualization.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/datavisualization/tikzlibrarydatavisualization.formats.functions.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/datavisualization/tikzlibrarydatavisualization.polar.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/datavisualization/tikzlibrarydatavisualization.sparklines.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/graphs/tikzlibrarygraphs.basic.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/graphs/tikzlibrarygraphs.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzexternalshared.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrary3d.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryarrows.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryautomata.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarybackgrounds.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarycalc.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarycalendar.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarychains.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarydecorations.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarydecorations.footprints.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarydecorations.fractals.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarydecorations.markings.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarydecorations.pathmorphing.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarydecorations.pathreplacing.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarydecorations.shapes.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarydecorations.text.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryer.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryfadings.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryfit.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryfixedpointarithmetic.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryfolding.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryfpu.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryintersections.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarylindenmayersystems.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarymatrix.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarymindmap.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarypatterns.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarypetri.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryplothandlers.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryplotmarks.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarypositioning.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryscopes.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryshadings.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryshadows.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryshapes.arrows.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryshapes.callouts.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryshapes.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryshapes.gates.logic.IEC.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryshapes.gates.logic.US.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryshapes.geometric.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryshapes.misc.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryshapes.multipart.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryshapes.symbols.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarysnakes.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryspy.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarysvg.path.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarythrough.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarytopaths.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarytrees.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryturtle.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/tikz.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/datavisualization/pgflibrarydatavisualization.barcharts.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/datavisualization/pgflibrarydatavisualization.formats.functions.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/datavisualization/pgflibrarydatavisualization.polar.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/decorations/pgflibrarydecorations.footprints.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/decorations/pgflibrarydecorations.fractals.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/decorations/pgflibrarydecorations.markings.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/decorations/pgflibrarydecorations.pathmorphing.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/decorations/pgflibrarydecorations.pathreplacing.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/decorations/pgflibrarydecorations.shapes.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/decorations/pgflibrarydecorations.text.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/pgflibraryarrows.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/pgflibraryfadings.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/pgflibraryfixedpointarithmetic.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/pgflibraryfpu.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/pgflibraryintersections.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/pgflibrarylindenmayersystems.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/pgflibrarypatterns.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/pgflibraryplothandlers.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/pgflibraryplotmarks.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/pgflibraryprofiler.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/pgflibraryshadings.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/pgflibrarysnakes.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/pgflibrarysvg.path.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/shapes/circuits/pgflibraryshapes.gates.ee.IEC.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/shapes/circuits/pgflibraryshapes.gates.ee.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/shapes/circuits/pgflibraryshapes.gates.logic.IEC.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/shapes/circuits/pgflibraryshapes.gates.logic.US.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/shapes/circuits/pgflibraryshapes.gates.logic.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/shapes/pgflibraryshapes.arrows.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/shapes/pgflibraryshapes.callouts.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/shapes/pgflibraryshapes.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/shapes/pgflibraryshapes.geometric.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/shapes/pgflibraryshapes.misc.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/shapes/pgflibraryshapes.multipart.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/shapes/pgflibraryshapes.symbols.code.tex
%{_texmfdistdir}/tex/generic/pgf/math/pgfmath.code.tex
%{_texmfdistdir}/tex/generic/pgf/math/pgfmathcalc.code.tex
%{_texmfdistdir}/tex/generic/pgf/math/pgfmathfloat.code.tex
%{_texmfdistdir}/tex/generic/pgf/math/pgfmathfunctions.base.code.tex
%{_texmfdistdir}/tex/generic/pgf/math/pgfmathfunctions.basic.code.tex
%{_texmfdistdir}/tex/generic/pgf/math/pgfmathfunctions.code.tex
%{_texmfdistdir}/tex/generic/pgf/math/pgfmathfunctions.comparison.code.tex
%{_texmfdistdir}/tex/generic/pgf/math/pgfmathfunctions.misc.code.tex
%{_texmfdistdir}/tex/generic/pgf/math/pgfmathfunctions.random.code.tex
%{_texmfdistdir}/tex/generic/pgf/math/pgfmathfunctions.round.code.tex
%{_texmfdistdir}/tex/generic/pgf/math/pgfmathfunctions.trigonometric.code.tex
%{_texmfdistdir}/tex/generic/pgf/math/pgfmathparser.code.tex
%{_texmfdistdir}/tex/generic/pgf/math/pgfmathutil.code.tex
%{_texmfdistdir}/tex/generic/pgf/modules/pgfmoduledatavisualization.code.tex
%{_texmfdistdir}/tex/generic/pgf/modules/pgfmoduledecorations.code.tex
%{_texmfdistdir}/tex/generic/pgf/modules/pgfmodulematrix.code.tex
%{_texmfdistdir}/tex/generic/pgf/modules/pgfmoduleoo.code.tex
%{_texmfdistdir}/tex/generic/pgf/modules/pgfmoduleparser.code.tex
%{_texmfdistdir}/tex/generic/pgf/modules/pgfmoduleplot.code.tex
%{_texmfdistdir}/tex/generic/pgf/modules/pgfmoduleshapes.code.tex
%{_texmfdistdir}/tex/generic/pgf/modules/pgfmodulesnakes.code.tex
%{_texmfdistdir}/tex/generic/pgf/modules/pgfmodulesorting.code.tex
%{_texmfdistdir}/tex/generic/pgf/rendering/pgfrenderpoints.code.tex
%{_texmfdistdir}/tex/generic/pgf/rendering/pgfrendertransform.code.tex
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgf.cfg
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsys-common-pdf-via-dvi.def
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsys-common-pdf.def
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsys-common-postscript.def
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsys-common-svg.def
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsys-dvi.def
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsys-dvipdfm.def
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsys-dvipdfmx.def
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsys-dvips.def
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsys-pdftex.def
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsys-tex4ht.def
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsys-textures.def
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsys-vtex.def
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsys-xetex.def
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsys.code.tex
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsysprotocol.code.tex
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsyssoftpath.code.tex
%{_texmfdistdir}/tex/generic/pgf/utilities/pgfcalendar.code.tex
%{_texmfdistdir}/tex/generic/pgf/utilities/pgfexternal.tex
%{_texmfdistdir}/tex/generic/pgf/utilities/pgfexternalwithdepth.tex
%{_texmfdistdir}/tex/generic/pgf/utilities/pgffor.code.tex
%{_texmfdistdir}/tex/generic/pgf/utilities/pgfkeys.code.tex
%{_texmfdistdir}/tex/generic/pgf/utilities/pgfkeysfiltered.code.tex
%{_texmfdistdir}/tex/generic/pgf/utilities/pgfrcs.code.tex
%{_texmfdistdir}/tex/generic/pgf/utilities/pgfutil-common.tex
%{_texmfdistdir}/tex/generic/pgf/utilities/pgfutil-context.def
%{_texmfdistdir}/tex/generic/pgf/utilities/pgfutil-latex.def
%{_texmfdistdir}/tex/generic/pgf/utilities/pgfutil-plain.def
%{_texmfdistdir}/tex/latex/pgf/basiclayer/pgf.sty
%{_texmfdistdir}/tex/latex/pgf/basiclayer/pgfbaseimage.sty
%{_texmfdistdir}/tex/latex/pgf/basiclayer/pgfbaselayers.sty
%{_texmfdistdir}/tex/latex/pgf/basiclayer/pgfbasematrix.sty
%{_texmfdistdir}/tex/latex/pgf/basiclayer/pgfbasepatterns.sty
%{_texmfdistdir}/tex/latex/pgf/basiclayer/pgfbaseplot.sty
%{_texmfdistdir}/tex/latex/pgf/basiclayer/pgfbaseshapes.sty
%{_texmfdistdir}/tex/latex/pgf/basiclayer/pgfbasesnakes.sty
%{_texmfdistdir}/tex/latex/pgf/basiclayer/pgfcore.sty
%{_texmfdistdir}/tex/latex/pgf/compatibility/pgfarrows.sty
%{_texmfdistdir}/tex/latex/pgf/compatibility/pgfautomata.sty
%{_texmfdistdir}/tex/latex/pgf/compatibility/pgfcomp-version-0-65.sty
%{_texmfdistdir}/tex/latex/pgf/compatibility/pgfcomp-version-1-18.sty
%{_texmfdistdir}/tex/latex/pgf/compatibility/pgfheaps.sty
%{_texmfdistdir}/tex/latex/pgf/compatibility/pgflibraryarrows.sty
%{_texmfdistdir}/tex/latex/pgf/compatibility/pgflibraryautomata.sty
%{_texmfdistdir}/tex/latex/pgf/compatibility/pgflibraryplothandlers.sty
%{_texmfdistdir}/tex/latex/pgf/compatibility/pgflibraryplotmarks.sty
%{_texmfdistdir}/tex/latex/pgf/compatibility/pgflibraryshapes.sty
%{_texmfdistdir}/tex/latex/pgf/compatibility/pgflibrarysnakes.sty
%{_texmfdistdir}/tex/latex/pgf/compatibility/pgflibrarytikzbackgrounds.sty
%{_texmfdistdir}/tex/latex/pgf/compatibility/pgflibrarytikztrees.sty
%{_texmfdistdir}/tex/latex/pgf/compatibility/pgfnodes.sty
%{_texmfdistdir}/tex/latex/pgf/compatibility/pgfshade.sty
%{_texmfdistdir}/tex/latex/pgf/doc/pgfmanual.code.tex
%{_texmfdistdir}/tex/latex/pgf/doc/pgfmanual.pdflinks.code.tex
%{_texmfdistdir}/tex/latex/pgf/doc/pgfmanual.prettyprinter.code.tex
%{_texmfdistdir}/tex/latex/pgf/doc/pgfmanual.sty
%{_texmfdistdir}/tex/latex/pgf/frontendlayer/libraries/tikzlibraryexternal.code.tex
%{_texmfdistdir}/tex/latex/pgf/frontendlayer/pgfpict2e.sty
%{_texmfdistdir}/tex/latex/pgf/frontendlayer/tikz.sty
%{_texmfdistdir}/tex/latex/pgf/math/pgfmath.sty
%{_texmfdistdir}/tex/latex/pgf/systemlayer/pgfsys.sty
%{_texmfdistdir}/tex/latex/pgf/utilities/pgfcalendar.sty
%{_texmfdistdir}/tex/latex/pgf/utilities/pgffor.sty
%{_texmfdistdir}/tex/latex/pgf/utilities/pgfkeys.sty
%{_texmfdistdir}/tex/latex/pgf/utilities/pgfpages.sty
%{_texmfdistdir}/tex/latex/pgf/utilities/pgfrcs.sty
%{_texmfdistdir}/tex/latex/pgf/utilities/tikzexternal.sty
%{_texmfdistdir}/tex/latex/pgf/utilities/xxcolor.sty
%{_texmfdistdir}/tex/plain/pgf/basiclayer/pgf.tex
%{_texmfdistdir}/tex/plain/pgf/basiclayer/pgfbaseimage.tex
%{_texmfdistdir}/tex/plain/pgf/basiclayer/pgfbaselayers.tex
%{_texmfdistdir}/tex/plain/pgf/basiclayer/pgfbasematrix.tex
%{_texmfdistdir}/tex/plain/pgf/basiclayer/pgfbasepatterns.tex
%{_texmfdistdir}/tex/plain/pgf/basiclayer/pgfbaseplot.tex
%{_texmfdistdir}/tex/plain/pgf/basiclayer/pgfbaseshapes.tex
%{_texmfdistdir}/tex/plain/pgf/basiclayer/pgfbasesnakes.tex
%{_texmfdistdir}/tex/plain/pgf/basiclayer/pgfcore.tex
%{_texmfdistdir}/tex/plain/pgf/frontendlayer/tikz.tex
%{_texmfdistdir}/tex/plain/pgf/math/pgfmath.tex
%{_texmfdistdir}/tex/plain/pgf/systemlayer/pgfsys.tex
%{_texmfdistdir}/tex/plain/pgf/utilities/pgfcalendar.tex
%{_texmfdistdir}/tex/plain/pgf/utilities/pgffor.tex
%{_texmfdistdir}/tex/plain/pgf/utilities/pgfkeys.tex
%{_texmfdistdir}/tex/plain/pgf/utilities/pgfrcs.tex
%doc %{_texmfdistdir}/doc/generic/pgf/AUTHORS
%doc %{_texmfdistdir}/doc/generic/pgf/ChangeLog
%doc %{_texmfdistdir}/doc/generic/pgf/FILES
%doc %{_texmfdistdir}/doc/generic/pgf/INSTALL
%doc %{_texmfdistdir}/doc/generic/pgf/README
%doc %{_texmfdistdir}/doc/generic/pgf/TODO
%doc %{_texmfdistdir}/doc/generic/pgf/images/brave-gnu-world-logo-mask.bb
%doc %{_texmfdistdir}/doc/generic/pgf/images/brave-gnu-world-logo-mask.jpg
%doc %{_texmfdistdir}/doc/generic/pgf/images/brave-gnu-world-logo.25.bb
%doc %{_texmfdistdir}/doc/generic/pgf/images/brave-gnu-world-logo.25.eps
%doc %{_texmfdistdir}/doc/generic/pgf/images/brave-gnu-world-logo.25.jpg
%doc %{_texmfdistdir}/doc/generic/pgf/images/brave-gnu-world-logo.bb
%doc %{_texmfdistdir}/doc/generic/pgf/images/brave-gnu-world-logo.eps
%doc %{_texmfdistdir}/doc/generic/pgf/images/brave-gnu-world-logo.jpg
%doc %{_texmfdistdir}/doc/generic/pgf/images/pgfmanual-mindmap-1.pdf
%doc %{_texmfdistdir}/doc/generic/pgf/images/pgfmanual-mindmap-2.pdf
%doc %{_texmfdistdir}/doc/generic/pgf/licenses/LICENSE
%doc %{_texmfdistdir}/doc/generic/pgf/licenses/gnu-free-documentation-license-1.2.txt
%doc %{_texmfdistdir}/doc/generic/pgf/licenses/gnu-public-license-2.txt
%doc %{_texmfdistdir}/doc/generic/pgf/licenses/latex-project-public-license-1.3c.txt
%doc %{_texmfdistdir}/doc/generic/pgf/licenses/manifest-code.txt
%doc %{_texmfdistdir}/doc/generic/pgf/licenses/manifest-documentation.txt
%doc %{_texmfdistdir}/doc/generic/pgf/macros/pgfmanual-en-macros.tex
%doc %{_texmfdistdir}/doc/generic/pgf/pgfmanual.pdf
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-base-actions.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-base-arrows.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-base-decorations.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-base-design.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-base-external.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-base-images.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-base-internalregisters.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-base-layers.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-base-matrices.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-base-nodes.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-base-paths.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-base-patterns.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-base-plots.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-base-points.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-base-quick.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-base-scopes.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-base-shadings.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-base-transformations.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-base-transparency.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-drivers.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-dv-axes.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-dv-backend.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-dv-examples.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-dv-formats.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-dv-introduction.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-dv-main.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-dv-stylesheets.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-dv-visualizers.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-guidelines.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-installation.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-introduction.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-3d.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-arrows.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-automata.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-backgrounds.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-calc.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-calendar.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-chains.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-circuits.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-decorations.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-edges.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-er.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-external.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-fadings.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-fit.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-fixedpoint.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-folding.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-fpu.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-lsystems.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-matrices.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-mindmaps.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-patterns.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-petri.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-plot-handlers.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-plot-marks.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-profiler.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-shadings.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-shadows.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-shapes.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-spy.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-svg-path.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-through.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-trees.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-turtle.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-license.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-main.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-math-algorithms.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-math-commands.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-math-design.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-math-numberprinting.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-math-parsing.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-module-parser.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-oo.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-pages.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-pgfcalendar.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-pgffor.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-pgfkeys.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-pgfkeysfiltered.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-pgfsys-commands.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-pgfsys-overview.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-pgfsys-paths.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-pgfsys-protocol.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tikz-actions.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tikz-coordinates.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tikz-decorations.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tikz-design.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tikz-matrices.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tikz-paths.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tikz-plots.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tikz-scopes.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tikz-shapes.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tikz-transformations.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tikz-transparency.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tikz-trees.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tutorial-Euclid.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tutorial-chains.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tutorial-map.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tutorial-nodes.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tutorial.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-xxcolor.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/plots/pgf-asymptotic-example.gnuplot
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/plots/pgf-asymptotic-example.table
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/plots/pgf-exp.gnuplot
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/plots/pgf-exp.table
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/plots/pgf-parametric-example.gnuplot
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/plots/pgf-parametric-example.table
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/plots/pgf-sin.gnuplot
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/plots/pgf-sin.table
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/plots/pgf-x.gnuplot
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/plots/pgf-x.table
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/plots/pgfmanual-sine.gnuplot
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/plots/pgfmanual-sine.table
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/plots/pgfplotgnuplot-example.gnuplot
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/plots/pgfplotgnuplot-example.table
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/texmf.cnf
%doc %{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfm/en/Makefile
%doc %{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfm/en/pgfmanual.tex
%doc %{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfm/pgfmanual-dvipdfm.cfg
%doc %{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfmx/en/Makefile
%doc %{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfmx/en/pgfmanual.tex
%doc %{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfmx/pgfmanual-dvipdfmx.cfg
%doc %{_texmfdistdir}/doc/generic/pgf/version-for-dvips/en/Makefile
%doc %{_texmfdistdir}/doc/generic/pgf/version-for-dvips/en/pgfmanual.tex
%doc %{_texmfdistdir}/doc/generic/pgf/version-for-dvips/pgfmanual-dvips.cfg
%doc %{_texmfdistdir}/doc/generic/pgf/version-for-pdftex/en/Makefile
%doc %{_texmfdistdir}/doc/generic/pgf/version-for-pdftex/en/pgfmanual.figlist
%doc %{_texmfdistdir}/doc/generic/pgf/version-for-pdftex/en/pgfmanual.tex
%doc %{_texmfdistdir}/doc/generic/pgf/version-for-pdftex/pgfmanual-pdftex.cfg
%doc %{_texmfdistdir}/doc/generic/pgf/version-for-tex4ht/en/Makefile
%doc %{_texmfdistdir}/doc/generic/pgf/version-for-tex4ht/en/pgfmanual.tex
%doc %{_texmfdistdir}/doc/generic/pgf/version-for-tex4ht/pgfmanual-tex4ht.cfg
%doc %{_texmfdistdir}/doc/generic/pgf/version-for-vtex/en/Makefile
%doc %{_texmfdistdir}/doc/generic/pgf/version-for-vtex/en/pgfmanual.tex
%doc %{_texmfdistdir}/doc/generic/pgf/version-for-vtex/pgfmanual-vtex.cfg
%doc %{_texmfdistdir}/doc/generic/pgf/version-for-xetex/en/Makefile
%doc %{_texmfdistdir}/doc/generic/pgf/version-for-xetex/en/pgfmanual.tex
%doc %{_texmfdistdir}/doc/generic/pgf/version-for-xetex/pgfmanual-xetex.cfg
%doc %{_texmfdistdir}/doc/latex/pgf/README
#- source
%doc %{_texmfdistdir}/source/latex/pgf/incoming/GrzegorzMurzynowski/pgfdatabasearrows.pdf
%doc %{_texmfdistdir}/source/latex/pgf/incoming/GrzegorzMurzynowski/pgfdatabasearrows.sty
%doc %{_texmfdistdir}/source/latex/pgf/incoming/GrzegorzMurzynowski/pgfdatabasearrows.tex
%doc %{_texmfdistdir}/source/latex/pgf/incoming/KarlheinzOchs/basics.pdf
%doc %{_texmfdistdir}/source/latex/pgf/incoming/KarlheinzOchs/basics.tex
%doc %{_texmfdistdir}/source/latex/pgf/incoming/KarlheinzOchs/fir.pdf
%doc %{_texmfdistdir}/source/latex/pgf/incoming/KarlheinzOchs/fir.tex
%doc %{_texmfdistdir}/source/latex/pgf/incoming/KarlheinzOchs/interconnection.pdf
%doc %{_texmfdistdir}/source/latex/pgf/incoming/KarlheinzOchs/interconnection.tex
%doc %{_texmfdistdir}/source/latex/pgf/incoming/KarlheinzOchs/macros.sty
%doc %{_texmfdistdir}/source/latex/pgf/incoming/KarlheinzOchs/pgflibrarytikzsignalflowarrows.code.tex
%doc %{_texmfdistdir}/source/latex/pgf/incoming/KarlheinzOchs/pgflibrarytikzsignalflowblocks.code.tex
%doc %{_texmfdistdir}/source/latex/pgf/incoming/KarlheinzOchs/pgflibrarytikzsignalflowdiagram.code.tex
%doc %{_texmfdistdir}/source/latex/pgf/incoming/KarlheinzOchs/pgflibrarytikzsignalflowoperators.code.tex
%doc %{_texmfdistdir}/source/latex/pgf/incoming/KarlheinzOchs/placement.pdf
%doc %{_texmfdistdir}/source/latex/pgf/incoming/KarlheinzOchs/placement.tex
%doc %{_texmfdistdir}/source/latex/pgf/incoming/KarlheinzOchs/signalflowdiagram.sty
%doc %{_texmfdistdir}/source/latex/pgf/testsuite/external/Makefile
%doc %{_texmfdistdir}/source/latex/pgf/testsuite/external/tikzexternaltest.code.tex
%doc %{_texmfdistdir}/source/latex/pgf/testsuite/external/tikzexternaltest.sharedpreamble.tex
%doc %{_texmfdistdir}/source/latex/pgf/testsuite/external/tikzexternaltest.tex
%doc %{_texmfdistdir}/source/latex/pgf/testsuite/external/tikzexternaltestmakefile.tex
%doc %{_texmfdistdir}/source/latex/pgf/testsuite/mathtest/pgfmathtestsuite.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.10-2
+ Revision: 754815
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.10-1
+ Revision: 719240
- texlive-pgf
- texlive-pgf
- texlive-pgf
- texlive-pgf


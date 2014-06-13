# revision 33057
# category Package
# catalog-ctan /graphics/pgf/base
# catalog-date 2014-02-26 21:08:13 +0100
# catalog-license lppl1.3
# catalog-version 3.0.0
Name:		texlive-pgf
Version:	3.0.0
Release:	2
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
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/graphs/tikzlibrarygraphs.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/graphs/tikzlibrarygraphs.standard.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzexternalshared.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrary3d.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryangles.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryarrows.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryautomata.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarybabel.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarybackgrounds.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarybending.code.tex
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
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarymath.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarymatrix.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarymindmap.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarypatterns.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarypetri.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryplothandlers.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryplotmarks.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarypositioning.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryquotes.code.tex
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
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/LUA_CODING_STYLE
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/bindings.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/bindings/Binding.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/bindings/BindingToPGF.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/circular.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/circular/Tantau2012.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/circular/library.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/control.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/control/Anchoring.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/control/ComponentAlign.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/control/ComponentDirection.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/control/ComponentDistance.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/control/ComponentOrder.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/control/Components.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/control/Distances.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/control/FineTune.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/control/LayoutPipeline.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/control/NodeAnchors.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/control/Orientation.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/control/Sublayouts.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/control/library.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/deprecated/Cluster.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/deprecated/Edge.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/deprecated/Graph.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/deprecated/Iterators.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/deprecated/Node.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/deprecated/Vector.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/circular/Tantau2012.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/control/Anchoring.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/FMMMLayout.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/FastMultipoleEmbedder.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/GEMLayout.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/MultilevelLayout.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/SpringEmbedderFR.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/SpringEmbedderFRExact.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/SpringEmbedderKK.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/multilevelmixer/BarycenterPlacer.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/multilevelmixer/CirclePlacer.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/multilevelmixer/EdgeCoverMerger.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/multilevelmixer/IndependentSetMerger.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/multilevelmixer/LocalBiconnectedMerger.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/multilevelmixer/MatchingMerger.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/multilevelmixer/MedianPlacer.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/multilevelmixer/RandomMerger.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/multilevelmixer/RandomPlacer.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/multilevelmixer/SolarMerger.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/multilevelmixer/SolarPlacer.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/multilevelmixer/ZeroPlacer.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/layered.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/layered/BarycenterHeuristic.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/layered/CoffmanGrahamRanking.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/layered/DfsAcyclicSubgraph.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/layered/FastHierarchyLayout.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/layered/FastSimpleHierarchyLayout.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/layered/GreedyCycleRemoval.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/layered/GreedyInsertHeuristic.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/layered/LongestPathRanking.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/layered/MedianHeuristic.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/layered/OptimalRanking.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/layered/SiftingHeuristic.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/layered/SplitHeuristic.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/layered/SugiyamaLayout.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/misclayout.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/misclayout/BalloonLayout.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/misclayout/CircularLayout.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/module/AcyclicSubgraphModule.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/module/HierarchyLayoutModule.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/module/InitialPlacer.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/module/MultilevelBuilder.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/module/RankingModule.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/module/TwoLayerCrossMin.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/planarity.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/planarity/PlanarizationLayout.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/trees/ReingoldTilford1981.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/examples.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/examples/ASCIIDisplayer.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/examples/BindingToASCII.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/examples/SimpleDemo.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/examples/SimpleEdgeDemo.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/examples/SimpleHuffman.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/examples/example_graph_for_ascii_displayer.txt
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/examples/library.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/CoarseGraph.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/Control.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/ControlCoarsening.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/ControlElectric.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/ControlIteration.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/ControlSprings.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/ControlStart.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/QuadTree.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/SpringElectricalHu2006.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/SpringElectricalLayouts.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/SpringElectricalWalshaw2000.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/SpringHu2006.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/SpringLayouts.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/library.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/interface.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/interface/InterfaceCore.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/interface/InterfaceToAlgorithms.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/interface/InterfaceToC.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/interface/InterfaceToDisplay.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/interface/Scope.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/CrossingMinimizationGansnerKNV1993.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/CycleRemovalBergerS1990a.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/CycleRemovalBergerS1990b.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/CycleRemovalEadesLS1993.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/CycleRemovalGansnerKNV1993.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/EdgeRoutingGansnerKNV1993.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/NetworkSimplex.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/NodePositioningGansnerKNV1993.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/NodeRankingGansnerKNV1993.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/NodeRankingMinimumHeight.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/Ranking.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/Sugiyama.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/crossing_minimization.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/cycle_removal.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/edge_routing.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/library.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/node_positioning.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/node_ranking.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/lib.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/lib/Bezier.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/lib/DepthFirstSearch.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/lib/Direct.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/lib/Event.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/lib/LookupTable.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/lib/PathLengths.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/lib/PriorityQueue.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/lib/Simplifiers.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/lib/Stack.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/lib/Storage.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/lib/Transform.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/model.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/model/Arc.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/model/Collection.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/model/Coordinate.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/model/Digraph.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/model/Edge.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/model/Hyperedge.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/model/Path.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/model/Vertex.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/model/library.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/ogdf.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/ogdf/library.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/phylogenetics.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/phylogenetics/AuthorDefinedPhylogeny.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/phylogenetics/BalancedMinimumEvolution.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/phylogenetics/BalancedNearestNeighbourInterchange.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/phylogenetics/DistanceMatrix.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/phylogenetics/Maeusle2012.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/phylogenetics/PhylogeneticTree.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/phylogenetics/SokalMichener1958.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/phylogenetics/library.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/tools/make_gd_wrap.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/trees.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/trees/ChildSpec.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/trees/ReingoldTilford1981.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/trees/SpanningTreeComputation.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/trees/library.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/tex/pgflibrarygraphdrawing.circular.code.tex
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/tex/pgflibrarygraphdrawing.code.tex
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/tex/pgflibrarygraphdrawing.examples.code.tex
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/tex/pgflibrarygraphdrawing.force.code.tex
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/tex/pgflibrarygraphdrawing.layered.code.tex
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/tex/pgflibrarygraphdrawing.trees.code.tex
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/tex/tikzlibrarygraphdrawing.code.tex
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
%{_texmfdistdir}/tex/generic/pgf/libraries/luamath/pgflibraryluamath.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/luamath/pgfluamath.functions.lua
%{_texmfdistdir}/tex/generic/pgf/libraries/luamath/pgfluamath.parser.lua
%{_texmfdistdir}/tex/generic/pgf/libraries/pgflibraryarrows.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/pgflibraryarrows.meta.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/pgflibraryarrows.spaced.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/pgflibrarycurvilinear.code.tex
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
%{_texmfdistdir}/tex/generic/pgf/lua/pgf/manual.lua
%{_texmfdistdir}/tex/generic/pgf/lua/pgf/manual/DocumentParser.lua
%{_texmfdistdir}/tex/generic/pgf/math/pgfmath.code.tex
%{_texmfdistdir}/tex/generic/pgf/math/pgfmathcalc.code.tex
%{_texmfdistdir}/tex/generic/pgf/math/pgfmathfloat.code.tex
%{_texmfdistdir}/tex/generic/pgf/math/pgfmathfunctions.base.code.tex
%{_texmfdistdir}/tex/generic/pgf/math/pgfmathfunctions.basic.code.tex
%{_texmfdistdir}/tex/generic/pgf/math/pgfmathfunctions.code.tex
%{_texmfdistdir}/tex/generic/pgf/math/pgfmathfunctions.comparison.code.tex
%{_texmfdistdir}/tex/generic/pgf/math/pgfmathfunctions.integerarithmetics.code.tex
%{_texmfdistdir}/tex/generic/pgf/math/pgfmathfunctions.misc.code.tex
%{_texmfdistdir}/tex/generic/pgf/math/pgfmathfunctions.random.code.tex
%{_texmfdistdir}/tex/generic/pgf/math/pgfmathfunctions.round.code.tex
%{_texmfdistdir}/tex/generic/pgf/math/pgfmathfunctions.trigonometric.code.tex
%{_texmfdistdir}/tex/generic/pgf/math/pgfmathode.code.tex
%{_texmfdistdir}/tex/generic/pgf/math/pgfmathparser.code.tex
%{_texmfdistdir}/tex/generic/pgf/math/pgfmathutil.code.tex
%{_texmfdistdir}/tex/generic/pgf/modules/pgfmodulebending.code.tex
%{_texmfdistdir}/tex/generic/pgf/modules/pgfmoduledatavisualization.code.tex
%{_texmfdistdir}/tex/generic/pgf/modules/pgfmoduledecorations.code.tex
%{_texmfdistdir}/tex/generic/pgf/modules/pgfmodulematrix.code.tex
%{_texmfdistdir}/tex/generic/pgf/modules/pgfmodulenonlineartransformations.code.tex
%{_texmfdistdir}/tex/generic/pgf/modules/pgfmoduleoo.code.tex
%{_texmfdistdir}/tex/generic/pgf/modules/pgfmoduleparser.code.tex
%{_texmfdistdir}/tex/generic/pgf/modules/pgfmoduleplot.code.tex
%{_texmfdistdir}/tex/generic/pgf/modules/pgfmoduleshapes.code.tex
%{_texmfdistdir}/tex/generic/pgf/modules/pgfmodulesnakes.code.tex
%{_texmfdistdir}/tex/generic/pgf/modules/pgfmodulesorting.code.tex
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgf.cfg
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsys-common-pdf-via-dvi.def
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsys-common-pdf.def
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsys-common-postscript.def
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsys-common-svg.def
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsys-dvi.def
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsys-dvipdfm.def
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsys-dvipdfmx.def
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsys-dvips.def
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsys-dvisvgm.def
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
%{_texmfdistdir}/tex/generic/pgf/utilities/pgfutil-common-lists.tex
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
%doc %{_texmfdistdir}/doc/generic/pgf/images/brave-gnu-world-logo-mask.bb
%doc %{_texmfdistdir}/doc/generic/pgf/images/brave-gnu-world-logo-mask.jpg
%doc %{_texmfdistdir}/doc/generic/pgf/images/brave-gnu-world-logo.25.bb
%doc %{_texmfdistdir}/doc/generic/pgf/images/brave-gnu-world-logo.25.eps
%doc %{_texmfdistdir}/doc/generic/pgf/images/brave-gnu-world-logo.25.jpg
%doc %{_texmfdistdir}/doc/generic/pgf/images/brave-gnu-world-logo.bb
%doc %{_texmfdistdir}/doc/generic/pgf/images/brave-gnu-world-logo.eps
%doc %{_texmfdistdir}/doc/generic/pgf/images/brave-gnu-world-logo.jpg
%doc %{_texmfdistdir}/doc/generic/pgf/images/brave-gnu-world-logo.xbb
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
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-dv-polar.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-dv-stylesheets.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-dv-visualizers.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-gd-algorithm-layer.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-gd-algorithms-in-c.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-gd-binding-layer.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-gd-circular.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-gd-display-layer.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-gd-examples.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-gd-force.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-gd-layered.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-gd-misc.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-gd-ogdf.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-gd-overview.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-gd-phylogenetics.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-gd-trees.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-gd-usage-pgf.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-gd-usage-tikz.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-guidelines.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-installation.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-introduction.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-3d.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-angles.tex
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
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-math.tex
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
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-main-body.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-main-preamble.tex
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
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tikz-arrows.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tikz-coordinates.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tikz-decorations.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tikz-design.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tikz-graphs.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tikz-matrices.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tikz-paths.tex
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tikz-pics.tex
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
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/plots/pgf-tan-example.gnuplot
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/plots/pgf-tan-example.table
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/plots/pgf-x.gnuplot
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/plots/pgf-x.table
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/plots/pgfmanual-sine.gnuplot
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/plots/pgfmanual-sine.table
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/plots/pgfplotgnuplot-example.gnuplot
%doc %{_texmfdistdir}/doc/generic/pgf/text-en/plots/pgfplotgnuplot-example.table
%doc %{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfm/en/Makefile
%doc %{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfm/en/pgfmanual.tex
%doc %{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfm/pgfmanual-dvipdfm.cfg
%doc %{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfmx/en/Makefile
%doc %{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfmx/en/pgfmanual-test.tex
%doc %{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfmx/en/pgfmanual.tex
%doc %{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfmx/pgfmanual-dvipdfmx.cfg
%doc %{_texmfdistdir}/doc/generic/pgf/version-for-dvips/en/Makefile
%doc %{_texmfdistdir}/doc/generic/pgf/version-for-dvips/en/pgfmanual.tex
%doc %{_texmfdistdir}/doc/generic/pgf/version-for-dvips/pgfmanual-dvips.cfg
%doc %{_texmfdistdir}/doc/generic/pgf/version-for-luatex/en/Makefile
%doc %{_texmfdistdir}/doc/generic/pgf/version-for-luatex/en/pgfmanual-test.tex
%doc %{_texmfdistdir}/doc/generic/pgf/version-for-luatex/en/pgfmanual.tex
%doc %{_texmfdistdir}/doc/generic/pgf/version-for-luatex/pgfmanual-luatex.cfg
%doc %{_texmfdistdir}/doc/generic/pgf/version-for-pdftex/en/Makefile
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
#- source
%doc %{_texmfdistdir}/source/generic/pgf/c/INSTALL
%doc %{_texmfdistdir}/source/generic/pgf/c/Makefile
%doc %{_texmfdistdir}/source/generic/pgf/c/config/ExampleLocalMakefileConfig.mk
%doc %{_texmfdistdir}/source/generic/pgf/c/config/MakefileConfig.mk
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/examples/c/Makefile
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/examples/c/SimpleDemoC.c
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/examples/c/SimpleDemoCPlusPlus.c++
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/interface/c/InterfaceFromC++.c++
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/interface/c/InterfaceFromC++.h
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/interface/c/InterfaceFromC.c
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/interface/c/InterfaceFromC.h
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/interface/c/Makefile
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/InterfaceFromOGDF.c++
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/InterfaceFromOGDF.h
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/Makefile
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/SimpleDemoOGDF.c++
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/energybased/FMMMLayout_script.h
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/energybased/FastMultipoleEmbedder_script.h
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/energybased/GEMLayout_script.h
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/energybased/MultilevelLayout_script.h
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/energybased/SpringEmbedderFRExact_script.h
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/energybased/SpringEmbedderFR_script.h
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/energybased/SpringEmbedderKK_script.h
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/energybased/energybased_script.h
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/energybased/multilevelmixer/BarycenterPlacer_script.h
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/energybased/multilevelmixer/CirclePlacer_script.h
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/energybased/multilevelmixer/EdgeCoverMerger_script.h
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/energybased/multilevelmixer/IndependentSetMerger_script.h
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/energybased/multilevelmixer/LocalBiconnectedMerger_script.h
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/energybased/multilevelmixer/MatchingMerger_script.h
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/energybased/multilevelmixer/MedianPlacer_script.h
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/energybased/multilevelmixer/RandomMerger_script.h
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/energybased/multilevelmixer/RandomPlacer_script.h
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/energybased/multilevelmixer/SolarMerger_script.h
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/energybased/multilevelmixer/SolarPlacer_script.h
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/energybased/multilevelmixer/ZeroPlacer_script.h
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/energybased/multilevelmixer/multilevelmixer_script.h
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/layered/BarycenterHeuristic_script.h
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/layered/CoffmanGrahamRanking_script.h
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/layered/DfsAcyclicSubgraph_script.h
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/layered/FastHierarchyLayout_script.h
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/layered/FastSimpleHierarchyLayout_script.h
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/layered/GreedyCycleRemoval_script.h
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/layered/GreedyInsertHeuristic_script.h
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/layered/LongestPathRanking_script.h
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/layered/MedianHeuristic_script.h
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/layered/OptimalRanking_script.h
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/layered/SiftingHeuristic_script.h
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/layered/SplitHeuristic_script.h
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/layered/SugiyamaLayout_script.h
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/layered/layered_script.h
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/misclayout/BalloonLayout_script.h
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/misclayout/CircularLayout_script.h
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/misclayout/misclayout_script.h
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/module/module_script.h
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/ogdf_script.c++
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/planarity/PlanarizationLayout_script.h
%doc %{_texmfdistdir}/source/generic/pgf/c/graphdrawing/pgf/gd/ogdf/c/planarity/planarity_script.h
%doc %{_texmfdistdir}/source/generic/pgf/testsuite/external/Makefile
%doc %{_texmfdistdir}/source/generic/pgf/testsuite/external/tikzexternaltest.code.tex
%doc %{_texmfdistdir}/source/generic/pgf/testsuite/external/tikzexternaltest.sharedpreamble.tex
%doc %{_texmfdistdir}/source/generic/pgf/testsuite/external/tikzexternaltest.tex
%doc %{_texmfdistdir}/source/generic/pgf/testsuite/external/tikzexternaltestmakefile.tex
%doc %{_texmfdistdir}/source/generic/pgf/testsuite/mathtest/pgfmathtestsuite.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

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
Requires(pre):	texlive-tlpkg
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

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/generic
%dir %{_datadir}/texmf-dist/tex/context
%dir %{_datadir}/texmf-dist/tex/generic
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/tex/plain
%dir %{_datadir}/texmf-dist/doc/generic/pgf
%dir %{_datadir}/texmf-dist/tex/context/third
%dir %{_datadir}/texmf-dist/tex/generic/pgf
%dir %{_datadir}/texmf-dist/tex/latex/pgf
%dir %{_datadir}/texmf-dist/tex/plain/pgf
%dir %{_datadir}/texmf-dist/doc/generic/pgf/images
%dir %{_datadir}/texmf-dist/doc/generic/pgf/plots
%dir %{_datadir}/texmf-dist/tex/context/third/pgf
%dir %{_datadir}/texmf-dist/tex/generic/pgf/basiclayer
%dir %{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer
%dir %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing
%dir %{_datadir}/texmf-dist/tex/generic/pgf/libraries
%dir %{_datadir}/texmf-dist/tex/generic/pgf/lua
%dir %{_datadir}/texmf-dist/tex/generic/pgf/math
%dir %{_datadir}/texmf-dist/tex/generic/pgf/modules
%dir %{_datadir}/texmf-dist/tex/generic/pgf/systemlayer
%dir %{_datadir}/texmf-dist/tex/generic/pgf/utilities
%dir %{_datadir}/texmf-dist/tex/latex/pgf/basiclayer
%dir %{_datadir}/texmf-dist/tex/latex/pgf/compatibility
%dir %{_datadir}/texmf-dist/tex/latex/pgf/doc
%dir %{_datadir}/texmf-dist/tex/latex/pgf/frontendlayer
%dir %{_datadir}/texmf-dist/tex/latex/pgf/math
%dir %{_datadir}/texmf-dist/tex/latex/pgf/systemlayer
%dir %{_datadir}/texmf-dist/tex/latex/pgf/utilities
%dir %{_datadir}/texmf-dist/tex/plain/pgf/basiclayer
%dir %{_datadir}/texmf-dist/tex/plain/pgf/frontendlayer
%dir %{_datadir}/texmf-dist/tex/plain/pgf/math
%dir %{_datadir}/texmf-dist/tex/plain/pgf/systemlayer
%dir %{_datadir}/texmf-dist/tex/plain/pgf/utilities
%dir %{_datadir}/texmf-dist/tex/context/third/pgf/basiclayer
%dir %{_datadir}/texmf-dist/tex/context/third/pgf/frontendlayer
%dir %{_datadir}/texmf-dist/tex/context/third/pgf/math
%dir %{_datadir}/texmf-dist/tex/context/third/pgf/systemlayer
%dir %{_datadir}/texmf-dist/tex/context/third/pgf/utilities
%dir %{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz
%dir %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua
%dir %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/tex
%dir %{_datadir}/texmf-dist/tex/generic/pgf/libraries/datavisualization
%dir %{_datadir}/texmf-dist/tex/generic/pgf/libraries/decorations
%dir %{_datadir}/texmf-dist/tex/generic/pgf/libraries/luamath
%dir %{_datadir}/texmf-dist/tex/generic/pgf/libraries/shapes
%dir %{_datadir}/texmf-dist/tex/generic/pgf/lua/pgf
%dir %{_datadir}/texmf-dist/tex/latex/pgf/frontendlayer/libraries
%dir %{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries
%dir %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf
%dir %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/tex/experimental
%dir %{_datadir}/texmf-dist/tex/generic/pgf/libraries/luamath/pgf
%dir %{_datadir}/texmf-dist/tex/generic/pgf/libraries/shapes/circuits
%dir %{_datadir}/texmf-dist/tex/generic/pgf/lua/pgf/manual
%dir %{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/circuits
%dir %{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/datavisualization
%dir %{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/graphs
%dir %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd
%dir %{_datadir}/texmf-dist/tex/generic/pgf/libraries/luamath/pgf/luamath
%dir %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/bindings
%dir %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/circular
%dir %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/control
%dir %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/deprecated
%dir %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc
%dir %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/examples
%dir %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/experimental
%dir %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/force
%dir %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/interface
%dir %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered
%dir %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/lib
%dir %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/model
%dir %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/ogdf
%dir %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/pedigrees
%dir %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/phylogenetics
%dir %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/planar
%dir %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/routing
%dir %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/tools
%dir %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/trees
%dir %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf
%dir %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/experimental/evolving
%dir %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi
%dir %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased
%dir %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/layered
%dir %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/misclayout
%dir %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/module
%dir %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/planarity
%dir %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/algorithms
%dir %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/base
%dir %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/forcetypes
%dir %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/initialpositioning
%dir %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/multilevelmixer
%doc %{_datadir}/texmf-dist/doc/generic/pgf/CHANGELOG.md
%doc %{_datadir}/texmf-dist/doc/generic/pgf/CTAN_NOTES.md
%doc %{_datadir}/texmf-dist/doc/generic/pgf/README.md
%doc %{_datadir}/texmf-dist/doc/generic/pgf/RELEASE_NOTES.md
%doc %{_datadir}/texmf-dist/doc/generic/pgf/color.cfg
%doc %{_datadir}/texmf-dist/doc/generic/pgf/description.html
%doc %{_datadir}/texmf-dist/doc/generic/pgf/images/brave-gnu-world-logo-mask.bb
%doc %{_datadir}/texmf-dist/doc/generic/pgf/images/brave-gnu-world-logo-mask.eps
%doc %{_datadir}/texmf-dist/doc/generic/pgf/images/brave-gnu-world-logo-mask.jpg
%doc %{_datadir}/texmf-dist/doc/generic/pgf/images/brave-gnu-world-logo.25.bb
%doc %{_datadir}/texmf-dist/doc/generic/pgf/images/brave-gnu-world-logo.25.eps
%doc %{_datadir}/texmf-dist/doc/generic/pgf/images/brave-gnu-world-logo.25.jpg
%doc %{_datadir}/texmf-dist/doc/generic/pgf/images/brave-gnu-world-logo.bb
%doc %{_datadir}/texmf-dist/doc/generic/pgf/images/brave-gnu-world-logo.eps
%doc %{_datadir}/texmf-dist/doc/generic/pgf/images/brave-gnu-world-logo.jpg
%doc %{_datadir}/texmf-dist/doc/generic/pgf/images/brave-gnu-world-logo.xbb
%doc %{_datadir}/texmf-dist/doc/generic/pgf/images/pgfmanual-mindmap-1.pdf
%doc %{_datadir}/texmf-dist/doc/generic/pgf/images/pgfmanual-mindmap-2.pdf
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-base-actions.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-base-animations.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-base-arrows.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-base-decorations.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-base-design.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-base-external.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-base-images.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-base-internalregisters.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-base-layers.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-base-matrices.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-base-nodes.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-base-paths.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-base-patterns.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-base-plots.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-base-points.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-base-quick.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-base-scopes.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-base-shadings.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-base-transformations.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-base-transparency.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-drivers.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-dv-axes.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-dv-backend.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-dv-examples.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-dv-formats.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-dv-introduction.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-dv-main.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-dv-polar.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-dv-stylesheets.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-dv-visualizers.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-gd-algorithm-layer.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-gd-algorithms-in-c.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-gd-binding-layer.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-gd-circular.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-gd-display-layer.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-gd-edge-routing.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-gd-examples.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-gd-force.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-gd-layered.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-gd-misc.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-gd-ogdf.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-gd-overview.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-gd-phylogenetics.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-gd-trees.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-gd-usage-pgf.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-gd-usage-tikz.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-guidelines.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-installation.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-introduction.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-library-3d.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-library-angles.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-library-arrows.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-library-automata.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-library-babel.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-library-backgrounds.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-library-calc.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-library-calendar.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-library-chains.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-library-circuits.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-library-decorations.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-library-edges.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-library-er.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-library-external.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-library-fadings.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-library-fit.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-library-fixedpoint.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-library-folding.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-library-fpu.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-library-lsystems.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-library-math.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-library-matrices.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-library-mindmaps.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-library-patterns.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-library-perspective.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-library-petri.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-library-plot-handlers.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-library-plot-marks.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-library-profiler.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-library-rdf.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-library-shadings.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-library-shadows.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-library-shapes.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-library-spy.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-library-svg-path.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-library-through.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-library-trees.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-library-turtle.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-library-views.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-license.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-main-body.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-main-preamble.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-main.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-math-algorithms.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-math-commands.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-math-design.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-math-numberprinting.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-math-parsing.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-module-parser.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-oo.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-pages.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-pgfcalendar.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-pgffor.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-pgfkeys.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-pgfkeysfiltered.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-pgfsys-animations.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-pgfsys-commands.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-pgfsys-overview.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-pgfsys-paths.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-pgfsys-protocol.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-tikz-actions.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-tikz-animations.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-tikz-arrows.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-tikz-coordinates.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-tikz-decorations.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-tikz-design.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-tikz-graphs.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-tikz-matrices.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-tikz-paths.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-tikz-pics.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-tikz-plots.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-tikz-scopes.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-tikz-shapes.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-tikz-transformations.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-tikz-transparency.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-tikz-trees.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-tutorial-Euclid.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-tutorial-chains.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-tutorial-map.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-tutorial-nodes.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-tutorial.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-en-xxcolor.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual-test.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual.cfg
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual.pdf
%doc %{_datadir}/texmf-dist/doc/generic/pgf/pgfmanual.tex
%doc %{_datadir}/texmf-dist/doc/generic/pgf/plots/pgf-asymptotic-example.gnuplot
%doc %{_datadir}/texmf-dist/doc/generic/pgf/plots/pgf-asymptotic-example.table
%doc %{_datadir}/texmf-dist/doc/generic/pgf/plots/pgf-exp.gnuplot
%doc %{_datadir}/texmf-dist/doc/generic/pgf/plots/pgf-exp.table
%doc %{_datadir}/texmf-dist/doc/generic/pgf/plots/pgf-parametric-example-cut.gnuplot
%doc %{_datadir}/texmf-dist/doc/generic/pgf/plots/pgf-parametric-example-cut.table
%doc %{_datadir}/texmf-dist/doc/generic/pgf/plots/pgf-parametric-example.gnuplot
%doc %{_datadir}/texmf-dist/doc/generic/pgf/plots/pgf-parametric-example.table
%doc %{_datadir}/texmf-dist/doc/generic/pgf/plots/pgf-sin.gnuplot
%doc %{_datadir}/texmf-dist/doc/generic/pgf/plots/pgf-sin.table
%doc %{_datadir}/texmf-dist/doc/generic/pgf/plots/pgf-tan-example.gnuplot
%doc %{_datadir}/texmf-dist/doc/generic/pgf/plots/pgf-tan-example.table
%doc %{_datadir}/texmf-dist/doc/generic/pgf/plots/pgf-x.gnuplot
%doc %{_datadir}/texmf-dist/doc/generic/pgf/plots/pgf-x.table
%doc %{_datadir}/texmf-dist/doc/generic/pgf/plots/pgfmanual-sine.gnuplot
%doc %{_datadir}/texmf-dist/doc/generic/pgf/plots/pgfmanual-sine.table
%doc %{_datadir}/texmf-dist/doc/generic/pgf/plots/pgfplotgnuplot-example.gnuplot
%doc %{_datadir}/texmf-dist/doc/generic/pgf/plots/pgfplotgnuplot-example.table
%{_datadir}/texmf-dist/tex/context/third/pgf/basiclayer/t-pgf.tex
%{_datadir}/texmf-dist/tex/context/third/pgf/basiclayer/t-pgfbim.tex
%{_datadir}/texmf-dist/tex/context/third/pgf/basiclayer/t-pgfbla.tex
%{_datadir}/texmf-dist/tex/context/third/pgf/basiclayer/t-pgfbma.tex
%{_datadir}/texmf-dist/tex/context/third/pgf/basiclayer/t-pgfbpl.tex
%{_datadir}/texmf-dist/tex/context/third/pgf/basiclayer/t-pgfbpt.tex
%{_datadir}/texmf-dist/tex/context/third/pgf/basiclayer/t-pgfbsh.tex
%{_datadir}/texmf-dist/tex/context/third/pgf/basiclayer/t-pgfbsn.tex
%{_datadir}/texmf-dist/tex/context/third/pgf/basiclayer/t-pgfcor.tex
%{_datadir}/texmf-dist/tex/context/third/pgf/frontendlayer/t-tikz.tex
%{_datadir}/texmf-dist/tex/context/third/pgf/math/t-pgfmat.tex
%{_datadir}/texmf-dist/tex/context/third/pgf/systemlayer/t-pgfsys.tex
%{_datadir}/texmf-dist/tex/context/third/pgf/utilities/t-pgfcal.tex
%{_datadir}/texmf-dist/tex/context/third/pgf/utilities/t-pgffor.tex
%{_datadir}/texmf-dist/tex/context/third/pgf/utilities/t-pgfkey.tex
%{_datadir}/texmf-dist/tex/context/third/pgf/utilities/t-pgfmod.tex
%{_datadir}/texmf-dist/tex/context/third/pgf/utilities/t-pgfrcs.tex
%{_datadir}/texmf-dist/tex/generic/pgf/basiclayer/pgfcore.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/basiclayer/pgfcorearrows.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/basiclayer/pgfcoreexternal.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/basiclayer/pgfcoregraphicstate.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/basiclayer/pgfcoreimage.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/basiclayer/pgfcorelayers.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/basiclayer/pgfcoreobjects.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/basiclayer/pgfcorepathconstruct.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/basiclayer/pgfcorepathprocessing.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/basiclayer/pgfcorepathusage.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/basiclayer/pgfcorepatterns.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/basiclayer/pgfcorepoints.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/basiclayer/pgfcorequick.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/basiclayer/pgfcorerdf.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/basiclayer/pgfcorescopes.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/basiclayer/pgfcoreshade.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/basiclayer/pgfcoretransformations.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/basiclayer/pgfcoretransparency.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/circuits/tikzlibrarycircuits.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/circuits/tikzlibrarycircuits.ee.IEC.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/circuits/tikzlibrarycircuits.ee.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/circuits/tikzlibrarycircuits.logic.CDH.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/circuits/tikzlibrarycircuits.logic.IEC.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/circuits/tikzlibrarycircuits.logic.US.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/circuits/tikzlibrarycircuits.logic.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/datavisualization/tikzlibrarydatavisualization.3d.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/datavisualization/tikzlibrarydatavisualization.barcharts.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/datavisualization/tikzlibrarydatavisualization.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/datavisualization/tikzlibrarydatavisualization.formats.functions.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/datavisualization/tikzlibrarydatavisualization.polar.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/datavisualization/tikzlibrarydatavisualization.sparklines.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/graphs/tikzlibrarygraphs.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/graphs/tikzlibrarygraphs.standard.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzexternalshared.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrary3d.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryangles.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryanimations.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryarrows.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryautomata.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarybabel.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarybackgrounds.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarybending.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarycalc.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarycalendar.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarychains.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarydecorations.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarydecorations.footprints.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarydecorations.fractals.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarydecorations.markings.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarydecorations.pathmorphing.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarydecorations.pathreplacing.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarydecorations.shapes.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarydecorations.text.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryer.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryfadings.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryfit.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryfixedpointarithmetic.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryfolding.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryfpu.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryintersections.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarylindenmayersystems.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarymath.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarymatrix.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarymindmap.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarypatterns.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarypatterns.meta.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryperspective.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarypetri.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryplothandlers.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryplotmarks.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarypositioning.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryquotes.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryrdf.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryscopes.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryshadings.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryshadows.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryshapes.arrows.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryshapes.callouts.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryshapes.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryshapes.gates.logic.IEC.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryshapes.gates.logic.US.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryshapes.geometric.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryshapes.misc.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryshapes.multipart.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryshapes.symbols.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarysnakes.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryspy.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarysvg.path.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarythrough.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarytopaths.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarytrees.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryturtle.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryviews.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/tikz.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/LUA_CODING_STYLE
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/bindings.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/bindings/Binding.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/bindings/BindingToPGF.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/circular.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/circular/Tantau2012.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/circular/doc.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/circular/library.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/control.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/control/Anchoring.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/control/ComponentAlign.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/control/ComponentDirection.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/control/ComponentDistance.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/control/ComponentOrder.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/control/Components.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/control/Distances.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/control/FineTune.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/control/LayoutPipeline.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/control/NodeAnchors.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/control/Orientation.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/control/Sublayouts.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/control/doc.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/control/library.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/deprecated/Cluster.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/deprecated/Edge.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/deprecated/Graph.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/deprecated/Iterators.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/deprecated/Node.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/deprecated/Vector.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/FMMMLayout.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/FastMultipoleEmbedder.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/GEMLayout.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/MultilevelLayout.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/SpringEmbedderFR.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/SpringEmbedderFRExact.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/SpringEmbedderKK.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/multilevelmixer/BarycenterPlacer.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/multilevelmixer/CirclePlacer.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/multilevelmixer/EdgeCoverMerger.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/multilevelmixer/IndependentSetMerger.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/multilevelmixer/LocalBiconnectedMerger.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/multilevelmixer/MatchingMerger.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/multilevelmixer/MedianPlacer.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/multilevelmixer/RandomMerger.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/multilevelmixer/RandomPlacer.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/multilevelmixer/SolarMerger.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/multilevelmixer/SolarPlacer.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/multilevelmixer/ZeroPlacer.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/layered.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/layered/BarycenterHeuristic.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/layered/CoffmanGrahamRanking.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/layered/DfsAcyclicSubgraph.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/layered/FastHierarchyLayout.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/layered/FastSimpleHierarchyLayout.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/layered/GreedyCycleRemoval.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/layered/GreedyInsertHeuristic.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/layered/LongestPathRanking.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/layered/MedianHeuristic.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/layered/OptimalRanking.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/layered/SiftingHeuristic.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/layered/SplitHeuristic.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/layered/SugiyamaLayout.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/misclayout.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/misclayout/BalloonLayout.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/misclayout/CircularLayout.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/module/AcyclicSubgraphModule.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/module/HierarchyLayoutModule.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/module/InitialPlacer.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/module/MultilevelBuilder.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/module/RankingModule.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/module/TwoLayerCrossMin.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/planarity.lua
%doc %{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/planarity/PlanarizationLayout.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/examples.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/examples/ASCIIDisplayer.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/examples/BindingToASCII.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/examples/SimpleDemo.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/examples/SimpleEdgeDemo.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/examples/SimpleHuffman.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/examples/example_graph_for_ascii_displayer.txt
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/examples/library.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/experimental/evolving/GraphAnimationCoordination.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/experimental/evolving/GreedyTemporalCycleRemoval.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/experimental/evolving/Skambath2016.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/experimental/evolving/Supergraph.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/experimental/evolving/SupergraphVertexSplitOptimization.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/experimental/evolving/TimeSpec.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/experimental/evolving/doc.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/experimental/evolving/layered.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/experimental/evolving/library.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/force.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/CoarseGraph.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/ControlCoarsening.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/ControlDeclare.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/ControlElectric.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/ControlIteration.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/ControlSprings.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/ControlStart.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/QuadTree.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/SpringElectricalHu2006.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/SpringElectricalLayouts.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/SpringElectricalWalshaw2000.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/SpringHu2006.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/SpringLayouts.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/algorithms/FruchtermanReingold.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/algorithms/HuSpringElectricalFW.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/algorithms/SimpleSpring.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/algorithms/SocialGravityCloseness.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/algorithms/SocialGravityDegree.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/base/CoarseGraphFW.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/base/ForceController.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/base/ForceTemplate.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/base/InitialTemplate.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/base/PathLengthsFW.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/base/Preprocessing.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/doc.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/forcetypes/ForceAbsoluteValue.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/forcetypes/ForceCanvasDistance.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/forcetypes/ForceCanvasPosition.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/forcetypes/ForceGraphDistance.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/forcetypes/ForcePullToGrid.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/forcetypes/ForcePullToPoint.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/initialpositioning/CircularInitialPositioning.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/initialpositioning/GridInitialPositioning.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/initialpositioning/RandomInitialPositioning.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/library.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/library.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/interface.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/interface/InterfaceCore.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/interface/InterfaceToAlgorithms.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/interface/InterfaceToC.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/interface/InterfaceToDisplay.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/interface/Scope.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/CrossingMinimizationGansnerKNV1993.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/CycleRemovalBergerS1990a.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/CycleRemovalBergerS1990b.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/CycleRemovalEadesLS1993.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/CycleRemovalGansnerKNV1993.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/EdgeRoutingGansnerKNV1993.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/NetworkSimplex.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/NodePositioningGansnerKNV1993.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/NodeRankingGansnerKNV1993.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/NodeRankingMinimumHeight.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/Ranking.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/Sugiyama.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/crossing_minimization.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/cycle_removal.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/edge_routing.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/library.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/node_positioning.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/node_ranking.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/lib.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/lib/Bezier.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/lib/DepthFirstSearch.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/lib/Direct.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/lib/Event.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/lib/LookupTable.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/lib/PathLengths.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/lib/PriorityQueue.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/lib/Simplifiers.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/lib/Stack.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/lib/Storage.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/lib/Transform.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/model.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/model/Arc.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/model/Collection.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/model/Coordinate.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/model/Digraph.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/model/Edge.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/model/Hyperedge.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/model/Path.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/model/Path_arced.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/model/Vertex.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/model/library.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/ogdf.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/ogdf/library.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/pedigrees.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/pedigrees/Koerner2015.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/pedigrees/library.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/phylogenetics.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/phylogenetics/AuthorDefinedPhylogeny.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/phylogenetics/BalancedMinimumEvolution.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/phylogenetics/BalancedNearestNeighbourInterchange.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/phylogenetics/DistanceMatrix.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/phylogenetics/Maeusle2012.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/phylogenetics/PhylogeneticTree.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/phylogenetics/SokalMichener1958.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/phylogenetics/library.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/planar.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/planar/BoyerMyrvold2004.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/planar/Embedding.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/planar/LinkedList.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/planar/List.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/planar/PDP.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/planar/PlanarLayout.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/planar/ShiftMethod.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/planar/library.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/planar/parameters.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/routing.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/routing/Hints.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/routing/NecklaceRouting.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/routing/library.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/tools/make_gd_wrap.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/trees.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/trees/ChildSpec.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/trees/ReingoldTilford1981.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/trees/SpanningTreeComputation.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/trees/doc.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/lua/pgf/gd/trees/library.lua
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/tex/experimental/tikzlibrarygraphdrawing.evolving.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/tex/pgflibrarygraphdrawing.circular.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/tex/pgflibrarygraphdrawing.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/tex/pgflibrarygraphdrawing.examples.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/tex/pgflibrarygraphdrawing.force.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/tex/pgflibrarygraphdrawing.layered.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/tex/pgflibrarygraphdrawing.trees.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/graphdrawing/tex/tikzlibrarygraphdrawing.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/libraries/datavisualization/pgflibrarydatavisualization.barcharts.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/libraries/datavisualization/pgflibrarydatavisualization.formats.functions.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/libraries/datavisualization/pgflibrarydatavisualization.polar.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/libraries/decorations/pgflibrarydecorations.footprints.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/libraries/decorations/pgflibrarydecorations.fractals.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/libraries/decorations/pgflibrarydecorations.markings.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/libraries/decorations/pgflibrarydecorations.pathmorphing.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/libraries/decorations/pgflibrarydecorations.pathreplacing.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/libraries/decorations/pgflibrarydecorations.shapes.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/libraries/decorations/pgflibrarydecorations.text.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/libraries/luamath/pgf/luamath/functions.lua
%{_datadir}/texmf-dist/tex/generic/pgf/libraries/luamath/pgf/luamath/parser.lua
%{_datadir}/texmf-dist/tex/generic/pgf/libraries/luamath/pgflibraryluamath.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/libraries/pgflibraryarrows.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/libraries/pgflibraryarrows.meta.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/libraries/pgflibraryarrows.spaced.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/libraries/pgflibrarycurvilinear.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/libraries/pgflibraryfadings.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/libraries/pgflibraryfixedpointarithmetic.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/libraries/pgflibraryfpu.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/libraries/pgflibraryintersections.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/libraries/pgflibrarylindenmayersystems.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/libraries/pgflibrarypatterns.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/libraries/pgflibrarypatterns.meta.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/libraries/pgflibraryplothandlers.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/libraries/pgflibraryplotmarks.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/libraries/pgflibraryprofiler.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/libraries/pgflibraryshadings.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/libraries/pgflibrarysnakes.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/libraries/pgflibrarysvg.path.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/libraries/pgflibrarytimelines.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/libraries/shapes/circuits/pgflibraryshapes.gates.ee.IEC.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/libraries/shapes/circuits/pgflibraryshapes.gates.ee.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/libraries/shapes/circuits/pgflibraryshapes.gates.logic.IEC.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/libraries/shapes/circuits/pgflibraryshapes.gates.logic.US.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/libraries/shapes/circuits/pgflibraryshapes.gates.logic.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/libraries/shapes/pgflibraryshapes.arrows.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/libraries/shapes/pgflibraryshapes.callouts.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/libraries/shapes/pgflibraryshapes.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/libraries/shapes/pgflibraryshapes.geometric.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/libraries/shapes/pgflibraryshapes.misc.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/libraries/shapes/pgflibraryshapes.multipart.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/libraries/shapes/pgflibraryshapes.symbols.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/lua/pgf/manual.lua
%{_datadir}/texmf-dist/tex/generic/pgf/lua/pgf/manual/DocumentParser.lua
%{_datadir}/texmf-dist/tex/generic/pgf/math/pgfint.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/math/pgfmath.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/math/pgfmathcalc.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/math/pgfmathfloat.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.base.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.basic.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.comparison.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.integerarithmetics.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.misc.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.random.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.round.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.trigonometric.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/math/pgfmathode.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/math/pgfmathparser.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/math/pgfmathutil.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/modules/pgfmoduleanimations.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/modules/pgfmodulebending.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/modules/pgfmoduledatavisualization.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/modules/pgfmoduledecorations.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/modules/pgfmodulematrix.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/modules/pgfmodulenonlineartransformations.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/modules/pgfmoduleoo.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/modules/pgfmoduleparser.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/modules/pgfmoduleplot.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/modules/pgfmoduleshapes.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/modules/pgfmodulesnakes.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/modules/pgfmodulesorting.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/pgf.revision.tex
%{_datadir}/texmf-dist/tex/generic/pgf/systemlayer/pgf.cfg
%{_datadir}/texmf-dist/tex/generic/pgf/systemlayer/pgfsys-common-pdf-via-dvi.def
%{_datadir}/texmf-dist/tex/generic/pgf/systemlayer/pgfsys-common-pdf.def
%{_datadir}/texmf-dist/tex/generic/pgf/systemlayer/pgfsys-common-postscript.def
%{_datadir}/texmf-dist/tex/generic/pgf/systemlayer/pgfsys-common-svg.def
%{_datadir}/texmf-dist/tex/generic/pgf/systemlayer/pgfsys-dvi.def
%{_datadir}/texmf-dist/tex/generic/pgf/systemlayer/pgfsys-dvipdfm.def
%{_datadir}/texmf-dist/tex/generic/pgf/systemlayer/pgfsys-dvipdfmx.def
%{_datadir}/texmf-dist/tex/generic/pgf/systemlayer/pgfsys-dvips.def
%{_datadir}/texmf-dist/tex/generic/pgf/systemlayer/pgfsys-dvisvgm.def
%{_datadir}/texmf-dist/tex/generic/pgf/systemlayer/pgfsys-dvisvgm4ht.def
%{_datadir}/texmf-dist/tex/generic/pgf/systemlayer/pgfsys-luatex.def
%{_datadir}/texmf-dist/tex/generic/pgf/systemlayer/pgfsys-pdftex.def
%{_datadir}/texmf-dist/tex/generic/pgf/systemlayer/pgfsys-tex4ht.def
%{_datadir}/texmf-dist/tex/generic/pgf/systemlayer/pgfsys-textures.def
%{_datadir}/texmf-dist/tex/generic/pgf/systemlayer/pgfsys-vtex.def
%{_datadir}/texmf-dist/tex/generic/pgf/systemlayer/pgfsys-xetex.def
%{_datadir}/texmf-dist/tex/generic/pgf/systemlayer/pgfsys.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/systemlayer/pgfsysanimations.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/systemlayer/pgfsysprotocol.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/systemlayer/pgfsyssoftpath.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/utilities/pgfcalendar.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/utilities/pgfexternal.tex
%{_datadir}/texmf-dist/tex/generic/pgf/utilities/pgfexternalwithdepth.tex
%{_datadir}/texmf-dist/tex/generic/pgf/utilities/pgffor.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/utilities/pgfkeys.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/utilities/pgfkeyslibraryfiltered.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/utilities/pgfrcs.code.tex
%{_datadir}/texmf-dist/tex/generic/pgf/utilities/pgfutil-common-lists.tex
%{_datadir}/texmf-dist/tex/generic/pgf/utilities/pgfutil-common.tex
%{_datadir}/texmf-dist/tex/generic/pgf/utilities/pgfutil-context.def
%{_datadir}/texmf-dist/tex/generic/pgf/utilities/pgfutil-latex.def
%{_datadir}/texmf-dist/tex/generic/pgf/utilities/pgfutil-plain.def
%{_datadir}/texmf-dist/tex/latex/pgf/basiclayer/pgf.sty
%{_datadir}/texmf-dist/tex/latex/pgf/basiclayer/pgfbaseimage.sty
%{_datadir}/texmf-dist/tex/latex/pgf/basiclayer/pgfbaselayers.sty
%{_datadir}/texmf-dist/tex/latex/pgf/basiclayer/pgfbasematrix.sty
%{_datadir}/texmf-dist/tex/latex/pgf/basiclayer/pgfbasepatterns.sty
%{_datadir}/texmf-dist/tex/latex/pgf/basiclayer/pgfbaseplot.sty
%{_datadir}/texmf-dist/tex/latex/pgf/basiclayer/pgfbaseshapes.sty
%{_datadir}/texmf-dist/tex/latex/pgf/basiclayer/pgfbasesnakes.sty
%{_datadir}/texmf-dist/tex/latex/pgf/basiclayer/pgfcore.sty
%{_datadir}/texmf-dist/tex/latex/pgf/compatibility/pgfarrows.sty
%{_datadir}/texmf-dist/tex/latex/pgf/compatibility/pgfautomata.sty
%{_datadir}/texmf-dist/tex/latex/pgf/compatibility/pgfcomp-version-0-65.sty
%{_datadir}/texmf-dist/tex/latex/pgf/compatibility/pgfcomp-version-1-18.sty
%{_datadir}/texmf-dist/tex/latex/pgf/compatibility/pgfheaps.sty
%{_datadir}/texmf-dist/tex/latex/pgf/compatibility/pgflibraryarrows.sty
%{_datadir}/texmf-dist/tex/latex/pgf/compatibility/pgflibraryautomata.sty
%{_datadir}/texmf-dist/tex/latex/pgf/compatibility/pgflibraryplothandlers.sty
%{_datadir}/texmf-dist/tex/latex/pgf/compatibility/pgflibraryplotmarks.sty
%{_datadir}/texmf-dist/tex/latex/pgf/compatibility/pgflibraryshapes.sty
%{_datadir}/texmf-dist/tex/latex/pgf/compatibility/pgflibrarysnakes.sty
%{_datadir}/texmf-dist/tex/latex/pgf/compatibility/pgflibrarytikzbackgrounds.sty
%{_datadir}/texmf-dist/tex/latex/pgf/compatibility/pgflibrarytikztrees.sty
%{_datadir}/texmf-dist/tex/latex/pgf/compatibility/pgfnodes.sty
%{_datadir}/texmf-dist/tex/latex/pgf/compatibility/pgfshade.sty
%doc %{_datadir}/texmf-dist/tex/latex/pgf/doc/pgfmanual-en-macros.tex
%doc %{_datadir}/texmf-dist/tex/latex/pgf/doc/pgfmanual.code.tex
%doc %{_datadir}/texmf-dist/tex/latex/pgf/doc/pgfmanual.pdflinks.code.tex
%doc %{_datadir}/texmf-dist/tex/latex/pgf/doc/pgfmanual.prettyprinter.code.tex
%doc %{_datadir}/texmf-dist/tex/latex/pgf/doc/pgfmanual.sty
%{_datadir}/texmf-dist/tex/latex/pgf/frontendlayer/libraries/tikzlibraryexternal.code.tex
%{_datadir}/texmf-dist/tex/latex/pgf/frontendlayer/pgfpict2e.sty
%{_datadir}/texmf-dist/tex/latex/pgf/frontendlayer/tikz.sty
%{_datadir}/texmf-dist/tex/latex/pgf/math/pgfmath.sty
%{_datadir}/texmf-dist/tex/latex/pgf/systemlayer/pgfsys.sty
%{_datadir}/texmf-dist/tex/latex/pgf/utilities/pgfcalendar.sty
%{_datadir}/texmf-dist/tex/latex/pgf/utilities/pgffor.sty
%{_datadir}/texmf-dist/tex/latex/pgf/utilities/pgfkeys.sty
%{_datadir}/texmf-dist/tex/latex/pgf/utilities/pgfpages.sty
%{_datadir}/texmf-dist/tex/latex/pgf/utilities/pgfparser.sty
%{_datadir}/texmf-dist/tex/latex/pgf/utilities/pgfrcs.sty
%{_datadir}/texmf-dist/tex/latex/pgf/utilities/tikzexternal.sty
%{_datadir}/texmf-dist/tex/latex/pgf/utilities/xxcolor.sty
%{_datadir}/texmf-dist/tex/plain/pgf/basiclayer/pgf.tex
%{_datadir}/texmf-dist/tex/plain/pgf/basiclayer/pgfbaseimage.tex
%{_datadir}/texmf-dist/tex/plain/pgf/basiclayer/pgfbaselayers.tex
%{_datadir}/texmf-dist/tex/plain/pgf/basiclayer/pgfbasematrix.tex
%{_datadir}/texmf-dist/tex/plain/pgf/basiclayer/pgfbasepatterns.tex
%{_datadir}/texmf-dist/tex/plain/pgf/basiclayer/pgfbaseplot.tex
%{_datadir}/texmf-dist/tex/plain/pgf/basiclayer/pgfbaseshapes.tex
%{_datadir}/texmf-dist/tex/plain/pgf/basiclayer/pgfbasesnakes.tex
%{_datadir}/texmf-dist/tex/plain/pgf/basiclayer/pgfcore.tex
%{_datadir}/texmf-dist/tex/plain/pgf/frontendlayer/tikz.tex
%{_datadir}/texmf-dist/tex/plain/pgf/math/pgfmath.tex
%{_datadir}/texmf-dist/tex/plain/pgf/systemlayer/pgfsys.tex
%{_datadir}/texmf-dist/tex/plain/pgf/utilities/pgfcalendar.tex
%{_datadir}/texmf-dist/tex/plain/pgf/utilities/pgffor.tex
%{_datadir}/texmf-dist/tex/plain/pgf/utilities/pgfkeys.tex
%{_datadir}/texmf-dist/tex/plain/pgf/utilities/pgfrcs.tex

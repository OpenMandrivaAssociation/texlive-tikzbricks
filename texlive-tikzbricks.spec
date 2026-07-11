%global tl_name tikzbricks
%global tl_revision 73140

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.6
Release:	%{tl_revision}.1
Summary:	Drawing bricks with TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/tikzbricks
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzbricks.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzbricks.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(epstopdf-pkg)
Requires:	texlive(iftex)
Requires:	texlive(pgf)
Requires:	texlive(tikz-3dplot)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A small LaTeX package to draw bricks with TikZ. The user can modify
color, shape, and viewpoint.


%global tl_name librebaskerville
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	The Libre Baskerville family of fonts with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/librebaskerville
License:	ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/librebaskerville.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/librebaskerville.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides the Libre Baskerville family of fonts, designed by
Pablo Impallari, for use with LaTeX, pdfLaTeX, XeLaTeX or LuaLaTeX. It
is primarily intended to be a web font but is also attractive as a text
font. A BoldItalic variant has been artificially generated.


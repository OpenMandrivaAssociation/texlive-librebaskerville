Name:		texlive-librebaskerville
Version:	64421
Release:	2
Summary:	LaTeX support for the Libre Baskerville family of fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/librebaskerville
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/librebaskerville.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/librebaskerville.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Libre Baskerville is designed by Pablo Impallari. It is
primarily intended to be a web font but is also attractive as a
TeX font. As there is currently no bold italic variant, an
artificially slanted version of the bold variant has been
generated.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/librebaskerville
%{_texmfdistdir}/fonts/map/dvips/librebaskerville
%{_texmfdistdir}/fonts/truetype/impallari/librebaskerville
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville
%{_texmfdistdir}/fonts/type1/impallari/librebaskerville
%{_texmfdistdir}/fonts/vf/impallari/librebaskerville
%{_texmfdistdir}/tex/latex/librebaskerville
%doc %{_texmfdistdir}/doc/fonts/librebaskerville

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}

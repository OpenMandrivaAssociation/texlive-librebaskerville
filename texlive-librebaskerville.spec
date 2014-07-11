# revision 31741
# category Package
# catalog-ctan /fonts/librebaskerville
# catalog-date 2013-09-23 21:56:36 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-librebaskerville
Version:	20130923
Release:	8
Summary:	LaTeX support for the Libre Baskerville family of fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/librebaskerville
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/librebaskerville.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/librebaskerville.doc.tar.xz
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
%{_texmfdistdir}/fonts/enc/dvips/librebaskerville/lbsk_5rmxhc.enc
%{_texmfdistdir}/fonts/enc/dvips/librebaskerville/lbsk_7c5ufm.enc
%{_texmfdistdir}/fonts/enc/dvips/librebaskerville/lbsk_aprite.enc
%{_texmfdistdir}/fonts/enc/dvips/librebaskerville/lbsk_hguso3.enc
%{_texmfdistdir}/fonts/enc/dvips/librebaskerville/lbsk_ktbdpq.enc
%{_texmfdistdir}/fonts/enc/dvips/librebaskerville/lbsk_lbmt7s.enc
%{_texmfdistdir}/fonts/enc/dvips/librebaskerville/lbsk_mr5ybw.enc
%{_texmfdistdir}/fonts/enc/dvips/librebaskerville/lbsk_rpuqof.enc
%{_texmfdistdir}/fonts/enc/dvips/librebaskerville/lbsk_yeotsr.enc
%{_texmfdistdir}/fonts/map/dvips/librebaskerville/LibreBaskerville.map
%{_texmfdistdir}/fonts/opentype/impallari/librebaskerville/LibreBaskerville-Bold.otf
%{_texmfdistdir}/fonts/opentype/impallari/librebaskerville/LibreBaskerville-BoldItalic.otf
%{_texmfdistdir}/fonts/opentype/impallari/librebaskerville/LibreBaskerville-Italic.otf
%{_texmfdistdir}/fonts/opentype/impallari/librebaskerville/LibreBaskerville-Regular.otf
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-Bold-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-Bold-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-Bold-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-Bold-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-Bold-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-Bold-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-Bold-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-Bold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-BoldItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-BoldItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-BoldItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-BoldItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-BoldItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-BoldItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-BoldItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-BoldItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-BoldItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-BoldItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-BoldItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-BoldItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-Italic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-Italic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-Italic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-Italic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-Italic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-Italic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-Italic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-Italic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-Italic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-Italic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-Italic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-Italic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-Regular-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-Regular-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-Regular-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-Regular-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-Regular-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-Regular-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-Regular-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-Regular-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-Regular-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-Regular-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-Regular-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librebaskerville/LibreBaskerville-Regular-tlf-ts1.tfm
%{_texmfdistdir}/fonts/type1/impallari/librebaskerville/LibreBaskerville-Bold.pfb
%{_texmfdistdir}/fonts/type1/impallari/librebaskerville/LibreBaskerville-BoldItalic.pfb
%{_texmfdistdir}/fonts/type1/impallari/librebaskerville/LibreBaskerville-Italic.pfb
%{_texmfdistdir}/fonts/type1/impallari/librebaskerville/LibreBaskerville-Regular.pfb
%{_texmfdistdir}/fonts/vf/impallari/librebaskerville/LibreBaskerville-Bold-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/librebaskerville/LibreBaskerville-Bold-sup-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/librebaskerville/LibreBaskerville-Bold-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/librebaskerville/LibreBaskerville-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/librebaskerville/LibreBaskerville-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/librebaskerville/LibreBaskerville-BoldItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/librebaskerville/LibreBaskerville-BoldItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/librebaskerville/LibreBaskerville-BoldItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/librebaskerville/LibreBaskerville-BoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/librebaskerville/LibreBaskerville-BoldItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/librebaskerville/LibreBaskerville-Italic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/librebaskerville/LibreBaskerville-Italic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/librebaskerville/LibreBaskerville-Italic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/librebaskerville/LibreBaskerville-Italic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/librebaskerville/LibreBaskerville-Italic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/librebaskerville/LibreBaskerville-Regular-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/librebaskerville/LibreBaskerville-Regular-sup-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/librebaskerville/LibreBaskerville-Regular-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/librebaskerville/LibreBaskerville-Regular-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/librebaskerville/LibreBaskerville-Regular-tlf-ts1.vf
%{_texmfdistdir}/tex/latex/librebaskerville/LY1LibreBaskerville-Sup.fd
%{_texmfdistdir}/tex/latex/librebaskerville/LY1LibreBaskerville-TLF.fd
%{_texmfdistdir}/tex/latex/librebaskerville/OT1LibreBaskerville-Sup.fd
%{_texmfdistdir}/tex/latex/librebaskerville/OT1LibreBaskerville-TLF.fd
%{_texmfdistdir}/tex/latex/librebaskerville/T1LibreBaskerville-Sup.fd
%{_texmfdistdir}/tex/latex/librebaskerville/T1LibreBaskerville-TLF.fd
%{_texmfdistdir}/tex/latex/librebaskerville/TS1LibreBaskerville-TLF.fd
%{_texmfdistdir}/tex/latex/librebaskerville/librebaskerville.sty
%doc %{_texmfdistdir}/doc/fonts/librebaskerville/FONTLOG.txt
%doc %{_texmfdistdir}/doc/fonts/librebaskerville/OFL.txt
%doc %{_texmfdistdir}/doc/fonts/librebaskerville/README
%doc %{_texmfdistdir}/doc/fonts/librebaskerville/librebaskerville-samples.pdf
%doc %{_texmfdistdir}/doc/fonts/librebaskerville/librebaskerville-samples.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}

# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/polynomial
# catalog-date 2008-08-23 00:06:02 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-polynomial
Version:	1.0
Release:	11
Summary:	Typeset (univariate) polynomials
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/polynomial
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/polynomial.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/polynomial.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/polynomial.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package offers an easy way to write (univariate)
polynomials and rational functions. It defines two commands,
one for polynomials \polynomial{coeffs} and one for rational
functions \polynomialfrac{Numerator}{Denominator}. Both
commands take lists of coefficients as arguments, and offer
limited optional behaviour.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/polynomial/polynomial.sty
%doc %{_texmfdistdir}/doc/latex/polynomial/README
%doc %{_texmfdistdir}/doc/latex/polynomial/polynomial.pdf
#- source
%doc %{_texmfdistdir}/source/latex/polynomial/polynomial.dtx
%doc %{_texmfdistdir}/source/latex/polynomial/polynomial.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 755021
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 719286
- texlive-polynomial
- texlive-polynomial
- texlive-polynomial
- texlive-polynomial


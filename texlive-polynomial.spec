Name:		texlive-polynomial
Version:	15878
Release:	2
Summary:	Typeset (univariate) polynomials
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/polynomial
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/polynomial.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/polynomial.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/polynomial.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

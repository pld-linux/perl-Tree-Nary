%include	/usr/lib/rpm/macros.perl
%define	pdir	Tree
%define	pnam	Nary
Summary:	Tree::Nary - Perl implementation of N-ary search trees
Summary(pl):	Tree::Nary - perlowa implementacja N-arnych drzew wyszukiwañ
Name:		perl-%{pdir}-%{pnam}
Version:	1.21
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Tree::Nary class implements N-ary trees (trees of data with any
number of branches), providing the organizational structure for a tree
(collection) of any number of nodes, but knowing nothing about the
specific type of node used.  It can be used to display hierarchical
database entries in an internal application (the NIS netgroup file is an
example of such a database). It offers the capability to select nodes on
the tree, and attachment points for nodes on the tree. Each attachment
point can support multiple child nodes.

%description -l pl
Klasa Tree::Nary jest implementacj± drzew N-arnych (drzew danych z
dowoln± liczb± odga³êzieñ), udostêpniaj±c± strukturê organizacyjn± dla
drzewa (zestawu) o dowolnej liczbie wêz³ów, bez wiedzy o konkretnym
typie wêz³ów. Klasa ta mo¿e byæ u¿ywana do wy¶wietlania rekordów
hierarchicznej bazy danych w wewnêtrznej aplikacji (plik grup
sieciowych NIS jest przyk³adem takiej bazy danych). Oferuje tak¿e
mo¿liwo¶æ wyboru wêz³ów w drzewie i punktów do³±czania dla wêz³ów.
Ka¿dy punkt do³±czania mo¿e s³u¿yæ wielu wêz³om potomnym.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*

#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Tree
%define		pnam	Nary
Summary:	Tree::Nary - Perl implementation of N-ary search trees
Summary(pl.UTF-8):	Tree::Nary - implementacja perlowa N-arnych drzew wyszukiwań
Name:		perl-Tree-Nary
Version:	1.3
Release:	2
Epoch:		1
# same as perl (README says Public Domain)
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c9eeebc69869554579b297aa61b0e779
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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

%description -l pl.UTF-8
Klasa Tree::Nary jest implementacją drzew N-arnych (drzew danych z
dowolną liczbą odgałęzień), udostępniającą strukturę organizacyjną dla
drzewa (zestawu) o dowolnej liczbie węzłów, bez wiedzy o konkretnym
typie węzłów. Klasa ta może być używana do wyświetlania rekordów
hierarchicznej bazy danych w wewnętrznej aplikacji (plik grup
sieciowych NIS jest przykładem takiej bazy danych). Oferuje także
możliwość wyboru węzłów w drzewie i punktów dołączania dla węzłów.
Każdy punkt dołączania może służyć wielu węzłom potomnym.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*

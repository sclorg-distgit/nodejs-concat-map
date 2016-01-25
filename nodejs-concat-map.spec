%{?scl:%scl_package nodejs-concat-map}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-concat-map

%global npm_name concat-map
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-concat-map
Version:	0.0.1
Release:	1%{?dist}
Summary:	concatenative mapdashery
Url:		https://github.com/substack/node-concat-map
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	MIT

BuildArch:	noarch

%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  %{?scl_prefix}nodejs-devel
BuildRequires:  nodejs010-runtime

%if 0%{?enable_tests}
BuildRequires:	%{?scl_prefix}npm(tape)
%endif

%description
concatenative mapdashery

%prep
%setup -q -n package

rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json *.js \
%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}

%check
%{nodejs_symlink_deps} --check

%endif

%files
%{nodejs_sitelib}/concat-map

%doc README.markdown LICENSE

%changelog
* Tue Dec 01 2015 Tomas Hrcka <thrcka@redhat.com> - 0.0.1-1
- Initial build

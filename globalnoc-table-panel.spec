Summary: GlobalNOC Table
Name:    globalnoc-table-panel
Version: 0.0.1
Release: %{_buildno}%{?dist}
License: Apache
Group:   GRNOC
URL:     https://globalnoc.iu.edu/
Source:  https://github.com/GlobalNOC/globalnoc-table-panel/

BuildArch: noarch
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)


%description
A grafana table with custom additions by GlobalNOC.

%prep
rm -rf %{_builddir}

mkdir -p %{_builddir}
cp -pr %{_sourcedir}/*  %{_builddir}

%build
npm install yarn
yarn install
grunt

%install
rm -rf $RPM_BUILDR_ROOT

%{__install} -d -p %{buildroot}%{_sharedstatedir}/grafana/plugins/globalnoc-table-panel/dist
cp -ar %{_builddir}/dist/* %{buildroot}%{_sharedstatedir}/grafana/plugins/globalnoc-table-panel/dist

%files
%{_sharedstatedir}/grafana/plugins/globalnoc-table-panel/dist

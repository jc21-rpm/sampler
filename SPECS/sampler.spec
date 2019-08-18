%define debug_package %{nil}

%global gh_user sqshq
%global gh_name sampler

Name:           sampler
Version:        1.0.3
Release:        1%{?dist}
Summary:        A tool for shell commands execution, visualization and alerting
Group:          Applications/System
License:        GNU
URL:            https://sampler.dev
BuildRequires:  golang alsa-lib-devel
Requires:       alsa-lib

%description
Sampler is a tool for shell commands execution, visualization and alerting.
Configured with a simple YAML file.

%prep
wget https://github.com/%{gh_user}/%{gh_name}/archive/v%{version}.tar.gz
tar xzf v%{version}.tar.gz
mkdir -p %{_builddir}/src/github.com/%{gh_user}/
cd %{_builddir}/src/github.com/%{gh_user}/
mv %{_builddir}/%{gh_name}-%{version} %{gh_name}
mkdir -p %{_builddir}/%{gh_name}-%{version}
cd %{gh_name}

%build
export GOPATH="%{_builddir}"
export PATH=$PATH:"%{_builddir}"/bin
cd %{_builddir}/src/github.com/%{gh_user}/%{gh_name}
GO111MODULE=on go build -o bin/%{name}

%install
install -Dm0755 %{_builddir}/src/github.com/%{gh_user}/%{gh_name}/bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Mon Aug 19 2019 Jamie Curnow <jc@jc21.com> 1.0.3-1
- v1.0.3

* Thu Aug 15 2019 Jamie Curnow <jc@jc21.com> 1.0.2-1
- v1.0.2

* Wed Aug 7 2019 Jamie Curnow <jc@jc21.com> 1.0.1-1
- Initial spec

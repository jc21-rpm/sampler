%define debug_package %{nil}

%global gh_user sqshq

Name:           sampler
Version:        1.1.0
Release:        1%{?dist}
Summary:        A tool for shell commands execution, visualization and alerting
Group:          Applications/System
License:        GNU
URL:            https://sampler.dev
Source:         https://github.com/%{gh_user}/%{name}/archive/v%{version}.tar.gz
BuildRequires:  golang alsa-lib-devel
Requires:       alsa-lib

%description
Sampler is a tool for shell commands execution, visualization and alerting.
Configured with a simple YAML file.

%prep
%setup -q -n %{name}-%{version}

%build
go build -o bin/%{name}

%install
install -Dm0755 bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Thu Dec 26 2019 Jamie Curnow <jc@jc21.com> 1.1.0-1
- v1.1.0

* Mon Aug 19 2019 Jamie Curnow <jc@jc21.com> 1.0.3-1
- v1.0.3

* Thu Aug 15 2019 Jamie Curnow <jc@jc21.com> 1.0.2-1
- v1.0.2

* Wed Aug 7 2019 Jamie Curnow <jc@jc21.com> 1.0.1-1
- Initial spec

%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%global release_name liberty

Name:           python-muranoclient
Version:        XXX
Release:        XXX
Summary:        python-muranoclient
Group:          Development/Libraries
License:        Apache License, Version 2.0
URL:            https://launchpad.net/murano
Source0:        https://launchpad.net/%{name}/%{release_name}/%{version}/+download/%{name}-%{version}.tar.gz
BuildRequires:  python-devel, python-setuptools, libyaml-devel, python-pbr, python-d2to1
BuildArch:      noarch
Requires:       python-pbr >= 1.6
Requires:       python-argparse
Requires:       python-prettytable >= 0.7
Requires:       python-keystoneclient >= 1:1.6.0
Requires:       python-glanceclient >= 1:0.18.0
Requires:       python-httplib2 >= 0.7.5
Requires:       python-iso8601 >= 0.1.9
Requires:       python-six >= 1.9.0
Requires:       python-babel >= 1.3
Requires:       pyOpenSSL >= 0.14
Requires:       PyYAML >= 3.1.0
Requires:       python-requests >= 2.5.2
Requires:       python-yaql >= 1.0.0
Requires:       python-oslo-serialization >= 1.4.0
Requires:       python-oslo-utils >= 2.0.0
Requires:       python-oslo-log >= 1.8.0

%description
Sytem package - python-muranoclient
Python package - python-muranoclient

%prep
%setup -q -n python-muranoclient-%{upstream_version}

%build
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{python_sitelib}/


%changelog

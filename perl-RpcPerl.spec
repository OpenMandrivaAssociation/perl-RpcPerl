%define module   RpcPerl
%define version  0.1
%define release  %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    LGPL or EPL
Group:      Development/Perl
Summary:    RPC with a Perl server
Url:        http://qooxdoo.org/documentation/0.8/rpc_perl
Source:     https://sourceforge.net/projects/qooxdoo-contrib/files/RpcPerl/%{module}-%{version}.zip
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
As described in the RPC overview, qooxdoo RPC is based on JSON-RPC as the
serialization and method call protocol. This page describes how to set up and
implement a Perl-based server.

%prep
%setup -q -n %{module}/%{version}

%build

%install
rm -rf %{buildroot}
install -d -m 755  %{buildroot}%{perl_vendorlib}
cp -pr Qooxdoo %{buildroot}%{perl_vendorlib}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README.CONFIGURE README.txt SERVER_WRITER_GUIDE jsonrpc.pl
%{perl_vendorlib}/Qooxdoo


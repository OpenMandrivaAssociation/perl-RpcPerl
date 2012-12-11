%define module   RpcPerl

Name:		perl-%{module}
Version:	0.1
Release:	2
License:	LGPL or EPL
Group:		Development/Perl
Summary:	RPC with a Perl server
Url:		http://qooxdoo.org/documentation/0.8/rpc_perl
Source:		https://sourceforge.net/projects/qooxdoo-contrib/files/RpcPerl/%{module}-%{version}.zip
BuildArch:	noarch

%description
As described in the RPC overview, qooxdoo RPC is based on JSON-RPC as the
serialization and method call protocol. This page describes how to set up and
implement a Perl-based server.

%prep
%setup -q -n %{module}/%{version}

%build

%install
install -d -m 755  %{buildroot}%{perl_vendorlib}
cp -pr Qooxdoo %{buildroot}%{perl_vendorlib}

%files
%doc README.CONFIGURE README.txt SERVER_WRITER_GUIDE jsonrpc.pl
%{perl_vendorlib}/Qooxdoo

%changelog
* Wed Jul 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.1-1mdv2010.0
+ Revision: 396455
- import perl-RpcPerl


* Wed Jul 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.1-1mdv2010.0
- first mdv release 

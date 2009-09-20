%define rel 7

Name:           svnmailer
Version:        1.0.8
Release:        %mkrel %rel
Summary:        Tool to send subversion commit notifications 
Group:          Development/Other
License:        Apache License 2.0
URL:            http://opensource.perlig.de/svnmailer/
Source0:        http://storage.perlig.de/svnmailer/%{name}-%{version}.tar.bz2
Patch:          svnmailer-1.0.8-python2.5.diff
BuildRequires:  python-devel
Requires:       python-svn  
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
The svnmailer is a tool that is usually called by a subversion hook to submit 
commit notifications in various ways (at the moment: mail via SMTP or a pipe 
to a sendmail like program, news via NNTP, or CIA live tracker notification 
via XML-RPC). It is derived from the original mailer.py distributed with 
subversion, but should be much more consistent, more extensible, and have 
many more features.

%prep
%setup -q
%patch -p0

%install
rm -rf %{buildroot}
python setup.py install --prefix=%{buildroot}/%_prefix

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES CREDITS docs LICENSE README
%_bindir/svn-mailer
%py_puresitedir/%name/
%py_puresitedir/*egg-info



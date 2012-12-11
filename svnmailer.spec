%define rel 8

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




%changelog
* Tue Nov 02 2010 Michael Scherer <misc@mandriva.org> 1.0.8-8mdv2011.0
+ Revision: 592174
- rebuild for python 2.7

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 1.0.8-7mdv2010.0
+ Revision: 445280
- rebuild

* Fri Jan 02 2009 Funda Wang <fwang@mandriva.org> 1.0.8-6mdv2009.1
+ Revision: 323369
- rebuild

* Thu Mar 13 2008 Andreas Hasenack <andreas@mandriva.com> 1.0.8-5mdv2008.1
+ Revision: 187646
- rebuild for 2008.1

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 01 2007 Michael Scherer <misc@mandriva.org> 1.0.8-4mdv2008.0
+ Revision: 19769
- patch to fix #30472


* Wed Dec 06 2006 Michael Scherer <misc@mandriva.org> 1.0.8-3mdv2007.0
+ Revision: 91850
- rebuild for new python
- Import svnmailer


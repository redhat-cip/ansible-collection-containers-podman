Name:           ansible-collection-containers-podman
Version:        1.8.1
Release:        1.VERS%{?dist}
Summary:        Podman container Ansible modules
License:        GPL-3.0-or-later
URL:            https://github.com/containers/ansible-podman-collections
Source0:        https://galaxy.ansible.com/download/ansible-collection-containers-podman-%{version}.tar.gz
BuildArch:      noarch

Requires:       ansible


%description
Podman container Ansible modules

%prep
%autosetup -c ansible-collection-containers-podman-%{version}-%{release}

%build


%install
install -d -m 0755 %{buildroot}/%{_datadir}/ansible/collections/ansible_collections/containers/podman/
cp -rp * %{buildroot}/%{_datadir}/ansible/collections/ansible_collections/containers/podman/

%files
%doc README.md
%{_datadir}/ansible/collections/ansible_collections/containers/podman/


%changelog

* Fri Oct 29 2021 Bill Peck <bpeck@redhat.com> - 1.8.1-1
- Initial package

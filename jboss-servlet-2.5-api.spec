%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-servlet-2.5-api
Version:          1.0.1
Release:          4%{dist}
Summary:          Java Servlet 2.5 API
Group:            Development/Libraries
License:          ASL 2.0 and W3C
Url:              http://www.jboss.org

# git clone git://github.com/jboss/jboss-servlet-api_spec.git
# cd jboss-servlet-api_spec/ && git archive --format=tar --prefix=jboss-servlet-2.5-api/ jboss-servlet-api_2.5_spec-1.0.1.Final | xz > jboss-servlet-2.5-api-1.0.1.Final.tar.xz
Source0:          jboss-servlet-2.5-api-%{namedversion}.tar.xz

BuildRequires:    java-devel
BuildRequires:    jboss-specs-parent
BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-source-plugin

Requires:         jpackage-utils
Requires:         java
BuildArch:        noarch

%description
The Java Servlet 2.5 API classes.

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Libraries
Requires:         jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-servlet-2.5-api

%build
mvn-rpmbuild install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 target/jboss-servlet-api_2.5_spec-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%doc LICENSE NOTICE

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE NOTICE

%changelog
* Thu Jul 11 2013 Ade Lee <alee@redhat.com> 1.0.1-4
- Removed unneeded build dependencies

* Thu Apr 4 2013 Ade Lee <alee@redhat.com> 1.0.1-3
- Removed javax.servlet mapping

* Wed Apr 3 2013 Ade Lee <alee@redhat.com> 1.0.1-2
- Corrected license

* Tue Apr 2 2013 Ade Lee <alee@redhat.com> 1.0.1-1
- Initial packaging

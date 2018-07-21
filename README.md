Ansible Role Spring boot App
=========

[![Build Status](https://travis-ci.org/orachide/ansible-role-springboot.svg?branch=master)](https://travis-ci.org/orachide/ansible-role-springboot)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-orachide-660198.svg)](https://galaxy.ansible.com/orachide)

Ansible role that install Spring boot application as a service.

This role will copy the application artifact on the server and start it. By default the role will also create a service (SystemV - init.d, Systemd) to manage application

Requirements
------------

Your spring boot application should be previously packaged as a fully executable jar as explained here :

https://docs.spring.io/spring-boot/docs/current/reference/html/deployment-install.html#deployment-install


```xml
<plugin>
	<groupId>org.springframework.boot</groupId>
	<artifactId>spring-boot-maven-plugin</artifactId>
	<configuration>
		<executable>true</executable>
	</configuration>
</plugin>
```


Role Variables
--------------

| Variables | Required | Default value | Description |
|-----------|----------|---------------|-------------|
| sb_app_name  | true     | *None*          | the application name |
| sb_app_group_id  | true     | *None*          | the maven artifact group id |
| sb_app_artifact_id  | true     | *None*          | the maven artifact id |
| sb_app_version  | true     | *None*          | the maven artifact version |
| sb_app_user  | true     | *None*          | the owner of application files on server|
| sb_app_user_group  | true     | *None*          | the group owninng application files |
| sb_app_extension  | true     | *jar*          | the artifact file extension. (jar,war,ear) |
| sb_app_state  | false     | *present*          | Can be *present* or *absent* depending on install or uninstall|
| sb_app_classifier  | false     | *None*          | the artifact file classifier (SOURCES,DOCS...) |
| sb_maven_repository_url  | false     | *[Maven official repo](http://repo1.maven.org/maven2)*          | the url to the maven repository |
| sb_app_repository_username  | false     | *None*          | username used for mave repo authentication |
| sb_app_repository_password  | false     | *None*          | password used for mave repo authentication |
| sb_app_artifact_file  | false     | *None*          | the local path to the artifact to deploy. If defined the role won't download artifact from *sb_maven_repository_url* but will use local artifact file. |
| sb_local_maven_artifact_dowload | false | false | Artifact should be download locally first and then copy to remote host? |
| sb_applications_root_folder  | false     | */opt/applis*         | the root folder where application files will be copy|
| sb_app_java_opts_xms  | false     | *256M*          | JAVA XMS value |
| sb_app_java_opts_xmx  | false     | *1024M*          | JAVA XMX value |
| sb_app_java_opts_others  | false     | *None*          | Custom JAVA_OPTS options |
| sb_app_config_file_template_path  | false     | *None*          | Spring application.yml file template path. This file will be copy near to the artifact  |
| sb_app_config_file_final_name  | false     | **application.yml**          | Configuration file final name, could be *.yml or *.properties  |
| sb_app_logback_file_template_path  | false     | *None*          | Logback file template path. This file will be loaded by setting `logging.config` system property  |
| sb_app_healthcheck_urls  | false     | *None*          | Http urls to check if the service is healthy (should be an array)|
| sb_app_healthcheck_ports  | false     | *None*          | TCP Ports to check if the service is healthy (should be an array)|
| sb_app_service_java_home  | false     | *None*          | Set the __JAVA_HOME__ to use |
| sb_app_stop_wait_time  | false     | 60 secs         | The time in seconds to wait when stopping the application before forcing a shutdown  |




Dependencies
------------

This role can install JAVA using [geerlingguy.java](https://github.com/geerlingguy/ansible-role-java)

Example Playbook
----------------

### Using local maven artifact


    - name: Converge
      hosts: all
      roles:
        - role: ansible-role-springboot
          sb_app_name: dummy-boot-app
          sb_app_group_id: fr.chidix
          sb_app_artifact_id: dummy-boot-app
          sb_app_version: 0.0.1-SNAPSHOT
          sb_app_extension: jar
          sb_app_user: sbuser
          sb_app_user_group: sbgroup
          sb_local_maven_artifact_dowload: false
          sb_app_artifact_file: "{{ playbook_dir}}/artifacts/dummy-boot-app-0.0.1-SNAPSHOT.jar"
          sb_app_config_file_template_path: "{{ playbook_dir }}/templates/dummy-boot-app-configuration.yml.j2"
          sb_app_java_opts_others: "-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=6006"
          sb_app_healthcheck_urls:
            - "http://localhost:8082/actuator/health"
          sb_app_healthcheck_ports:
            - 8082

### Using maven artifact from maven repository


    - name: Converge
      hosts: all
      roles:
        - role: ansible-role-springboot
          sb_app_as_a_service: true
          sb_app_name: dummy-boot-app
          sb_app_group_id: fr.chidix
          sb_app_artifact_id: dummy-boot-app
          sb_app_version: 0.0.1-SNAPSHOT
          sb_app_extension: jar
          sb_app_user: sbuser
          sb_app_user_group: sbgroup
          sb_maven_repository_url: https://my-private-maven-repository/repository/maven-snapshots/
          sb_app_repository_username: my-user
          sb_app_repository_password: my-very-secure-password
          sb_local_maven_artifact_dowload: false
          sb_app_config_file_template_path: "{{ playbook_dir }}/templates/dummy-boot-app-configuration.yml.j2"
          sb_app_healthcheck_urls:
            - "http://localhost:8082/actuator/health"
          sb_app_healthcheck_ports:
            - 8082

License
-------

BSD

Author Information
------------------

This role was created in 2018 by [Rachide Ouattara](https://orachide.chidix.fr/).

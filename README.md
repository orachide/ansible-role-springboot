Ansible Role Spring boot App
=========

[![Build Status](https://travis-ci.org/orachide/ansible-role-springboot.svg?branch=master)](https://travis-ci.org/orachide/ansible-role-springboot)

Ansible role that install Spring boot application on server.

This role will copy the application artifact on the server and start it. By default the role will also create a service (SystemV - init.d, Systemd) to manage application

Requirements
------------

Your spring boot application should be previously packaged as a fully executable jar as explained here :

https://docs.spring.io/spring-boot/docs/current/reference/html/deployment-install.html#deployment-script-customization-conf-file

Role Variables
--------------

| Variables | Required | Default value | Description |
|-----------|----------|---------------|-------------|
| sb_app_name  | true     | *None*          | the application name |
| sb_app_group_id  | true     | *None*          | the maven group id |
| sb_app_artifact_id  | true     | *None*          | the maven artifact id |
| sb_app_version  | true     | *None*          | the maven artifact version |
| sb_app_user  | true     | *None*          | the owner of application files on server|
| sb_app_user_group  | true     | *None*          | the group owninng application files |
| sb_app_classifier  | false     | *None*          | the artifact file classifier (SOURCES,DOCS...) |
| sb_app_extension  | true     | *jar*          | the artifact file extension. (jar,war,ear) |
| sb_maven_repository_url  | false     | *Maven official repo*          | the url to the maven repository |
| sb_app_artifact_file  | false     | *None*          | the local path to the artifact to deploy |
| sb_local_maven_artifact_dowload | false | false | Artifact should be download locally first and then copy to remote host? |
| sb_app_java_opts_xms  | false     | *256M*          | JAVA XMS value |
| sb_app_java_opts_xmx  | false     | *1024M*          | JAVA XMX value |
| sb_app_java_opts_others  | false     | *None*          | Custom JAVA_OPTS options |



Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: all
      vars:
        sb_app_name: my-app
        sb_app_group_id: my-groupid
        sb_app_artifact_id: my-artifactid
        sb_app_version: 0.0.1
        sb_app_user: john
        sb_app_user_group: user_group
        sb_app_artifact_file: /path/file.jar
        sb_app_extension: jar
      roles:
        - role: ansible-role-springboot

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).

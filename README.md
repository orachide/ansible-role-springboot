Ansible Role Spring boot App
=========

[![Build Status](https://travis-ci.org/orachide/ansible-role-springboot.svg?branch=master)](https://travis-ci.org/orachide/ansible-role-springboot)

A brief description of the role goes here.

Requirements
------------

Your spring boot application should be previously packaged as a fully executable jar as explained here :

https://docs.spring.io/spring-boot/docs/current/reference/html/deployment-install.html#deployment-script-customization-conf-file

Role Variables
--------------

| Variables | Required | Default value | Description |
|-----------|----------|---------------|-------------|
| app_name  | true     | *None*          | the application name |
| app_group_id  | true     | *None*          | the application name |
| app_artifact_id  | true     | *None*          | the application name |
| app_version  | true     | *None*          | the application name |
| app_user  | true     | *None*          | the application name |
| app_user_group  | true     | *None*          | the application name |
| app_extension  | true     | *None*          | the application name |
| app_repository_url  | false     | *Maven official repo*          | the url to the maven repository |
| app_artifact_file  | false     | *None*          | the local path to the artifact to deploy |
| local_maven_artifact_dowload | false | false | Artifact should be download locally first and then copy to remote host? |
| app_artifact_file  | false     | *None*          | the local path to the artifact to deploy |
| app_java_opts_xms  | false     | *256M*          | JAVA XMS value |
| app_java_opts_xmx  | false     | *1024M*          | JAVA XMX value |
| app_java_opts_others  | false     | *None*          | Custom JAVA_OPTS options |



Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: all
      vars:
        app_name: my-app
        app_group_id: my-groupid
        app_artifact_id: my-artifactid
        app_version: 0.0.1
        app_user: john
        app_user_group: ro
        app_artifact_file: /path/file.jar
        app_extension: jar
      roles:
        - role: ansible-role-springboot

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).

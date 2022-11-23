### In this playbook we sepregate the nodes####
---
#here,this is target section
- host: web
  become: true
# we mantion here varaiables##
  var:
     pkgname:httpd  tasks:   name: install apache
    action:  yum name='{{pkgname}}' state=install
    notify:  restart '{{pkgname}}
#here,we use handlers
#"handlers are just like regular task in an ansible playbook,but are only run ifthe task contain
# notify directive and also indicates that it changed somethin
   handlers:
   - name: restart '{{pkgname}}
      action: service name= '{{pkgname}}  state= restarted

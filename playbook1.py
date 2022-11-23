### In this playbook we sepregate the nodes####
---
#here,this is target section
- host: web   #IN WEB NODES,we have almost 50 machine with diffenet OS
  become: true
  Connection: ssh
# we mantion here varaiables##
  var:
     pkgname:httpd
     pkgName:python == yum install -y python3
  tasks:
    - name: install apache
      action:  yum name='{{pkgname}}' state=install
      when: ansible_os_family == "RedHat"
      notify:  install '{{pkgName}}
#here,we use handlers
#"handlers are just like regular task in an ansible playbook,but are only run ifthe task contain
# notify directive and also indicates that it changed somethin
   handlers:
   - name: install '{{pkgName}}
      action: name= '{{pkgName}}  state= install
    #yum install -y python3

#If we want to want to secure our sensitive data, ansible allow us
#to use vault modeuale(encrypted file)
#ansible -vault create vault.yml
#ansible-vault edit vault.yml
# ansible-vault rekey vault.yml
#ansible-vault encrypt (filename).yml
#nsible-vault decrypt (filename).yml



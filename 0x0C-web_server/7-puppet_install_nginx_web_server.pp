# installing and configure an Nginx server using Puppet instead of Bash

# Updating packages using apt
exec { 'apt-update':
  command => 'apt-get -y update',
  path    => ['/usr/bin', '/bin'],
}

# Installing Nginx
package { 'nginx':
  ensure  => 'installed',
  require => Exec['apt-update'],
}

# Nginx HTTP traffic(Port 80)
exec { 'allow-nginx-http':
  command => 'ufw allow "Nginx HTTP"',
  path    => ['/usr/sbin', '/usr/bin', '/sbin', '/bin'],
  unless  => 'ufw status | grep "Nginx HTTP"',
  require => Package['nginx'],
}

# Creating index file with "Hello World"
file { '/var/www/html/index.nginx-debian.html':
  ensure  => 'file',
  content => 'Hello World',
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  require => Package['nginx'],
}

# Nginx rewrite rule
exec { 'nginx-rewrite-rule':
  command => 'sed -i "/server_name _;/a rewrite ^/redirect_me/ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
  path    => ['/usr/bin', '/bin'],
  require => Package['nginx'],
}

# Restarting Nginx service
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => [Exec['add-nginx-rewrite-rule'], Package['nginx']],
}


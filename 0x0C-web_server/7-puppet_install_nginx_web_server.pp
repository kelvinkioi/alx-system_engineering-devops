# installing and configure an Nginx server using Puppet instead of Bash

exec { 'system update using apt':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['update system']
}

file {'/var/www/html/index.html':
  content => 'Hello World!',
}

exec {'redirect_me':
  command  => sudo sed -i '/server_name _;/a rewrite ^/redirect_me/ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;' /etc/nginx/sites-available/default
  provider => 'shell',
}

service {'nginx':
  ensure  => running,
  require => Package['nginx']
}

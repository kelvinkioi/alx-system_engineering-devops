#we are testing how well our web server setup featuring Nginx is doing under pressure
# Increase limit
exec { 'fixing nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}


-> exec { 'restarting nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}

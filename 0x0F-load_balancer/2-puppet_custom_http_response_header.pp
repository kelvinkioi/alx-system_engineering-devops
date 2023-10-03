# automate the task of creating a custom HTTP header response, but with Puppet
package {'nginx':
  ensure => 'present',
}

exec { 'update and install':
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx',
  provider => shell,
}

exec { 'sudo sed -i "/listen 80 default_server/a add_header X-Served-By $hostname;" /etc/nginx/sites-available/default':
  provider => shell,
}

exec { 'sudo service nginx restart':
  provider => shell,
}

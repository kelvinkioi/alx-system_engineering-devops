# installing and configure an Nginx server using Puppet instead of Bash
package {'nginx':
  ensure => 'present',
}

exec { 'update and install':
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx',
  provider => shell,

}

exec { 'Hello World':
  command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
  provider => shell,
}

exec { 'sudo sed -i "/server_name _;/a rewrite ^/redirect_me/ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default':
  provider => shell,
}

exec { 'sudo service nginx restart':
  provider => shell,
}

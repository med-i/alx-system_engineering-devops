# install Nginx web server using Puppet

package { 'nginx':
  ensure => installed,
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Package['nginx'],
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => '
server {
  add_header X-Served-By $hostname;
  listen 80 default_server;
  listen [::]:80 default_server;

  root /var/www/html;

  server_name _;
  error_page 404 /404.html;
  location = /404.html {
    root /var/www/html; internal;
  }
  location /redirect_me {
    return 301 https://github.com/med-i;
  }
  location / {
    try_files $uri $uri/ =404;
  }
}',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/sites-available/default'],
}

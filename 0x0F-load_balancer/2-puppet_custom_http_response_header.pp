# install Nginx web server using Puppet

package { 'nginx':
  ensure => installed,
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "server {
    listen 80 default_server;
    server_name _;

    rewrite ^/redirect_me https://www.github.com/med-i permanent;

    error_page 404 /404.html;
    location = /404.html {
      root /var/www/html;
      internal;
    }

    add_header X-Served-By $hostname;

    location / {
      root /var/www/html;
      index index.html index.htm;
    }
  }",
}

file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
}

exec { 'nginx-test':
  command => 'nginx -t',
  path    => '/usr/sbin',
  require => File['/etc/nginx/sites-available/default'],
}

service { 'nginx':
  ensure    => running,
  subscribe => File['/etc/nginx/sites-available/default'],
}

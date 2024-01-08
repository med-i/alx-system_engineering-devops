# install Nginx web server using Puppet

package { 'nginx':
  ensure => installed,
}

file { '/var/www/html/index.html':
  content => 'Hello, World!',
}

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "
server {
    add_header X-Served-By \$hostname;
    listen 80 default_server;
    server_name _;

    location /redirect_me {
      return 301 https://github.com/med-i;
    }

    error_page 404 /404.html;
    location = /404.html {
      root /var/www/html;
      internal;
    }

    location / {
      root /var/www/html;
      index index.html;
    }
  }",
}

service { 'nginx':
  ensure    => running,
  subscribe => File['/etc/nginx/sites-available/default'],
}

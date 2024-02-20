# rename class-wp-locale.phpp to class-wp-locale.php
exec { 'rename_class-wp-locale':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => ['/usr/bin', '/bin'],
}

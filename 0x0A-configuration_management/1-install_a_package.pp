# Ensure pip3 is installed
package { 'python3-pip':
  ensure => installed,
}

# Install Flask v2.1.0
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}

# makes the server accept connections without password
file_line { 'Declare identity file':
  path  => '/etc/ssh/ssh_config',
  line  => 'IdentityFile ~/.ssh/school',
}

file_line { 'Turn off passwordd authedntication':
  path  => '/etc/ssh/ssh_config',
  line  => 'PasswordAuthentication no',
}

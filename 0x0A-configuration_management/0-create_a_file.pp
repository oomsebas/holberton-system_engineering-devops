#puppet resource to create a file.

file {'/tmp/holberton':
  group   => www-data,
  owner   => www-data,
  mode    => '0744',
  content => 'I love puppet',
}

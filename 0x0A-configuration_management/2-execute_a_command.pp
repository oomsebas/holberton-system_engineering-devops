#puppet resource to execute a command

exec {'kill process':
  command => 'pkill -f ./killmenow',
  path    => '/usr/bin'
  }

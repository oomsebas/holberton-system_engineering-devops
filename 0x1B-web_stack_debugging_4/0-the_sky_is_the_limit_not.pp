#extend the limit of open files in the system
exec { 'change max of opened files':
      command => 'sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 2000\"/g"\
       /etc/default/nginx; service nginx restart',
      path    => ['/usr/bin', '/bin']
}


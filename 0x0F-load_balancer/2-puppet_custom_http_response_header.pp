#puppet script to modify nginx.config

include stdlib

file_line {'config2':
  path  => '/etc/nginx/nginx.conf',
  after => '^http*{*',
  line  => '        add_header X-Server-By $HOSTNAME;',
}

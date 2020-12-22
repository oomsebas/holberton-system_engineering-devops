#puppet script to modify nginx.config

include stdlib

file_line {'config2':
  path  => '/etc/nginx/nginx.conf',
  after => '^*types_hash_max_size*',
  line  => '        add_header X-Server-By $HOSTNAME;',
}

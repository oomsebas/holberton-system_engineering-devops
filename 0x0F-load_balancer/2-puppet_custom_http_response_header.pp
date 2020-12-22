#puppet script to modify nginx.config

include stdlib

exec {'install server 1':
     command => 'sudo apt-get -y update',
     path    => '/usr/bin'
      }
exec {'installs server 2':
     command => 'sudo apt-get upgrade',
     path    => '/usr/bin'
      }
exec {'installs server 3':
     command => 'sudo apt-get install -y nginx',
     path    => '/usr/bin'
      }
exec {'install server 4':
     command => 'sudo ufw allow "Nginx HTTP"',
     path    => '/usr/bin'
      }
file_line {'config2':
  path  => '/etc/nginx/nginx.conf',
  after => '^http*{*',
  line  => '        add_header X-Server-By $HOSTNAME;',
}

exec {'install server 5':
     command => '/bin/echo "Holberton School" | sudo tee /usr/share/nginx/html/index.html',
     path    => '/usr/bin:/usr/sbin:/bin'
      }

exec {'install server 6':
     command => 'sudo service nginx restart',
     path    => '/usr/bin'
      }

#puppet script to modify nginx.config


exec {'install server':
      command  => 'sudo apt-get update;
      sudo apt-get -y install nginx;
      sudo sed -i "21 i\\\tadd_header X-Served-By $HOSTNAME;" /etc/nginx/nginx.conf;
      sudo service nginx restart',
      provider => 'shell',
      }

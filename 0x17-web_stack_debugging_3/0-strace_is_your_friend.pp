# Fix error server 500 on apache for a typo en wp-file settings
exec { 'Fix server':
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path    => '/bin/'
}

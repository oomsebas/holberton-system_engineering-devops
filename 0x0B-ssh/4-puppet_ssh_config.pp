#puppet script to modify the ssh_confih archive

include stdlib
file_line {'config1':
  path  => '/etc/ssh/ssh_config',
  line  => '    PubkeyAuthentication yes',
  match => '^*PubkeyAuthentication*'
}
file_line {'config2':
  path  => '/etc/ssh/ssh_config',
  line  => '    IdentityFile ~/.ssh/holberton',
  match => '^*IdentityFile ~/.ssh/holberton*'
}
file_line {'config3':
  path  => '/etc/ssh/ssh_config',
  line  => '    KbdInteractiveAuthentication no',
  match => '^*KbdInteractiveAuthentication*'
}

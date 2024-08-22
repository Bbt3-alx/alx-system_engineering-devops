# login with the holberton user and open a file without any error message.

exec { 'change_limit':
  command => 'sed -i "/^holberton hard/s/4/50000" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}

exec { 'change_limit':
  command => 'sed -i "/^holberton soft/s/5/50000" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}

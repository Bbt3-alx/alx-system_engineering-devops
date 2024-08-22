# login with the holberton user and open a file without any error message.

exec { 'change_hard_limit':
  command => 'sed -i "/^holberton hard/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/:/usr/bin/',
  onlyif  => 'grep -q "^holberton hard.*4" /etc/security/limits.conf',
}

exec { 'change_soft_limit':
  command => 'sed -i "/^holberton soft/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/:/usr/bin/',
  onlyif  => 'grep -q "^holberton soft.*5" /etc/security/limits.conf',
  require => Exec['change_hard_limit'],
}

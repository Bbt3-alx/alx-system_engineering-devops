# Increase the ulimit for nginx

exec { 'ulimit_nginx':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/:/usr/bin/',
  onlyif  => 'grep -q "15" /etc/default/nginx',
}

# Restart nginx to apply the new ulimit
exec { 'restart_nginx':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d/:/usr/local/sbin/:/usr/local/bin/:/usr/sbin/:/usr/bin/:/sbin/:/bin/',
  require => Exec['ulimit_nginx'],
}

# This manisfest  kills a process named killmenow.


exec { 'pkill_process':
  command => 'pkill -f ./killmenow',
  path    => ['/bin', '/usr/bin'],
  onlyif  => 'pgrep -f ./killmenow',
}

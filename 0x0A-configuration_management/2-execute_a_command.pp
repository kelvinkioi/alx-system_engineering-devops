#Using Puppet, create a manifest that kills a process named killmenow

exec { 'kills a process':
  command => 'pkill "killmenow"',
  path    => ['/usr/bin', '/usr/sbin',], 
}

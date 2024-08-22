# Increases the number of requests that nginx server can handle

# Increase teh ulimit
exec { 'fix-nginx':
    command => 'sed -i "n/15/4096/" /etc/default/nginx',
    path    => '/usr/local/sbin:/usr/local/bin:/usr/bin:/sbin:/bin',
}
->
# Restart nginx
exec { 'nginx-restart':
    command => '/etc/init.d/nginx restart',
    path    => '/etc/init.d/',
}

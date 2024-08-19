# Setting HTTP header in server

# Update packages
exec { 'update_server':
	command => 'apt-get update',
	user    => 'root',
	provider => 'shell',
}

# Ensure nginx is installed 
package { 'nginx':
	ensure   => present,
	provider => 'apt'
}
->
# Update nginx configuration and add custom HTTP header
file_line { 'set_http_header':
	ensure  => 'present',
	path    => '/etc/nginx/sites-enabled/default',
	after   => 'listen 80 default_server;',
	line    => 'add_header X-Served-By $hostname;'
}
->
# Start nginx
service { 'nginx':
	ensure    => running,
	enable    => true,
	require   => Package['nginx']
}

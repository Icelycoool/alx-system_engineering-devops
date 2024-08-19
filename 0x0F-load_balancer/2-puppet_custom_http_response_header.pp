# Setting HTTP header in server

# Ensure nginx is installed 
package { 'nginx':
	ensure => installed,
}
->
# Update nginx configuration and add custom HTTP header
file_line { 'set_http_header':
	path    => '/etc/nginx/sites-enabled/default',
	line    => 'add_header X-Served-By $hostname;',
	match   => 'server_name _;',
	after   => 'server_name _;',
	require => Package['nginx'],
}
->
# Ensure nginx is running and will restart after changes
service { 'nginx':
	ensure    => running,
	enable    => true,
	require   => ['nginx']
}

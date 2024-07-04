# Puppet manifest to install and configure nginx

# Puppet manifest to install and configure Nginx

package { 'nginx':
  ensure => installed,
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
  require => Package['nginx'],
}

file_line { 'nginx_redirect':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => 'rewrite ^/redirect_me https://nginx.org/en permanent;',
  require => Package['nginx'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => [Package['nginx'], File['/var/www/html/index.html'], File_line['nginx_redirect']],
}

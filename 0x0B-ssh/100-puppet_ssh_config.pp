# Sets up client ssh configuration

exec { 'echo "PasswordAuthentication no\nIdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config':
        path    => '/bin/'
}

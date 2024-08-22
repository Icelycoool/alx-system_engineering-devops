# Enable the user holberton without error

# Increase hard file limit for Holberton user
exec { 'hard-file-limit-for-Holberton':
    command => 'sed -i "/^holberton hard/s/5/50000" /etc/security/limits.conf',
    path    => '/usr/local/bin/:/bin/'
}

# Increase soft file limit for Holberton
exec { 'soft-file-limit-for-Holberton':
    command => 'sed -i "/^holberton soft/s/4/50000/" /etc/security/limits.conf',
    path    => '/usr/local/bin/:/bin/'
}

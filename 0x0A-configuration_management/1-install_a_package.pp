#dd Using Puppet, install flask from pip3.


# Ensure pip3 is installed
# package { 'python3-pip3':
#  ensure => 'installed',
#c}


# Install Flask using pip3
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

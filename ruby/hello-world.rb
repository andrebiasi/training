#!/usr/bin/ruby -w

puts "Hello, Ruby!";

print <<EOF
Line 1
Line 2
Line 3
EOF

# This is a comment
#
BEGIN {
  puts "Initialising..."
}

=begin
comment line 1
comment line 2
=end

END {
  puts "Finalising..."
}
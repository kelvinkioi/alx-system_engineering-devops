#!/usr/bin/env ruby
#Regexp that searches for a particuar words starting
#with h and ends with and have a particuar pattern of characters
puts ARGV[0].scan(/h[b|t]{2,5}n/).join

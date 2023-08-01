#!/usr/bin/env ruby
#Regexp that searches for a particuar words
puts ARGV[0].scan(/h[b|t]{2,5}n/).join

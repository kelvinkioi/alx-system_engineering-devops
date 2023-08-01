#!/usr/bin/env ruby
#Regexp that searches for specific words
puts ARGV[0].scan(/h[b|t]{3,6}n/).join

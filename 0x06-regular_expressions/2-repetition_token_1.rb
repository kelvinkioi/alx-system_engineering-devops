#!/usr/bin/env ruby
#regular expression that will matches specific words
puts ARGV[0].scan(/h[t|b]{1,2}n/).join

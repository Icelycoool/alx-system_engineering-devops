#!/usr/bin/env ruby
# A regular expression that matches repetition token
put ARGV[0].scan(/hb+t{2,5}+n/).join

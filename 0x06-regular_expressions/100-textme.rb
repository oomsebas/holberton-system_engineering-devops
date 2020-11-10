#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:(\+?[A-Za-z0-9]+)\]\s{1}\[to:(\+?[A-Za-z0-9]+)\]\s{1}\[flags:(-?\d+\:-?\d+\:-?\d+\:-?\d+\:-?\d+)\]/).join(",")

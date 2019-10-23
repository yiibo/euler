#!/usr/bin/ruby

# Author: Yibo Weng
# Date: 26/07/2016

# Best Approximation Question in Euler
require 'pry'

class BestApprox
  def initialize(d,llim,ulim)
    @d,@llim,@ulim=d,llim,ulim
    @sum=0
    solve()
    disp()
  end

  def solve()
    #
    for n in @llim..@ulim
      n_root=Math.sqrt(n)
      if n_root.is_a? Integer then
        next
      end

      former_diff=Float::INFINITY
      for s in 2..@d
        for r in s*(Math.sqrt(n-1).floor)..s*(Math.sqrt(n+1).ceil)
          curr_diff=(r.to_f/s-n_root).abs
          if curr_diff > ((r-1.0)/s-n_root).abs then
            next
          elsif curr_diff < former_diff then
            former_diff=curr_diff
            # For debugging
            s_opt=s
          end
        end
      end
      @sum+=s_opt
    end
  end

  def disp()
    puts @sum
  end
end

#run=BestApprox.new(1000000000000,1,100000)
run=BestApprox.new(1000000000000,100000,100000)

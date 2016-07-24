#!/usr/bin/ruby

# Author: Yibo Weng
# Date: 22/07/2016

# Find largest prime factor

class LargestPrimeFactor
  def initialize(input)
    @input=input
  end

  # Brute Force Algorithm
  def brute()
    @lf=@input
    i=2
    while i < @lf do
      if @lf % i == 0
        @lf/=i
        i=2
      end
      i+=1
    end
  end

  def disp()
    puts @lf
  end
end

run=LargestPrimeFactor.new(6857)
run.disp()

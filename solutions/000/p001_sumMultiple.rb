#!/usr/bin/ruby

# Euler Project
# Problem 1: https://projecteuler.net/problem=1

# Author: Yibo Weng
# Date: 21/07/2016

# Find sum of all natural numbers below 1000 that are multiples of 3 or 5
class SumMultiple
  def initialize(input_no,upper)
    @i, @u = input_no, upper
  end

  def solve()
    # Boundary Conditions
    n = @u/@i
    if @u % @i == 0
      n-=1
    end

    # Arithmetic Sequence Formula
    @sum = n * @i *(1 + n)/2
  end

  def getSumMultiple
    solve()
    @sum
  end
end

upper=1000
sm3=SumMultiple.new(3,upper)
sm5=SumMultiple.new(5,upper)
sm15=SumMultiple.new(15,upper)
puts sm3.getSumMultiple() + sm5.getSumMultiple() - sm15.getSumMultiple()

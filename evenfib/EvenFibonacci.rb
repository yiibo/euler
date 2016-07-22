#!/usr/bin/ruby

# Author: Yibo Weng
# Date: 22/07/2016

class EvenFibonacci
  def initialize(upper)
    @u=upper
  end

  def solve()
    @fib=0
    fPrev=1
    f=2

    while f < @u do
      if f % 2 == 0
        @fib += f
      end
      f+=fPrev
      fPrev=f-fPrev
    end
  end

  def getFib()
    solve()
    @fib
  end

  def show()
    puts @fib
  end
end

run=EvenFibonacci.new(4000000)
x=run.getFib()
puts x

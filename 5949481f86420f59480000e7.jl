# Task:
# Given a list of integers, determine whether the sum of its elements is odd or even.

# Give your answer as a string matching "odd" or "even".

# If the input array is empty consider it as: [0] (array with a zero).

# Examples:
# Input: [0]
# Output: "even"

# Input: [0, 1, 4]
# Output: "odd"

# Input: [0, -1, -5]
# Output: "even"
# Have fun!

# function oddoreven(array)
    
#     return sum( array ) % 2 == 0 ? "even" : "odd"
#   # your code here
# end

function oddoreven( array )
    return iseven(reduce(xor, array; init=0)) ? "even" : "odd" 
end


using BenchmarkTools
using Test

@btime @testset "all" begin 
  @testset "Edge tests" begin
    @test oddoreven([0]) == "even"
    @test oddoreven([1]) == "odd"
    @test oddoreven(Array{Int}(undef, 0)) == "even"
  end

  @testset "Even tests" begin
    @test oddoreven([0, 1, 5]) == "even"
    @test oddoreven([0, 1, 3]) == "even"
    @test oddoreven([1023, 1, 2]) == "even"
  end

  @testset "Negative Even tests" begin
    @test oddoreven([0, -1, -5]) == "even"
    @test oddoreven([0, -1, -3]) == "even"
    @test oddoreven([-1023, 1, -2]) == "even"
  end

  @testset "Odd tests" begin
    @test oddoreven([0, 1, 2]) == "odd"
    @test oddoreven([0, 1, 4]) == "odd"
    @test oddoreven([1023, 1, 3]) == "odd"
  end

  @testset "Negative Odd tests" begin
    @test oddoreven([0, -1, 2]) == "odd"
    @test oddoreven([0, 1, -4]) == "odd"
    @test oddoreven([-1023, -1, 3]) == "odd"
  end
end

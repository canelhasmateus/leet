# Take an integer n (n >= 0) and a digit d (0 <= d <= 9) as an integer.

# Square all numbers k (0 <= k <= n) between 0 and n.

# Count the numbers of digits d used in the writing of all the k**2.

# Call nb_dig (or nbDig or ...) the function taking n and d as parameters and returning this count.

# Examples:
# n = 10, d = 1 
# the k*k are 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100
# We are using the digit 1 in: 1, 16, 81, 100. The total count is then 4.

# nb_dig(25, 1) returns 11 since
# the k*k that contain the digit 1 are:
# 1, 16, 81, 100, 121, 144, 169, 196, 361, 441.
# So there are 11 digits 1 for the squares of numbers between 0 and 25.
# Note that 121 has twice the digit 1.


function nb_dig(n, d)

    squares = map(i -> i * i, 0:n)
    digitizeds = map(digits, squares)
    flattened = reduce(vcat, digitizeds)
    return sum(map(i -> i == d, flattened))
    # your code
end

function nb_dig2(n, d)
    return sum(count(i->i==d, digits(i^2)) for i in 0:n)
end


function nb_dig3( n, d)
    return sum(count(==(d), digits(i * i)) for i in 0:n)
end

function nb_dig4(n, d)
  result = 0
  for i = 0:n
    for dig in digits(i^2)
      if dig == d
        result += 1
      end
    end
  end
  return result
end

using Test

using BenchmarkTools

@testset "nb_dig" begin

    @test nb_dig(5750, 0) == 4700
    @test nb_dig(11011, 2) == 9481
    @test nb_dig(12224, 8) == 7733

end

@btime nb_dig(5750, 0) == 4700
@btime nb_dig2(5750, 0) == 4700
@btime nb_dig3(5750, 0) == 4700
@btime nb_dig4(5750, 0) == 4700

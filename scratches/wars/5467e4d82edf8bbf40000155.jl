# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

# Examples:
# Input: 42145 Output: 54421

# Input: 145263 Output: 654321

# Input: 123456789 Output: 987654321



using Test

# function descendingorder(n)

#     sorted = s -> sort(s, rev = true)
#     parsed = s -> parse(Int, s)
#     splitted = s -> split(s, "")
#     joined = s -> join(s, "")
    
#     return n |> string |> splitted |> sorted |> joined |> parsed
#     # ...
# end

function descendingorder(n)

    sorted = s -> sort(s, rev = true)
    parsed = s -> parse(Int, s)    
    joined = s -> join(s, "")
    return n |> digits |> sorted |> joined |> parsed
    # ...
end






@testset "tests" begin
    @test descendingorder(0) == 0
    @test descendingorder(1) == 1
    @test descendingorder(123456789) == 987654321
end

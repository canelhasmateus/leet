# The input is a string str of digits. Cut the string into chunks (a chunk here is a substring of the initial string) of size sz (ignore the last chunk if its size is less than sz).
# 
# If a chunk represents an integer such as the sum of the cubes of its digits is divisible by 2, reverse that chunk; otherwise rotate it to the left by one position. Put together these modified chunks and return the result as a string.
# 
# If
# 
# sz is <= 0 or if str is empty return ""
# sz is greater (>) than the length of str it is impossible to take a chunk of size sz hence return "".


# todo complete
 
asInt(x) = parse(Int64, x)

function cubeSum(x :: String)
    return x |> asInt |> digits |> x -> x .^ 3 |> sum |> s -> mod(s, 2) == 0
end

function rev(x)
    return reverse(x)
end

function rot(x)
    return x[2:lastindex(x)-1]  * x[1]
end


function slice(acc, n)
    current = 1
    maxim = length(acc)
    result = []

    while true
        fin = current + n - 1
        if fin > maxim
            break
        end
        currentSlice = acc[current:fin]
        println(typeof(currentSlice))
        push!(result, currentSlice)
        current += n + 1
    end

    return result
end

function switch(x)
    if cubeSum(x)
        return rev(x)
    else
        return rot(x)
    end
end

function revrot(s, n)

    if n <= 0 || n > length(s)
        return ""
    end

    if s == ""
        return ""
    end

    results = map( switch , slice(s, n) )
    return join(results, "")
end

using Test

@testset begin

    @test revrot("1234", 0) == ""
    @test revrot("", 0) == ""
    @test revrot("733049910872815764", 5) == "330479108928157"

end

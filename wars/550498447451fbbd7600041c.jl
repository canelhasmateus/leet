#Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks whether the two arrays have the "same" elements, with the same multiplicities. "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

#Examples
#Valid arrays
#a = [121, 144, 19, 161, 19, 144, 19, 11]  
#b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]



function comp(array1, array2)

    if isnothing(array1) || isnothing(array2)
        return false
    end

    counts = Dict()

    for element in array2
        counts[element] = get(counts, element, 0) + 1
    end

    for element in array1
        key = element * element
        if !haskey(counts, key)
            return false
        end

        counts[key] = counts[key] - 1

    end


    for (key, value) in counts
        if value != 0
            return false
        end
    end

    return true

end





function comp2(array1, array2)

    return !isnothing(array1) &&
           !isnothing(array2) &&
           sort(array1) |> (x -> x .* x) == sort(array2)

end




using Test


@testset begin


    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
    @test comp(a1, a2) == true
    @test comp2(a1, a2) == true



    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11 * 21, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
    @test comp(a1, a2) == false
    @test comp2(a1, a2) == false
end

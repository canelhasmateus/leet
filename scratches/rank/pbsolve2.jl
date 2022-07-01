
function maxElement(n, maxSum, k)



    S1 = (k^2 + k) / 2
    S2 = (n - k - 1) * (n - k) / 2
    best = ceil((maxSum + S1 + S2) / n)
    return Int(best)

end


function f(n)

    sub = sort(n)
    println( sub )
    result = 0
    for index = 1:length(sub)
        result += n[index] * index
    end
    return result
end


function sortedSum(a)
    result = 0
    tmp = []
    for i in a        
        append!( tmp , i )
        result += f( tmp )
    end
    return result % (1E9 + 7)
end

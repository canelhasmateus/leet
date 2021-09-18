#Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the first one, excluding the last one).

# All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one.



function asint( string ) 
    return parse( Int64 , string)
end

function ipsbetween(start, finish)

    ip_regex = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    first_matches = match(ip_regex, start)
    second_matches = match(ip_regex, finish)

    total = 0
    for i in 1:4
        base = 256^(4 - i)
        total += base * (asint(second_matches[i]) - asint(first_matches[i]))
    end

    return total
end




using Test



using Test

@testset  begin

    @test ipsbetween("10.0.0.0", "10.0.0.50") == 50
    @test ipsbetween("20.0.0.10", "20.0.1.0") == 246

end




module testtoken

using Test
include("../src/token.jl") 

@testset "Basic Tokenization" begin

    @test tokenize('=') == Equals()
    @test tokenize('+') == Plus()
    @test tokenize('(') == LParens()
    @test tokenize(')') == RParens()
    @test tokenize('{') == LCurly()
    @test tokenize('}') == RCurly()
    @test tokenize(',') == Comma()
    @test tokenize(';') == SemiColon()

end



end

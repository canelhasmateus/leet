module testlexer
include("../src/lexer.jl")
include("../src/token.jl")
using Test

@testset "Char Tokens" begin

    input = "=+(){},;"
    mlexer = Lexer(input)
    @test mlexer.readPosition == 1
    @test next!(mlexer) == Equals()
    @test next!(mlexer) == Plus()
    @test next!(mlexer) == LParens()
    @test next!(mlexer) == RParens()
    @test next!(mlexer) == LCurly()
    @test next!(mlexer) == RCurly()
    @test next!(mlexer) == Comma()
    @test next!(mlexer) == SemiColon()

end

@testset "String Token" begin

    input = "
    let five = 5;
    let ten=10;
    let add = fn( x, y ) {
        x + y;
    };

    let result = add( five , ten);
    "

    lexer = Lexer(input)

    for token in [
        Let(), Ident("five"), Equals(), IntT(5), SemiColon(),
        Let(), Ident("ten"), Equals(), IntT(10), SemiColon(),
        Let(), Ident("add"), Equals(), Fn(), LParens(), Ident("x"), Comma(), Ident("y"), RParens(),
        LCurly(), Ident("x"), Plus(), Ident("y"), SemiColon(), RCurly(),
        Let(), Ident("result"), Equals(), Ident("add"), LParens(), Ident("five"), Comma(), Ident("ten"), RParens(), SemiColon(),
        EOF()]
        @test next!(lexer) == token
    end

end



end




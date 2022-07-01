include("token.jl")

mutable struct Lexer
    input::String
    position::Integer
    readPosition::Integer
    ch::Char
end

Lexer(input::String) = Lexer(input, 1, 1, input[1])

function next!(self::Lexer, kind::Type{Char})
    
    self.ch = self.input[self.readPosition]
    self.position = self.readPosition
    self.readPosition = self.readPosition + 1
end


function next!(self::Lexer, kind::Type{Token})::Token

    token , step = tokenize(self.input, self.readPosition)


    while token == Nothing

        token = 

    end

    token.readPosition 
    return token

end

next!(self::Lexer) = next!(self, Token)



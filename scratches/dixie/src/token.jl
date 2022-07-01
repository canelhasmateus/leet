

using Match

abstract type Token end

struct Comma <: Token end
struct Equals <: Token end
struct Plus <: Token end
struct LParens <: Token end
struct RParens <: Token end
struct LCurly <: Token end
struct RCurly <: Token end
struct SemiColon <: Token end
struct Let <: Token end
struct Fn <: Token end
struct EOF <: Token end
struct Ident <: Token
    literal::String
end
struct IntT <: Token
    literal::Integer
end



function all(f , itr)
    for i in itr
        result = f(i)
        if result == false
            return false
        end
    end
    return true

end


function tokenize(character::AbstractChar)::Token

    @match character begin
        '=' => Equals()
        '+' => Plus()
        '(' => LParens()
        ')' => RParens()
        '{' => LCurly()
        '}' => RCurly()
        ',' => Comma()
        ';' => SemiColon()
        '\x00' => EOF()
        _ => Nothing
    end
end

function tokenize(input::String , startingPosition :: Integer)::Token


    if word == "let"
        return Let()
    end

    if word == "fn"
        return Fn()
    end


    if all(isletter, word)
        return Ident(word)
    end
    if all(isdigit, word)
        value = parse(Integer, word)
        return IntT(value)
    end





end


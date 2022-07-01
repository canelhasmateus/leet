struct Positioned{T}
  position :: Integer
  element :: T 
  
end

function order(words)
    
    if words == "" return "" end
    
    pattern = r"[^\d]*([1-9]+)[^\d]*"

    to_match = (word) -> match(   pattern , word)[1]
    to_int = (word) -> parse( Int , word ) 
    to_position = (s) -> to_int( to_match( s ))

    to_struct = word -> Positioned( to_position( word ) , word)

    positionedList = map( to_struct , split( words , " "))
    positionedList = sort( positionedList  , by = p -> p.position)
    positionedList = map( p -> p.element , positionedList) 
    return join( positionedList, " ")

    # ...
end

using Test

@test order("is2 Thi1s T4est 3a") == "Thi1s is2 3a T4est"
@test order("4of Fo1r pe6ople g3ood th5e the2") == "Fo1r the2 g3ood 4of th5e pe6ople"
@test order("") == ""



content = open("./data/objects/pack/pack-ab791e31e145b51752796b39d86bd87751785a85.pack")
content = read(content)

##
using BenchmarkTools

abstract type GitElement end

struct Commit <: GitElement end

struct Tree <: GitElement end

struct Blob <: GitElement end

struct Tag <: GitElement end

struct OFS <: GitElement end

struct REF <: GitElement end


function unpack(content::Array{UInt8})::Int32
    return reinterpret(Int32, content)[1]
end

struct GitVersion
    version::Int32
    GitVersion(x) = new(unpack(reverse(x)))
end

struct Pack
    version::Int32
    objects::Array{GitElement}
end

mutable struct PackParser
    offset::Int32
    pack::Pack
end

abstract type GitStep end

struct HeaderStep <: GitStep
    stepSize::Int32
    version::Int32
    numObjects::Int32
end

struct ElementStep <: GitStep
    element::GitElement
end

function identify(kind::UInt8)::Type{<:GitElement}

    return if kind == "100"
        Commit
    elseif kind == "010"
        Tree
    elseif kind == "110"
        Blob
    elseif kind == "001"
        Tag
    elseif kind == "011"
        OFS
    elseif kind == "111"
        REF
    end

end

function advance!(parser::PackParser, step::HeaderStep)
    parser.offset += step.stepSize
    parser.pack = Pack(step.version, [])
end

function advance!(parser::PackParser, step::ElementStep)
    parser.offset += step.stepSize
    parser.pack
    push!(parser.pack.objects, step.element)
end

function parse(t::Type{HeaderStep}, content::Array{UInt8})::HeaderStep

    header = content[1:4]
    version = content[5:8]
    numObjects = reinterpret(Int32, content[9:12])[1]
    return HeaderStep(13, 2, numObjects)
end

function parse(t::Type{ElementStep}, content::Array{UInt8})::ElementStep

    offset = 1
    initialBits = bitstring(content[offset])
    element = identify(initialBits[2:5])
    
    while true

        if bits[0] != "1"
            break
        end
    end

end

function parse(::Type{Pack}, content::Array{UInt8})::Pack
    pack = Pack(0, [])
    parser = PackParser(0, pack)

    step = parse(HeaderStep, content)
    advance!(parser, step)


    size = length(content)
    while parser.offset < size
        step = parse(ElementStep, content[parser.offset:end])
        advance!(parser, step)
    end

    return parser.pack
end


parse(Pack, content)

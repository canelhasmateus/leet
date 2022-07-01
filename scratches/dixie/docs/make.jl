using dixie
using Documenter

DocMeta.setdocmeta!(dixie, :DocTestSetup, :(using dixie); recursive=true)

makedocs(;
    modules=[dixie],
    authors="Mateus Canelhas",
    repo="https://github.com/canelhasmateus/dixie.jl/blob/{commit}{path}#{line}",
    sitename="dixie.jl",
    format=Documenter.HTML(;
        prettyurls=get(ENV, "CI", "false") == "true",
        canonical="https://canelhasmateus.github.io/dixie.jl",
        assets=String[],
    ),
    pages=[
        "Home" => "index.md",
    ],
)

deploydocs(;
    repo="github.com/canelhasmateus/dixie.jl",
    devbranch="master",
)

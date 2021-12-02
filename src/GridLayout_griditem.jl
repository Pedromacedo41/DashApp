# AUTO GENERATED FILE - DO NOT EDIT

export GridLayout_griditem

"""
    GridLayout_griditem(;kwargs...)
    GridLayout_griditem(children::Any;kwargs...)
    GridLayout_griditem(children_maker::Function;kwargs...)


A GridItem component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): Dash-assigned callback that should be called to report property changes
to Dash, to make them available for callbacks.
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `h` (Real; optional)
- `i` (String; optional)
- `maxH` (Real; optional)
- `maxW` (Real; optional)
- `minH` (Real; optional)
- `minW` (Real; optional)
- `w` (Real; optional)
- `x` (Real; optional)
- `y` (Real; optional)
"""
function GridLayout_griditem(; kwargs...)
        available_props = Symbol[:children, :id, :h, :i, :maxH, :maxW, :minH, :minW, :w, :x, :y]
        wild_props = Symbol[]
        return Component("GridLayout_griditem", "GridItem", "gridlayout", available_props, wild_props; kwargs...)
end

GridLayout_griditem(children::Any; kwargs...) = GridLayout_griditem(;kwargs..., children = children)
GridLayout_griditem(children_maker::Function; kwargs...) = GridLayout_griditem(children_maker(); kwargs...)


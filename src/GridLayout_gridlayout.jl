# AUTO GENERATED FILE - DO NOT EDIT

export GridLayout_gridlayout

"""
    GridLayout_gridlayout(;kwargs...)
    GridLayout_gridlayout(children::Any;kwargs...)
    GridLayout_gridlayout(children_maker::Function;kwargs...)


A GridLayout component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional)
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `layout` (Array; optional): Dash-assigned callback that should be called to report property changes
to Dash, to make them available for callbacks.
"""
function GridLayout_gridlayout(; kwargs...)
        available_props = Symbol[:children, :id, :layout]
        wild_props = Symbol[]
        return Component("GridLayout_gridlayout", "GridLayout", "gridlayout", available_props, wild_props; kwargs...)
end

GridLayout_gridlayout(children::Any; kwargs...) = GridLayout_gridlayout(;kwargs..., children = children)
GridLayout_gridlayout(children_maker::Function; kwargs...) = GridLayout_gridlayout(children_maker(); kwargs...)


# AUTO GENERATED FILE - DO NOT EDIT

export areabump

"""
    areabump(;kwargs...)

An AreaBump component.

Keyword arguments:
- `id` (String; optional)
- `axisBottom` (Dict; optional)
- `axisTop` (Dict; optional)
- `blendMode` (String; optional)
- `clickedPoint` (Dict; optional)
- `colors` (Dict; optional)
- `data` (Array; required)
- `defs` (Array; optional)
- `endLabel` (String; optional)
- `fill` (Array; optional)
- `margin` (Dict; optional)
- `spacing` (Real; optional)
- `startLabel` (String; optional)
"""
function areabump(; kwargs...)
        available_props = Symbol[:id, :axisBottom, :axisTop, :blendMode, :clickedPoint, :colors, :data, :defs, :endLabel, :fill, :margin, :spacing, :startLabel]
        wild_props = Symbol[]
        return Component("areabump", "AreaBump", "dash_nivo", available_props, wild_props; kwargs...)
end


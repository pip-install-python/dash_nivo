# AUTO GENERATED FILE - DO NOT EDIT

export responsivecircle

"""
    responsivecircle(;kwargs...)

A ResponsiveCircle component.

Keyword arguments:
- `id` (String; optional)
- `borderColor` (Dict; optional)
- `borderWidth` (Real; optional)
- `childColor` (Dict; optional)
- `colors` (Dict; optional)
- `data` (Dict; required)
- `defs` (Array; optional)
- `enableLabels` (Bool; optional)
- `fill` (Array; optional)
- `labelTextColor` (Dict; optional)
- `labelsSkipRadius` (Real; optional)
- `margin` (Dict; optional)
- `motionConfig` (String; optional)
- `padding` (Real; optional)
- `zoomedId` (String; optional)
"""
function responsivecircle(; kwargs...)
        available_props = Symbol[:id, :borderColor, :borderWidth, :childColor, :colors, :data, :defs, :enableLabels, :fill, :labelTextColor, :labelsSkipRadius, :margin, :motionConfig, :padding, :zoomedId]
        wild_props = Symbol[]
        return Component("responsivecircle", "ResponsiveCircle", "dash_nivo", available_props, wild_props; kwargs...)
end


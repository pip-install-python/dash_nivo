# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AreaBump(Component):
    """An AreaBump component.


Keyword arguments:

- id (string; optional)

- axisBottom (dict; default {    tickSize: 5,    tickPadding: 5,    tickRotation: 0,    legend: '',    legendPosition: 'middle',    legendOffset: 32,    truncateTickAt: 0})

- axisTop (dict; default {    tickSize: 5,    tickPadding: 5,    tickRotation: 0,    legend: '',    legendPosition: 'middle',    legendOffset: -36,    truncateTickAt: 0})

- blendMode (string; default 'multiply')

- clickedPoint (dict; optional)

- colors (dict; default { scheme: 'nivo' })

- data (list; required)

- defs (list; default [    {        id: 'dots',        type: 'patternDots',        background: 'inherit',        color: '#38bcb2',        size: 4,        padding: 1,        stagger: True    },    {        id: 'lines',        type: 'patternLines',        background: 'inherit',        color: '#eed312',        rotation: -45,        lineWidth: 6,        spacing: 10    }])

- endLabel (string; default 'id')

- fill (list; default [    {        match: {            id: 'CoffeeScript'        },        id: 'dots'    },    {        match: {            id: 'TypeScript'        },        id: 'lines'    }])

- margin (dict; default { top: 40, right: 100, bottom: 40, left: 100 })

- spacing (number; default 8)

- startLabel (string; default 'id')"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_nivo'
    _type = 'AreaBump'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, data=Component.REQUIRED, margin=Component.UNDEFINED, spacing=Component.UNDEFINED, colors=Component.UNDEFINED, blendMode=Component.UNDEFINED, defs=Component.UNDEFINED, fill=Component.UNDEFINED, startLabel=Component.UNDEFINED, endLabel=Component.UNDEFINED, axisTop=Component.UNDEFINED, axisBottom=Component.UNDEFINED, clickedPoint=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'axisBottom', 'axisTop', 'blendMode', 'clickedPoint', 'colors', 'data', 'defs', 'endLabel', 'fill', 'margin', 'spacing', 'startLabel']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'axisBottom', 'axisTop', 'blendMode', 'clickedPoint', 'colors', 'data', 'defs', 'endLabel', 'fill', 'margin', 'spacing', 'startLabel']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['data']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AreaBump, self).__init__(**args)
